"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

from Partie import *


def conversion(nb_wagons):
    # convertit le nombre de wagons en nombre de points
    if nb_wagons == 1:
        return 1
    if nb_wagons == 2:
        return 2
    if nb_wagons == 3:
        return 4
    if nb_wagons == 4:
        return 7
    if nb_wagons == 5:
        return 10
    if nb_wagons == 6:
        return 15


graphe_villes = {}
graphe_villes['Los Angeles'] = ['San Francisco', 'Las Vegas', 'Phoenix', 'El Paso']
graphe_villes['San Francisco'] = ['Portland', 'Salt Lake City', 'Los Angeles']
graphe_villes['Portland'] = ['Seattle', 'Salt Lake City', 'San Francisco']
graphe_villes['Seattle'] = ['Portland', 'Helena', 'Vancouver', 'Calgary']
graphe_villes['Vancouver'] = ['Seattle', 'Calgary']
graphe_villes['Calgary'] = ['Winnipeg', 'Helena', 'Seattle', 'Vancouver']
graphe_villes['Helena'] = ['Seattle', 'Calgary', 'Winnipeg', 'Duluth', 'Omaha', 'Denver', 'Salt Lake City']
graphe_villes['Salt Lake City'] = ['Portland', 'San Francisco', 'Las Vegas', 'Denver', 'Helena']
graphe_villes['Las Vegas'] = ['Salt Lake City', 'Los Angeles']
graphe_villes['Phoenix'] = ['El Paso', 'Santa Fe', 'Los Angeles', 'Denver']
graphe_villes['El Paso'] = ['Santa Fe', 'Phoenix', 'Los Angeles', 'Houston', 'Dallas', 'Oklahoma City']
graphe_villes['Santa Fe'] = ['Phoenix', 'Denver', 'Oklahoma City', 'El Paso']
graphe_villes['Denver'] = ['Santa Fe', 'Phoenix', 'Salt Lake City', 'Helena', 'Omaha', 'Kansas City', 'Oklahoma City']
graphe_villes['Oklahoma City'] = ['Denver', 'Kansas City', 'Santa Fe', 'El Paso', 'Dallas', 'Little Rock']
graphe_villes['Kansas City'] = ['Denver', 'Omaha', 'Saint Louis', 'Oklahoma City']
graphe_villes['Omaha'] = ['Denver', 'Kansas City', 'Chicago', 'Duluth', 'Helena']
graphe_villes['Duluth'] = ['Winnipeg', 'Helena', 'Sault Ste Marie', 'Toronto', 'Chicago', 'Omaha']
graphe_villes['Sault Ste Marie'] = ['Winnipeg', 'Duluth', 'Toronto', 'Montreal']
graphe_villes['Winnipeg'] = ['Calgary', 'Helena', 'Duluth', 'Sault Ste Marie']
graphe_villes['Dallas'] = ['Houston', 'El Paso', 'Oklahoma City', 'Little Rock']
graphe_villes['Houston'] = ['Dallas', 'El Paso', 'New Orleans']
graphe_villes['New Orleans'] = ['Houston', 'Little Rock', 'Atlanta', 'Miami']
graphe_villes['Little Rock'] = ['New Orleans', 'Dallas', 'Oklahoma City', 'Saint Louis', 'Nashville']
graphe_villes['Saint Louis'] = ['Little Rock', 'Kansas City', 'Chicago', 'Pittsburgh', 'Nashville']
graphe_villes['Chicago'] = ['Saint Louis', 'Omaha', 'Duluth', 'Toronto', 'Pittsburgh']
graphe_villes['Nashville'] = ['Saint Louis', 'Pittsburgh', 'Little Rock', 'Atlanta', 'Raleigh']
graphe_villes['Atlanta'] = ['Nashville', 'Raleigh', 'Charleston', 'New Orleans', 'Miami']
graphe_villes['Miami'] = ['New Orleans', 'Atlanta', 'Charleston']
graphe_villes['Charleston'] = ['Miami', 'Atlanta', 'Raleigh']
graphe_villes['Pittsburgh'] = ['Washington', 'Raleigh', 'Nashville', 'Saint Louis', 'Chicago', 'Toronto', 'New York']
graphe_villes['Toronto'] = ['Pittsburgh', 'Chicago', 'Duluth', 'Sault Ste Marie', 'Montreal']
graphe_villes['Montreal'] = ['Boston', 'New York', 'Toronto', 'Sault Ste Marie']
graphe_villes['Boston'] = ['Montreal', 'New York']
graphe_villes['New York'] = ['Boston', 'Montreal', 'Pittsburgh', 'Washington']
graphe_villes['Washington'] = ['New York', 'Pittsburgh', 'Raleigh']
graphe_villes['Raleigh'] = ['Washington', 'Pittsburgh', 'Nashville', 'Atlanta', 'Charleston']


def parcours_profondeur(graph, noeud):
    """ L'algorithme parcours_profondeur renvoie """
    dejaVu = [noeud]
    A_visiter = [noeud]
    while A_visiter:
        noeud = A_visiter.pop()
        for voisin in graph[noeud]:
            if voisin not in dejaVu:
                dejaVu.append(voisin)
                A_visiter.append(voisin)
        return dejaVu


# print(parcours_profondeur(graphe_villes,'Toronto'))


class EnsembleDisjoint:
    """
    Cette classe permet de gérer les ensembles disjoints. Deux éléments sont
    considérés dans le même ensemble s'ils ont le même parent.
    """
    parent = {}

    # Création de 36 ensembles disjoints, état de départ de notre graphe
    def __init__(self, N=36):
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
    """Construction de l'arbre couvrant minimal à l'aide de l'algorithme de Kruskal.
    L'algorithme de Kruskal permet d'obtenir le plus court chemin entre deux villes."""
    arbre_minimal = []
    ed = EnsembleDisjoint(nombre_villes)
    index = 0
    while len(arbre_minimal) < nombre_villes - 1:
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
        # Objectifs = jr.main_cartes['Destination']

    def get_id_ville(self, nom_ville):
        return self.partie.villes[nom_ville].id

    def get_lien_villes(self, nom_ville1, nom_ville2):
        return self.partie.liens_villes[nom_ville1][nom_ville2][1]

    def get_infos_liaison(self, nom_ville1, nom_ville2):
        return self.get_id_ville(nom_ville1), self.get_id_ville(nom_ville2), self.get_lien_villes(nom_ville1,
                                                                                                  nom_ville2)

    def calcul_pts_destinations(self, joueur):
        # joueur.nb_points = 0
        # liaisons = []
        # for destination in joueur.main_destination:
        #     ville1, ville2 = [ville.strip() for ville in destination.strip().split("to")]
        #     liaisons.append(self.get_infos_liaison(ville1, ville2))
        nb_villes = 36
        arbre_min = Kruskal(liaisons, nb_villes)
        for destination in joueur.main_destination:
            ville1, ville2 = [ville.strip() for ville in destination.strip().split("to")]
            if (ville1 and ville2) in arbre_min:
                joueur.nb_points += self.partie.carte_destination[destination]
            else:
                joueur.nb_points -= self.partie.carte_destination[destination]

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

    def calcul_plus_long_chemin_joueur(self, joueur):
        villes_prises = []
        n = len(joueur.route_prise)
        for i in range(n):
            villes_prises.append(joueur.route_prise[i][0], joueur.route_prise[i][1])
        villes_prises = list(set(villes_prises))
        graphe_villes_joueur = graphe_villes
        for ville in graphe_villes:
            if ville not in villes_prises:
                del graphe_villes_joueur[ville]
        for ville in villes_prises:
            old_chemin = chemin
            chemin_bis = parcours_profondeur(ville, graphe_villes_joueur)
            if len(chemin_bis) > len(old_chemin):
                chemin = chemin_bis
        return chemin

    def trouver_indice_longueur_max(lst):
        maxList = max(lst, key=lambda i: len(i))
        index = maxList.index(maxList)
        return index

    def calcul_plus_long_chemin(self, partie):
        n = len(partie.les_joueurs)
        plus_longs_chemins = []
        les_joueurs = list(partie.les_joueurs)
        for i in range(n):
            plus_longs_chemins.append(self.calcul_plus_long_chemin_joueur(les_joueurs[i]))
        return self.trouver_indice_longueur_max(plus_longs_chemins)

    def attribue_points_plc(self, partie):
        i = self.calcul_plus_long_chemin(partie)
        partie.les_joueurs.nb_points[i] += 10


if __name__ == '__main__':
    # liste des liaisons au format (départ, arrivée, longueur)

    partie = Partie()
    score = Score(partie)

    liaisons = [score.get_infos_liaison("Los Angeles", "San Francisco"),
                score.get_infos_liaison("Los Angeles", "Las Vegas"),
                score.get_infos_liaison("Los Angeles", "Phoenix"),
                score.get_infos_liaison("Los Angeles", "El Paso"),
                score.get_infos_liaison("San Francisco", "Portland"),
                score.get_infos_liaison("San Francisco", "Salt Lake City"),
                score.get_infos_liaison("Portland", "Seattle"),
                score.get_infos_liaison("Portland", "Salt Lake City"),
                score.get_infos_liaison("Seattle", "Helena"),
                score.get_infos_liaison("Seattle", "Vancouver"),
                score.get_infos_liaison("Seattle", "Calgary"),
                score.get_infos_liaison("Vancouver", "Calgary"),
                score.get_infos_liaison("Calgary", "Winnipeg"),
                score.get_infos_liaison("Calgary", "Helena"),
                score.get_infos_liaison("Helena", "Winnipeg"),
                score.get_infos_liaison("Helena", "Duluth"),
                score.get_infos_liaison("Helena", "Omaha"),
                score.get_infos_liaison("Helena", "Denver"),
                score.get_infos_liaison("Helena", "Salt Lake City"),
                score.get_infos_liaison("Salt Lake City", "Las Vegas"),
                score.get_infos_liaison("Salt Lake City", "Denver"),
                score.get_infos_liaison("Phoenix", "El Paso"),
                score.get_infos_liaison("Phoenix", "Santa Fe"),
                score.get_infos_liaison("Phoenix", "Denver"),
                score.get_infos_liaison("El Paso", "Santa Fe"),
                score.get_infos_liaison("El Paso", "Houston"),
                score.get_infos_liaison("El Paso", "Dallas"),
                score.get_infos_liaison("El Paso", "Oklahoma City"),
                score.get_infos_liaison("Santa Fe", "Denver"),
                score.get_infos_liaison("Santa Fe", "Oklahoma City"),
                score.get_infos_liaison("Denver", "Omaha"),
                score.get_infos_liaison("Denver", "Kansas City"),
                score.get_infos_liaison("Oklahoma City", "Kansas City"),
                score.get_infos_liaison("Oklahoma City", "Dallas"),
                score.get_infos_liaison("Oklahoma City", "Little Rock"),
                score.get_infos_liaison("Kansas City", "Omaha"),
                score.get_infos_liaison("Kansas City", "Saint Louis"),
                score.get_infos_liaison("Omaha", "Chicago"),
                score.get_infos_liaison("Omaha", "Duluth"),
                score.get_infos_liaison("Duluth", "Winnipeg"),
                score.get_infos_liaison("Duluth", "Sault Ste Marie"),
                score.get_infos_liaison("Duluth", "Toronto"),
                score.get_infos_liaison("Duluth", "Chicago"),
                score.get_infos_liaison("Sault Ste Marie", "Winnipeg"),
                score.get_infos_liaison("Sault Ste Marie", "Duluth"),
                score.get_infos_liaison("Sault Ste Marie", "Toronto"),
                score.get_infos_liaison("Sault Ste Marie", "Montreal"),
                score.get_infos_liaison("Winnipeg", "Calgary"),
                score.get_infos_liaison("Dallas", "Houston"),
                score.get_infos_liaison("Dallas", "Little Rock"),
                score.get_infos_liaison("Houston", "New Orleans"),
                score.get_infos_liaison("New Orleans", "Little Rock"),
                score.get_infos_liaison("New Orleans", "Atlanta"),
                score.get_infos_liaison("New Orleans", "Miami"),
                score.get_infos_liaison("Little Rock", "Saint Louis"),
                score.get_infos_liaison("Little Rock", "Nashville"),
                score.get_infos_liaison("Saint Louis", "Chicago"),
                score.get_infos_liaison("Saint Louis", "Pittsburgh"),
                score.get_infos_liaison("Saint Louis", "Nashville"),
                score.get_infos_liaison("Chicago", "Toronto"),
                score.get_infos_liaison("Chicago", "Pittsburgh"),
                score.get_infos_liaison("Nashville", "Pittsburgh"),
                score.get_infos_liaison("Nashville", "Atlanta"),
                score.get_infos_liaison("Nashville", "Raleigh"),
                score.get_infos_liaison("Atlanta", "Raleigh"),
                score.get_infos_liaison("Atlanta", "Charleston"),
                score.get_infos_liaison("Atlanta", "Miami"),
                score.get_infos_liaison("Miami", "Charleston"),
                score.get_infos_liaison("Charleston", "Raleigh"),
                score.get_infos_liaison("Pittsburgh", "Washington"),
                score.get_infos_liaison("Pittsburgh", "Raleigh"),
                score.get_infos_liaison("Pittsburgh", "Toronto"),
                score.get_infos_liaison("Pittsburgh", "New York"),
                score.get_infos_liaison("Toronto", "Montreal"),
                score.get_infos_liaison("Montreal", "Boston"),
                score.get_infos_liaison("Montreal", "New York"),
                score.get_infos_liaison("Boston", "New York"),
                score.get_infos_liaison("New York", "Washington"),
                score.get_infos_liaison("Washington", "Raleigh")]

    liaisons.sort(key=lambda x: x[2])  # on trie les liaisons par longueur
    print(len(liaisons))
    nombre_villes = 36

    arbre_min = Kruskal(liaisons, nombre_villes)
    print(arbre_min)
