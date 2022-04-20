"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

# Imports :
from Jeu import Jeu
from Joueur import Joueur
from Score import Score


class Partie():
    """Classe qui est utilisé pour lancer une partie du jeu.
    Fait appel à la classe Jeu pour accéder à toutes les cartes et informations sur le plateau de jeu."""

    def __init__(self):
        self.les_joueurs = []
        self.nb_joueurs: int = 0
        self.carte = 'carte'
        # A compléter

    def debut_partie(self):
        """
        Définition des joueurs
        :return:
        """
        self.nb_joueurs = int(input('Nombre de joueurs pour la partie'))
        for k in range(self.nb_joueurs):
            self.les_joueurs.append(Joueur(input('Nom du Joueur ' + str(k + 1)), input(
                'Choisir sa couleur de Joueur parmi les suivantes : \n - blue \n - red \n - black \n - random'), 0))

    def choix_tour_joueur(self):
        """
        Définit le tour des joueurs en fonction de celui qui a le plus voyagé puis selon sens horaire.
        :return:
        L'ordre des joueurs de la partie
        """
        joueur_voyageur = input("Qui a le plus voyagé entre ces joueurs ? \n" + self.liste_joueurs())
        index_premier = self.les_joueurs.index(joueur_voyageur)
        if index_premier == 0:
            return "L'ordre des joueurs est établi comme suit : \n" + self.liste_joueurs()
        else:
            temp_joueur = []
            while len(self.les_joueurs) > index_premier:
                temp_joueur.append(self.les_joueurs.pop(index_premier))
            while len(self.les_joueurs) > 0:
                temp_joueur.append(self.les_joueurs.pop(0))
            self.les_joueurs = temp_joueur
            return "L'ordre des joueurs est établi comme suit : \n" + self.liste_joueurs()

    def liste_joueurs(self):
        """
        Renvoie la liste des joueurs en partie dans l'ordre de leur tour.
        :return:
        """
        liste_joueurs = ""
        for joueur in self.les_joueurs:
            liste_joueurs += joueur.nom_joueur + "\n"
        return liste_joueurs

    def tour(self):
        """
        Réalise 1 tour pour 1 joueur de toutes les actions possibles.
        :return:
        """

    def partie(self):
        """
        Fait tourner une partie complète du jeu. Du début à la fin.
        :return:
        """
        self.debut_partie()
        """
        Règle du jeu :
        Tour de jeu
        Le joueur qui a le plus voyagé commence. Par la suite, on joue dans le sens des aiguilles d’une montre. 
        À son tour, le joueur doit faire une et une seule des trois actions suivantes :"""
        self.choix_tour_joueur()


if __name__ == '__main__':
    p = Partie()
    p.partie()
    # test=input('test de input')
