
import pymongo
from pymongo import MongoClient
import pandas as pd
import streamlit as st
from art import *



#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Projet MongoDB",
                   page_icon=":books:",
                   layout='wide')

# Fonction titre centré
def centered_text(text, taille):
    st.markdown(f"<{taille} style='text-align: center;'>{text}</h3>", unsafe_allow_html=True)
    st.write("\n")
# Conversion du titre en ASCII art
texte = text2art("Bienvenue",font="Caligraphy")
# Affichage titre
st.markdown(f"```{texte}```")
st.title("sur l'application de gestion de votre Bibliothèque :books:")
texte=":books:"
centered_text("< == Veuillez choisir un onglet sur la gauche de votre écran", "h3")


#"broadway"
#"block"
#"big"
#"banner"
#"bubble"
#"lean"
#"mini"
#"script"
#"shadow"
#"slant"
#"letters"
#"Isometric3"
#"Caligraphy" *****
#"Swan" ***
