"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""


class Joueur():
    """
    Classe qui définit les attributs et cartes du joueur d'une partie.
    Il y aura ici les joueurs IA et humains. A nous de les définir comme on le souhaite.
    """
    def __init__(self,nom_couleur,points):
        self.joueur='name'          # Nom du joueur
        self.wagons=45              # Nombre de wagons maximum par joueur
        self.couleur=nom_couleur    # Définit la couleur du joueur
        self.nb_points=points       # Définit le marqueur de points du joueur
        self.mains={}               # Définit la main actuelle du joueur => contient toutes ses cartes

    @property
    def couleur(self):
        """
        Accesseur de la variable couleur
        :return: valeur de couleur
        """
        return self.__couleur

    @couleur.setter
    def couleur(self,nom_couleur):
        """
        Définit la valeur du paramètre et vérifie les conditions de définition
        :param nom_couleur: str
        :return: None
        """
        assert type(nom_couleur)==str
        self.__couleur=nom_couleur

































