
import pymongo
from pymongo import MongoClient
import pandas as pd
import streamlit as st

#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Recherche d'Ouvrages",
                   page_icon=":mag_right:",
                   layout='wide')



# Fonction titre centré
def centered_text(text):
    st.markdown(f"<h3 style='text-align: center;'>{text}</h3>", unsafe_allow_html=True)
    st.write("\n")
centered_text("Rechercher un Ouvrage")


# import DB
client = MongoClient()
db = client.MongoDB
Books = db.Books


# Double Curseur année
min_annee, max_annee = st.sidebar.slider(
"Sélectionnez l'intervalle de dates désiré :",
min_value = 1949,
max_value = 2030,
value = (1949,2024),
step = 1)

st.sidebar.markdown("***")

# fonction de création et affichage du DF
def dataframe(json):
    # Création du DataFrame
    df_books = pd.DataFrame(json)

    # Réorganisation du DF
    df_books.insert(1, 'Titre', df_books['title'])
    df_books.insert(2, 'Auteurs', df_books['authors'].apply(lambda x: ', '.join(x)))
    df_books.insert(3, 'Année', df_books['year'])
    df_books.insert(4, 'Type', df_books['type'].replace({'article': 'Article', 'Book': 'Livre', 'Phd': "Thèse"}))

    # Suppression des colonnes inutiles
    columns_to_drop = ['number', 'cites', 'volume', 'editor', 'isbn', 'series', 'publisher', 'type', 'title', 'pages', 'year', 'booktitle', 'url', 'authors']
    for column in columns_to_drop:
        if column in df_books.columns:
            df_books.drop(column, axis=1, inplace=True)
            
    ### COLOR ###
    pd.set_option("styler.render.max_elements", 600000)
    # Fonction pour appliquer la couleur aux cases
    def mettre_en_couleur(valeur):
        if valeur == 'Article':
            return 'color: red'
        elif valeur == 'Livre':
            return 'color: green'
        elif valeur == 'Thèse':
            return 'color: blue'
        else:
            return 'color: yellow'
        
    # Prise en compte du curseur année
    df_books_year = df_books[
    (df_books['Année']<=max_annee) & (df_books['Année']>=min_annee)
    ]
    
    # Appliquer le style rouge aux cases de la colonne 'Type'
    #df_books_styled = df_books_year.style.map(mettre_en_couleur, subset=['Type'])
            
    #afficher = st.dataframe(df_books_styled)
    afficher = st.dataframe(df_books_year)
    
    return afficher



# Fonction de recherche
def cherche(mode, colonne):
    json = []
    for item in Books.find({mode : {"$regex":colonne, "$options": "i"}}).sort('year'):
        if item == "Livre":
            item = "Book"
        elif item == "Thèse":
            item = "Phd"
        json.append(item)
    return json


# Choix du Mode de Recherche
recherche = st.sidebar.radio(
    "Comment voulez-vous rechercher ?",
    ('Par Titre', 'Par Auteur', "Par Type"))

st.sidebar.markdown("***")


    
# Menu déroulant des TITRES
if recherche == "Par Titre":
    liste_titres = []
    for item in Books.find({"title" : {"$regex":"", "$options": "i"}}).sort('title') :
        liste_titres.append(item['title'])
    liste_titres.sort()
    liste_titres.append('Tous')
    titre = st.sidebar.selectbox(
    'Titre', liste_titres, index=liste_titres.index('Tous')
    )
    if titre == 'Tous':
        json = list(Books.find())
    else :
        json = cherche("title", titre)



# Menu déroulant des AUTEURS
elif recherche == "Par Auteur":
    set_auteurs = set([])
    for item in Books.find({"authors" : {"$regex":"", "$options": "i"}}).sort('authors') :
        for i in range (len(item['authors'])) :
            item['authors'][i] = item['authors'][i].replace('?','')
            set_auteurs.add(item['authors'][i])
    liste_auteurs = list(set_auteurs)
    liste_auteurs.sort()
    liste_auteurs.append('Tous')
    auteur = st.sidebar.selectbox(
    'Auteur', liste_auteurs, index=liste_auteurs.index('Tous')
    )
    if auteur == 'Tous':
        json = list(Books.find())
    else :
        json = cherche("authors", auteur)
        
        
        
# Menu déroulant des TYPES
elif recherche == "Par Type":
    set_types = set([])
    for item in Books.find({"type" : {"$regex":"", "$options": "i"}}).sort('type') :
        set_types.add(item['type'])
    liste_types = list(set_types)
    liste_types = ["Article" if x == "Article" else "Livre" if x == "Book" else "Thèse" if x == "Phd" else x for x in liste_types]
    liste_types.sort()
    liste_types.append('Tous')
    type = st.sidebar.selectbox(
    'Type', liste_types, index=liste_types.index('Tous')
    )
    if type == 'Tous':
        json = list(Books.find())
    else :
        if type == "Livre":
            type = "Book"
        elif type == "Thèse":
            type = "Phd"
        json = cherche("type", type)



# AFFICHAGE DU DATAFRAME
dataframe(json)