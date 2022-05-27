"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

from Joueur import Joueur as jr
# from Partie import Partie
# TODO: check the imports to avoid looping imports.

def conversion(nb_wagons):
    #convertit le nombre de wagons en nombre de points
    if nb_wagons == 1 :
        return 1
    if nb_wagons == 2 :
        return 2
    if nb_wagons == 3 :
        return 4
    if nb_wagons == 4 :
        return 7
    if nb_wagons == 5 :
        return 10
    if nb_wagons == 6 :
        return 15


class EnsembleDisjoint:
    """
    Cette classe permet de gérer les ensembles disjoints. Deux éléments sont
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
    arbre_minimal = []
    ed = EnsembleDisjoint(nombre_villes)
    index = 0
    while len(arbre_minimal) < nombre_villes - 1 :
        (depart, arrivee, longueur) = liaisons[index]
        index += 1

        x = ed.get_parent(depart)
        y = ed.get_parent(arrivee)

        if x != y:
            arbre_minimal.append((depart, arrivee, longueur))
            ed.Union(x, y)
        return arbre_minimal

class Score():
    """Classe qui implémente les différentes méthodes pour calculer les joueur.nb_points du jeu
    => Il pourra y avoir plusieurs méthodes de calcul des joueur.nb_points sur le graphe. A voir selon le temps qu'on a."""

    def __init__(self, partie):
        self.compte = 'compte le score'
        self.partie = partie
        # self.tableau_score = {
        # 1 : 1,
        # 2
        # }
        # A compléter
        # nb_joueurs = pt.nb_joueurs
        # L = nb_joueurs*[0]
        # for i in range(nb_joueurs):
        # L[i] = []
        #Objectifs = jr.main_cartes['Destination']

    def get_id_ville(self,nom_ville):
        return self.partie.villes[nom_ville].id

    def get_lien_villes(self,nom_ville1,nom_ville2):
        return self.partie.liens_villes[nom_ville1][nom_ville2][1]

    def get_infos_liaison(self,nom_ville1,nom_ville2):
        return (self.get_id_ville(nom_ville1),self.get_id_ville(nom_ville2),self.get_lien_villes(nom_ville1,nom_ville2))

    def calcul_pts_destinations(self, joueur):
        joueur.nb_points = 0
        for j in range(3):
            if (joueur.main_cartes[1][j][0][0] and joueur.main_cartes[1][j][0][1]) in arbre_min:
                joueur.nb_points += joueur.main_cartes[1][j][1]
            else:
                joueur.nb_points += joueur.main_cartes[1][j][1]

    def calcul_pts_route(self, joueur):
        """
        Compte le nb de points gagnés par les joueurs lors de la prise d'une route.
        :param joueur:
        :return:
        """
        for r in joueur.route_prise:
            ville1 = r[0]
            ville2 = r[1]
            joueur.nb_points += conversion(self.partie.liens_villes[ville1][ville2][1])
        return joueur.nb_points


    def calcul_plus_long_chemin(self,joueur):
       pass



if __name__ == '__main__':

# liste des liaisons au format (départ, arrivée, longueur)

    partie = Partie()
    score = Score(partie)

    liaisons = [score.get_infos_liaison("Los Angeles","San Francisco"),
                score.get_infos_liaison("Los Angeles","Las Vegas"),
                score.get_infos_liaison("Los Angeles","Phoenix"),
                score.get_infos_liaison("Los Angeles","El Paso"),
                score.get_infos_liaison("San Francisco","Portland"),
                score.get_infos_liaison("San Francisco","Salt Lake City"),
                score.get_infos_liaison("Portland","Seattle"),
                score.get_infos_liaison("Portland","Salt Lake City"),
                score.get_infos_liaison("Seattle","Helena"),
                score.get_infos_liaison("Seattle","Vancouver"),
                score.get_infos_liaison("Seattle","Calgary"),
                score.get_infos_liaison("Vancouver","Calgary"),
                score.get_infos_liaison("Calgary","Winnipeg"),
                score.get_infos_liaison("Calgary","Helena"),
                score.get_infos_liaison("Helena","Winnipeg"),
                score.get_infos_liaison("Helena","Duluth"),
                score.get_infos_liaison("Helena","Omaha"),
                score.get_infos_liaison("Helena","Denver"),
                score.get_infos_liaison("Helena","Salt Lake City"),
                score.get_infos_liaison("Salt Lake City","Las Vegas"),
                score.get_infos_liaison("Salt Lake City","Denver"),
                score.get_infos_liaison("Phoenix","El Paso"),
                score.get_infos_liaison("Phoenix","Santa Fe"),
                score.get_infos_liaison("Phoenix","Denver"),
                score.get_infos_liaison("El Paso","Santa Fe"),
                score.get_infos_liaison("El Paso","Houston"),
                score.get_infos_liaison("El Paso","Dallas"),
                score.get_infos_liaison("El Paso","Oklahoma City"),
                score.get_infos_liaison("Santa Fe","Denver"),
                score.get_infos_liaison("Santa Fe","Oklahoma City"),
                score.get_infos_liaison("Denver","Omaha"),
                score.get_infos_liaison("Denver","Kansas City"),
                score.get_infos_liaison("Oklahoma City","Kansas City"),
                score.get_infos_liaison("Oklahoma City","Dallas"),
                score.get_infos_liaison("Oklahoma City","Little Rock"),
                score.get_infos_liaison("Kansas City","Omaha"),
                score.get_infos_liaison("Kansas City", "Saint Louis"),
                score.get_infos_liaison("Omaha","Chicago"),
                score.get_infos_liaison("Omaha","Duluth"),
                score.get_infos_liaison("Duluth","Winnipeg"),
                score.get_infos_liaison("Duluth","Sault Ste Marie"),
                score.get_infos_liaison("Duluth","Toronto"),
                score.get_infos_liaison("Duluth","Chicago"),
                score.get_infos_liaison("Sault Ste Marie","Winnipeg"),
                score.get_infos_liaison("Sault Ste Marie","Duluth"),
                score.get_infos_liaison("Sault Ste Marie","Toronto"),
                score.get_infos_liaison("Sault Ste Marie","Montreal"),
                score.get_infos_liaison("Winnipeg","Calgary"),
                score.get_infos_liaison("Dallas","Houston"),
                score.get_infos_liaison("Dallas","Little Rock"),
                score.get_infos_liaison("Houston","New Orleans"),
                score.get_infos_liaison("New Orleans","Little Rock"),
                score.get_infos_liaison("New Orleans","Atlanta"),
                score.get_infos_liaison("New Orleans","Miami"),
                score.get_infos_liaison("Little Rock","Saint Louis"),
                score.get_infos_liaison("Little Rock","Nashville"),
                score.get_infos_liaison("Saint Louis","Chicago"),
                score.get_infos_liaison("Saint Louis","Pittsburgh"),
                score.get_infos_liaison("Saint Louis","Nashville"),
                score.get_infos_liaison("Chicago","Toronto"),
                score.get_infos_liaison("Chicago","Pittsburgh"),
                score.get_infos_liaison("Nashville","Pittsburgh"),
                score.get_infos_liaison("Nashville","Atlanta"),
                score.get_infos_liaison("Nashville","Raleigh"),
                score.get_infos_liaison("Atlanta","Raleigh"),
                score.get_infos_liaison("Atlanta","Charleston"),
                score.get_infos_liaison("Atlanta","Miami"),
                score.get_infos_liaison("Miami","Charleston"),
                score.get_infos_liaison("Charleston","Raleigh"),
                score.get_infos_liaison("Pittsburgh","Washington"),
                score.get_infos_liaison("Pittsburgh","Raleigh"),
                score.get_infos_liaison("Pittsburgh","Toronto"),
                score.get_infos_liaison("Pittsburgh","New York"),
                score.get_infos_liaison("Toronto","Montreal"),
                score.get_infos_liaison("Montreal","Boston"),
                score.get_infos_liaison("Montreal","New York"),
                score.get_infos_liaison("Boston","New York"),
                score.get_infos_liaison("New York","Washington"),
                score.get_infos_liaison("Washington","Raleigh")]

    liaisons.sort(key=lambda x: x[2])  # on trie les liaisons par longueur
    nombre_villes = 36

    arbre_min = Kruskal(liaisons, nombre_villes)
    print(arbre_min)