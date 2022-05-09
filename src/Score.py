"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

from Joueur import Joueur as jr
#from Partie import Partie as pt

class EnsembleDisjoint:
    """
    Cette classe permet de gérer les ensmebles disjoints. Deux éléments sont
    considérés dans le même ensemble s'ils ont le même parent.
    """
    parent = {}

    # Création de n ensemble disjoints, état de départ de notre graphe
    def __init__(self, N):
        for i in range(N):
            self.parent[i] = i

    # Fonction qui permet de retrouver le parent le plus lointain
    def get_parent(self, k):
        if self.parent[k] == k:
            return k

        return self.get_parent(self.parent[k])

    # Union de deux ensembles jusque là disjoints
    def Union(self, a, b):
        x = self.get_parent(a)
        y = self.get_parent(b)

        self.parent[x] = y

def Kruskal(liaisons, nombre_villes):
    """Construction de l'arbre couvrant minimal à l'aide de l'algorithme de Kruskal"""
    arbre_minimal =[]
    ed = EnsembleDisjoint(nombre_villes)
    index = 0
    while len(arbre_minimal) != nombre_villes - 1 :
        (depart, arrivee, longueur) = liaisons[index]
        index = index + 1

        x = ed.get_parent(depart)
        y = ed.get_parent(arrivee)

        if x != y :
            arbre_minimal.apppend((depart, arrivee, longueur))
            ed.Union(x,y)
        return arbre_minimal

class Score():
    """Classe qui implémente les différentes méthodes pour calculer les joueur.nb_points du jeu
    => Il pourra y avoir plusieurs méthodes de calcul des joueur.nb_points sur le graphe. A voir selon le temps qu'on a."""
    def __init__(self,partie):
        self.compte='compte le score'
        self.partie=partie
        #self.tableau_score = {
            #1 : 1,
            #2
        #}
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

    #def calcul_plus_long_chemin(self,joueur):
        #for r in self.joueur.route_prise :
            #ville =





if __name__ == '__main__':

# liste des arcs au format (départ, arrivée, longueur)

    liaisons = [("Los Angeles", "San Franciso", 3),("Los Angeles", "Las Vegas", 2),
                ("Los Angeles", "Phoenix", 3),("Los Angeles", "El Paso", 6),
                ("San Francisco", "Portland", 5),("San Francisco", "Salt Lake City", 5),
                ("Portland", "Seattle", 1),("Portland", "Salt Lake City", 6),
                ("Seattle", "Helena", 6),("Seattle", "Vancouver", 1),
                ("Seattle", "Calgary", 4),("Vancouver","Calgary",3),
                ("Calgary", "Winnipeg", 6),("Calgary", "Helena", 4),
                ("Helena", "Winnipeg", 4),("Helena", "Duluth", 6),
                ("Helena", "Omaha", 5),("Helena", "Denver", 4),
                ("Helena", "Salt Lake City", 3),("Salt Lake City", "Las Vegas", 3),
                ("Salt Lake City","Denver",3),("Phoenix","El Paso",3),
                ("Phoenix","Santa Fe",3),("Phoenix", "Denver", 5),
                ("El Paso","Santa Fe",2),("El Paso","Houston",6),
                ("El Paso","Dallas",4),("El Paso", "Oklahoma City", 5),
                ("Santa Fe","Denver",2),("Santa Fe", "Oklahoma City", 3),
                ("Denver","Omaha",4),("Denver","Kansas City",4),
                ("Oklahoma City","Kansas City",2),("Oklahoma City","Dallas",2),
                ("Oklahoma City","Little Rock",2),("Kansas City","Omaha",1),
                ("Kansas City", "Saint Louis",2),("Omaha","Chicago",4),
                ("Omaha", "Duluth", 2),("Duluth","Winnipeg",4),
                ("Duluth", "Sault Ste Marie", 3),("Duluth","Toronto",6),
                ("Duluth", "Chicago", 3),("Sault Ste Marie","Winnipeg",6),
                ("Sault Ste Marie","Duluth",3),("Sault Ste Marie","Toronto",2),
                ("Sault Ste Marie","Montreal",5),("Winnipeg","Calgary",6),
                ("Dallas","Houston",1),("Dallas","Little Rock",2),
                ("Houston","New Orleans",2),("New Orleans","Little Rock",3),
                ("New Orleans","Atlanta",4),("New Orleans","Miami",6),
                ("Little Rock","Saint Louis",2),("Little Rock","Nashville",3),
                ("Saint Louis","Chicago",2),("Saint Louis","Pittsburgh",5),
                ("Saint Louis","Nashville",2),("Chicago","Toronto",4),
                ("Chicago","Pittsburgh",3),("Nashville","Pittsburgh",4),
                ("Nashville","Atlanta",1),("Nashville","Raleigh", 3),
                ("Atlanta","Raleigh",2),("Atlanta","Charleston",2),
                ("Atlanta","Miami",5),("Miami","Charleston",4),
                ("Charleston","Raleigh",2),("Pittsburgh","Washington",2),
                ("Pittsburgh","Raleigh",2),("Pittsburgh","Toronto",2),
                ("Pittsburgh","New York",2),("Toronto","Montreal",3),
                ("Montreal","Boston",2),("Montreal","New York",3),
                ("Boston","New York",2),("New York","Boston",2),
                ("Boston","Washington",2),("Washington","Raleigh",2,)]

    liaisons.sort(key=lambda x: x[2]) # on trie les liaisons par longueur
    nombre_villes = 36

    print(Kruskal(liaisons, nombre_villes))