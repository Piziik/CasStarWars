from Acteur import Acteur
from Personnage import Personnage
from operator import attrgetter

##Classe Film
class Film:
    ##Constructeur
    def __init__(self, titre, annee, nbEpisode, cout, recette, acteurs):
        self.titre = titre
        self.annee = annee
        self.nbEpisode = nbEpisode
        self.cout = cout
        self.recette = recette
        self.acteurs = acteurs

    ##Getter/Setter
    def get_titre(self):
        return self.titre
    def set_titre(self, x):
        self.titre = x

    ##Modification de la methode __str__ afin d'afficher le message souhaité
    def __str__(self):
        return f'Le titre du film est {self.titre}, il est sortit en {self.annee}\nIl s\'agit du {self.nbEpisode}ème épisodes. Le film coûte {self.cout}€ et à fait {self.recette}€ de recette'

    ##Methode qui permet d'afficher les informations des films d'une liste de films
    def afficherInfosCollectionFilm(collectionFilm):
        for i in range(len(collectionFilm)):
            print(collectionFilm[i])

    ##Methode qui renvoi le nombre d'acteurs d'un film
    def nbActeursFilm(film):
        nbActeurs = len(film.acteurs)
        return nbActeurs

    ##Methode qui renvoi le nombre de personnages d'un film
    def nbPersonnagesFilm(film):
        nbPersonnage = 0
        collectionActeurs = film.acteurs
        for i in range(len(collectionActeurs)):
            nbPersonnage += Acteur.nbPersonnagesActeur(collectionActeurs[i])
        return nbPersonnage

    ##Methode qui calcule le bénéfice d'un film donné
    def benefice(film):
        calcul = film.recette - film.cout
        if(calcul < 1 and calcul != 0):
            deficit = calcul
            print(f"Le film à un déficit de {deficit} €")
        elif(calcul == 0):
            print(f"Le film est ni en bénéfice ni en déficit")
        else:
            benefice = calcul
            print(f"Le film est bénéficiare de {benefice} €")

    ##Methode qui renvoi "True" si l'année d'un film est en dessous d'une année donnée en paramètre (renvoi "False" sinon)
    def isBeforeAnnee(film, annee):
        beforeAnnee = False
        anneeFilm = film.annee
        if(annee > anneeFilm):
            beforeAnnee = True
        return beforeAnnee