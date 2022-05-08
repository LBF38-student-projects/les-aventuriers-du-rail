"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

from Joueur import Joueur as jr
from Partie import *

class Score(object):
    """Classe qui implémente les différentes méthodes pour calculer les joueur.nb_points du jeu
    => Il pourra y avoir plusieurs méthodes de calcul des joueur.nb_points sur le graphe. A voir selon le temps qu'on a."""
    def __init__(self,partie):
        self.compte='compte le score'
        self.partie=partie
        self.tableau_score = {
            1 : 1,
        }
        #A compléter
        #nb_joueurs = pt.nb_joueurs
        #L = nb_joueurs*[0]
        #for i in range(nb_joueurs):
            #L[i] = []
        Objectifs = jr.main_cartes['Destination']

    def calcul_pts_destinations(self,joueur):
        joueur.nb_points = 0
        for r in self.joueur.route_prise :
            nv_nom_route = "{0} to {1}".format(r[0], r[1])
            if nv_nom_route not in self.joueur.mains_cartes['Destination']:
                nv_nom_route = "{0} to {1}".format(r[1], r[0])
            elif nv_nom_route not in self.joueur.mains_cartes['Destination']:
                joueur.nb_points = joueur.nb_points
            else :
                joueur.nb_points += self.partie.carte_destination["nv_nom_route"]

    def calcul_pts_route(self,joueur):
        """
        Compte le nb de points gagnés par les joueurs lors de la prise d'une route.
        :param joueur:
        :return:
        """
        for r in joueur.route_prise :
            ville1 = r[0]
            ville2 = r[1]
            joueur.nb_points += self.partie.liens_villes[ville1][ville2][1]

    def calcul_plus_long_chemin(self,joueur):
        # for r in joueur.route_prise :
        #     ville =
        return "A implémenter"