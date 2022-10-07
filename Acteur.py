class Acteur:
    ##Constructeur
    def __init__(self, nom, prenom, personnages):
        self.nom = nom
        self.prenom = prenom
        self.personnages = personnages

    ##Getter/Setter
    def get_nom(self):
        return self.nom
    def set_nom(self, x):
        self.nom = x


    ##Modification de la methode __str__ afin d'afficher le message souhaité
    def __str__(self):
        return f"L'acteur s'appelle {self.prenom} {self.nom}, il incarne {self.personnages}"

    ##Methode qui affiche le nombre de personnages pour un acteur donné
    def nbPersonnagesActeur(acteur):
        nbPersonnagesActeur = len(acteur.personnages)
        return nbPersonnagesActeur
