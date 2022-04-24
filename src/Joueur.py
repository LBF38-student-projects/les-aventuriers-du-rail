"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

# Imports :
from abc import abstractmethod, ABCMeta, ABC


class Joueur():
    """
    Classe qui définit les attributs et cartes du joueur d'une partie.
    Il y aura ici les joueurs IA et humains. A nous de les définir comme on le souhaite.
    """

    def __init__(self, nom_joueur, nom_couleur, points):
        self.nom_joueur: str = nom_joueur  # Nom du joueur
        self.wagons = 45  # Nombre de wagons maximum par joueur
        self.couleur = nom_couleur  # Définit la couleur du joueur
        self.nb_points = points  # Définit le marqueur de points du joueur
        self.main_cartes = {
            'Wagon': {
                'violet': 0,
                'blanc': 0,
                'bleu': 0,
                'jaune': 0,
                'orange': 0,
                'noir': 0,
                'rouge': 0,
                'vert': 0,
                'locomotive': 0
            },
            'Destination': []  # Réunit toutes les cartes Destination du joueur. Ne contient que les noms des cartes.
        }  # Définit la main actuelle du joueur => contient toutes ses cartes
        self.route_prise={}

    @property
    def couleur(self):
        """
        Accesseur de la variable couleur
        :return: valeur de couleur
        """
        return self.__couleur

    @couleur.setter
    def couleur(self, nom_couleur):
        """
        Définit la valeur du paramètre et vérifie les conditions de définition
        :param nom_couleur: str
        :return: None
        """
        assert type(nom_couleur) == str
        self.__couleur = nom_couleur
