# - :books: Gestionnaire de Librairie :books:      -

Projet réalisé à partir d'une bases de données open source de 118.000 livres.

Projet individuel réalisé en 2 semaines.

##
## Sujet :
Le sujet de ce projet était de réaliser un système de gestion permettant à une librairie de gérer son stock de livres.
La base de données étant héberger sur MongoDB avec pour contrainte d'utiliser Pymongo pour les requêtes.
Fonctionnalités demandées :
* Recherche de livres dans la base de données
* Ajout d'un nouveau livre
* Suppression d'un livre via son identifiant

##
## Réponse apportée :

J'ai répondu au sujet en utilisant une interface Streamlit.
* L'onglet Recherche permet de faire une recherche dans la base de données via un titre, un auteur, un type d'ouvrage et de limiter les dates via un curseur.
* L'onglet Ajout permet d'ajouter un nouveau livre avec son titre, son ou ses auteur(s), son année de publication et son type. Un identifiant est généré automatiquement.
* L'onglet Suppression permet de supprimer un livre via son identifiant ou tous les livres d'un auteur en sélectionnant l'auteur désiré.
* L'onglet Statistiques permet d'afficher le nombre d'ouvrages, la répartition par type d'ouvrages, la répartition par année, le nombre d'auteurs, le top 10 des auteurs les plus prolifiques de la base et le nombre de livres par auteur.

##
## Outils utilisés :
* MongoDB
* Python
* PyMongo
* Streamlit
* Pandas
* Matplotlib et Seaborn
