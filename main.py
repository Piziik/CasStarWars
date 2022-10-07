from Film import Film
from Acteur import Acteur
from Personnage import Personnage

##Permet à l'utilisateur de choisir ses valeurs pour créer un objet de type Film
titre = input("Entrez un titre pour le film\n")
annee = int(input("Entrez une annee pour le film\n"))
episode = int(input("Entrez l'épisode du film\n"))
cout = int(input("Entrez le cout du film\n"))
recette = int(input("Entrez les recettes du film\n"))

##Initialise un acteur
acteur1 = Acteur("Ford", "Harrison", ["Han Solo", "Indiana Jones", "Plouf"])
acteur2 = Acteur("Oultaf", "Yanis", ["JarJar Binks", "OuiOui", "Yanis Maverick"])
acteur3 = Acteur("Joubert", "Tristan", ["Dark Vador", "Grevious", "Dora"])

##Initialise des films
film1 = Film("StarWars", 1977, 4, 11000000, 5000000000, [acteur1, acteur2, acteur3])
film2 = Film("StarWars", 1980, 5, 11000000, 5000000000, [acteur1])
film3 = Film(titre, annee, episode, cout, recette, [acteur1])

##Initialise un personnage
personnage1 = Personnage("Solo", "Han")

##Initialise une liste de film
listeDeFilm = [film1, film2, film3]

##Test des méthodes

##Affiche les infos de chaque films contenus dans une liste de films
Film.afficherInfosCollectionFilm(listeDeFilm)
##Affiche le nombre de personnages d'un acteur donné
Acteur.nbPersonnagesActeur(acteur1)

##Affiche le nombre d'acteurs d'un film donné
print(f"Ce film à {Film.nbPersonnagesFilm(film1)} acteurs")
##Affiche le nombre de personnages d'un film donné
print(f"Ce film à {Film.nbPersonnagesFilm(film1)} personnages")
##Affiche si le film est en déficit ou en bénéfice et de combien
Film.benefice(film3)
##Affiche "True" si l'année du film donné en paramètre est en dessous d'une année également donnée en paramètre
print(Film.isBeforeAnnee(film3, 2000))