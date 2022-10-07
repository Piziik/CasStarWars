##Classe personnage
class Personnage:
    ##Constructeur
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    ##Getter/Setter
    def get_nom(self):
        return self.nom
    def set_nom(self, x):
        self.nom = x

    ##Methode __str__
    def __str__(self):
        return f"Le personnage s'appelle {self.prenom} {self.nom}"
