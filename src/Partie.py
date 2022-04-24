"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

# Imports :
import random

from Joueur import Joueur
from Score import Score
import matplotlib.pyplot as plt
import random as r


class Jeu():
    """Classe qui met en place les parties immuables du jeu pour ensuite être utilisé dans chaque partie."""

    def __init__(self):
        """Définit les éléments immuables du jeu classique.
        ---
        Cartes wagons :
        - Variable : carte_wagons
        - Type : dictionnaire
        - Syntaxe : "nom de la carte": nb de cartes

        Cartes destination :
        - Variable : carte_destination
        - Type : dictionnaire
        - Syntaxe : "Nom de la carte": nb de points
        """
        self.carte_wagons = {
            "violet": 12,
            "blanc": 12,
            "bleu": 12,
            "jaune": 12,
            "orange": 12,
            "noir": 12,
            "rouge": 12,
            "vert": 12,
            "locomotive": 14
        }
        self.carte_destination = {
            "Los Angeles to New York": 21,
            "Duluth to Houston": 8,
            "Sault Ste Marie to Nashville": 8,
            "New York to Atlanta": 6,
            "Portland to Nashville": 17,
            "Vancouver to Montreal": 20,
            "Duluth to El Paso": 10,
            "Toronto to Miami": 10,
            "Portland to Phoenix": 11,
            "Dallas to New York": 11,
            "Calgary to Salt Lake City": 7,
            "Calgary to Phoenix": 13,
            "LA to Miami": 20,
            "Winnipeg to Little Rock": 11,
            "San Francisco to Atlanta": 17,
            "Kansas City to Houston": 5,
            "Los Angeles to Chicago": 16,
            "Denver to Pittsburgh": 11,
            "Chicago to Santa Fe": 9,
            "Vancouver to Santa Fe": 13,
            "Boston to Miami": 12,
            "Chicago to New Orleans": 7,
            "Montreal to Atlanta": 9,
            "Seattle to New York": 22,
            "Denver to El Paso": 4,
            "Helena to Los Angeles": 8,
            "Winnipeg to Houston": 12,
            "Montreal to New Orleans": 13,
            "Sault Ste Marie to Oklahoma City": 9,
            "Seattle to Los Angeles": 9
        }
        self.villes = {
            "Los Angeles": (4, 5),
            "San Francisco": (1.5, 9),
            "Portland": (2, 17),
            "Seattle": (3, 19),
            "Vancouver": (3, 21),
            "Calgary": (8, 21.5),
            "Helena": (12, 16.5),
            "Salt Lake City": (9, 12),
            "Las Vegas": (7, 7.5),
            "Phoenix": (9, 5),
            "El Paso": (13.5, 4),
            "Santa Fe": (14, 7),
            "Denver": (14, 10.5),
            "Oklahoma City": (20, 8),
            "Kansas City": (20.5, 11),
            "Omaha": (19.5, 13),
            "Duluth": (21, 17),
            "Winnipeg": (17, 21),
            "Sault Ste Marie": (25.5, 19),
            "Dallas": (20.5, 5),
            "Houston": (22, 3),
            "New Orleans": (25.5, 3.5),
            "Little Rock": (23, 8),
            "Saint Louis": (24, 11),
            "Chicago": (25.5, 14),
            "Nashville": (27, 10),
            "Atlanta": (29, 8),
            "Miami": (34, 2),
            "Charleston": (33, 8),
            "Pittsburgh": (30, 15),
            "Toronto": (30, 18),
            "Montreal": (33, 22),
            "Boston": (35.5, 19.5),
            "New York": (33.5, 16.5),
            "Washington": (34, 13),
            "Raleigh": (31.5, 10.5)
        }
        self.liens_villes = {
            "Los Angeles": {
                "San Francisco": ["yellow", 3],
                "Las Vegas": ["grey", 2],
                "Phoenix": ["grey", 3],
                "El Paso": ["black", 6]
            },
            "San Francisco": {
                "Portland": ["orange", 5],
                "Salt Lake City": ["orange", 5],
                "Los Angeles": ["yellow", 3]
            },
            "Portland": {
                "Seattle": ["grey", 1],
                "Salt Lake City": ["blue", 6],
                "San Francisco": ["orange", 5]
            },
            "Seattle": {
                "Portland": ["grey", 1],
                "Helena": ["yellow", 6],
                "Vancouver": ["grey", 1],
                "Calgary": ["grey", 4]
            },
            "Vancouver": {
                "Seattle": ["grey", 1],
                "Calgary": ["grey", 3]
            },
            "Calgary": {
                "Winnipeg": ["white", 6],
                "Helena": ["grey", 4],
                "Seattle": ["grey", 4],
                "Vancouver": ["grey", 3]
            },
            "Helena": {
                "Seattle": ["yellow", 6],
                "Calgary": ["grey", 4],
                "Winnipeg": ["blue", 4],
                "Duluth": ["orange", 6],
                "Omaha": ["red", 5],
                "Denver": ["orange", 4],
                "Salt Lake City": ["grey", 3]
            },
            "Salt Lake City": {
                "Portland": ["blue", 6],
                "San Francisco": ["orange", 5],
                "Las Vegas": ["orange", 3],
                "Denver": ["yellow", 3],
                "Helena": ["grey", 3]
            },
            "Las Vegas": {
                "Salt Lake City": ["orange", 3],
                "Los Angeles": ["grey", 2]
            },
            "Phoenix": {
                "El Paso": ["grey", 3],
                "Santa Fe": ["grey", 3],
                "Los Angeles": ["grey", 3],
                "Denver": ["white", 5]
            },
            "El Paso": {
                "Santa Fe": ["grey", 2],
                "Phoenix": ["grey", 3],
                "Los Angeles": ["black", 6],
                "Houston": ["orange", 6],
                "Dallas": ["red", 4],
                "Oklahoma City": ["yellow", 5]
            },
            "Santa Fe": {
                "Phoenix": ["grey", 3],
                "Denver": ["grey", 2],
                "Oklahoma City": ["blue", 3],
                "El Paso": ["grey", 2]
            },
            "Denver": {
                "Santa Fe": ["grey", 2],
                "Phoenix": ["white", 5],
                "Salt Lake City": ["yellow", 3],
                "Helena": ["orange", 4],
                "Omaha": ["grey", 4],
                "Kansas City": ["black", 4],
                "Oklahoma City": ["red", 4]
            },
            "Oklahoma City": {
                "Denver": ["red", 4],
                "Kansas City": ["grey", 2],
                "Santa Fe": ["blue", 3],
                "El Paso": ["yellow", 6],
                "Dallas": ["grey", 2],
                "Little Rock": ["grey", 2]
            },
            "Kansas City": {
                "Denver": ["orange", 4],
                "Omaha": ["grey", 1],
                "Saint Louis": ["grey", 2],
                "Oklahoma City": ["grey", 2]
            },
            "Omaha": {
                "Denver": ["grey", 4],
                "Kansas City": ["grey", 1],
                "Chicago": ["blue", 4],
                "Duluth": ["grey", 2],
                "Helena": ["red", 5]
            },
            "Duluth": {
                "Winnipeg": ["white", 4],
                "Helena": ["orange", 6],
                "Sault Ste Marie": ["grey", 3],
                "Toronto": ["grey", 6],
                "Chicago": ["red", 3],
                "Omaha": ["grey", 2]
            },
            "Sault Ste Marie": {
                "Winnipeg": ["grey", 6],
                "Duluth": ["grey", 3],
                "Toronto": ["grey", 2],
                "Montreal": ["black", 5]
            },
            "Winnipeg": {
                "Calgary": ["white", 6],
                "Helena": ["blue", 4],
                "Duluth": ["black", 4],
                "Sault Ste Marie": ["grey", 6]
            },
            "Dallas": {
                "Houston": ["grey", 1],
                "El Paso": ["red", 4],
                "Oklahoma City": ["grey", 2],
                "Little Rock": ["grey", 2]
            },
            "Houston": {
                "Dallas": ["grey", 1],
                "El Paso": ["orange", 6],
                "New Orleans": ["grey", 2]
            },
            "New Orleans": {
                "Houston": ["grey", 2],
                "Little Rock": ["orange", 3],
                "Atlanta": ["yellow", 4],
                "Miami": ["red", 6]
            },
            "Little Rock": {
                "New Orleans": ["orange", 3],
                "Dallas": ["grey", 2],
                "Oklahoma City": ["grey", 2],
                "Saint Louis": ["grey", 2],
                "Nashville": ["white", 3]
            },
            "Saint Louis": {
                "Little Rock": ["grey", 2],
                "Kansas City": ["grey", 2],
                "Chicago": ["white", 2],
                "Pittsburgh": ["orange", 5],
                "Nashville": ["grey", 2]
            },
            "Chicago": {
                "Saint Louis": ["white", 2],
                "Omaha": ["blue", 4],
                "Duluth": ["red", 3],
                "Toronto": ["white", 4],
                "Pittsburgh": ["black", 3]
            },
            "Nashville": {
                "Saint Louis": ["grey", 2],
                "Pittsburgh": ["yellow", 4],
                "Little Rock": ["white", 3],
                "Atlanta": ["grey", 1],
                "Raleigh": ["black", 3]
            },
            "Atlanta": {
                "Nashville": ["grey", 1],
                "Raleigh": ["grey", 2],
                "Charleston": ["grey", 2],
                "New Orleans": ["yellow", 4],
                "Miami": ["blue", 5]
            },
            "Miami": {
                "New Orleans": ["red", 6],
                "Atlanta": ["blue", 5],
                "Charleston": ["grey", 4]
            },
            "Charleston": {
                "Miami": ["grey", 4],
                "Atlanta": ["grey", 2],
                "Raleigh": ["grey", 2]
            },
            "Pittsburgh": {
                "Washington": ["grey", 2],
                "Raleigh": ["grey", 2],
                "Nashville": ["yellow", 4],
                "Saint Louis": ["orange", 5],
                "Chicago": ["black", 3],
                "Toronto": ["grey", 2],
                "New York": ["orange", 2]
            },
            "Toronto": {
                "Pittsburgh": ["grey", 2],
                "Chicago": ["white", 4],
                "Duluth": ["grey", 6],
                "Sault Ste Marie": ["grey", 2],
                "Montreal": ["grey", 3]
            },
            "Montreal": {
                "Boston": ["grey", 2],
                "New York": ["blue", 3],
                "Toronto": ["grey", 3],
                "Sault Ste Marie": ["black", 5]
            },
            "Boston": {
                "Montreal": ["grey", 2],
                "New York": ["yellow", 2]
            },
            "New York": {
                "Boston": ["yellow", 2],
                "Montreal": ["blue", 3],
                "Pittsburgh": ["orange", 2],
                "Washington": ["black", 2]
            },
            "Washington": {
                "New York": ["black", 2],
                "Pittsburgh": ["grey", 2],
                "Raleigh": ["grey", 2]
            },
            "Raleigh": {
                "Washington": ["grey", 2],
                "Pittsburgh": ["grey", 2],
                "Nashville": ["black", 3],
                "Atlanta": ["grey", 2],
                "Charleston": ["grey", 2]
            },
        }

    def plateau(self):
        """Définit le plateau du jeu
        => Construit le graphe des villes
        Affiche un point pour chaque ville avec le nom en dessous
        Relie chaque ville par un trait gris quand non occupé
        """
        plateau = plt.figure()

        """Affichage des liens entre les villes :"""
        for ville in self.liens_villes.keys():
            x_ville, y_ville = self.villes[ville]
            for ville2 in self.liens_villes[ville].keys():
                nom_lien, couleur_lien = ville2, self.liens_villes[ville][ville2][0]
                x_liens, y_liens = self.villes[nom_lien]
                plt.plot((x_ville, x_liens), (y_ville, y_liens), couleur_lien, linewidth=5)
        """Affichage des points + noms des villes :"""
        for ville in self.villes.keys():
            x, y = self.villes[ville]
            plt.plot(x, y, 'ro')
            plt.text(x - 1, y - 1, ville)
        """Arrière-plan du plateau :"""
        ax = plt.axes()
        ax.set_facecolor('lightgrey')
        return plateau

    def capture_route(self):
        """
        Capture la route si le joueur a suffisamment de cartes wagon selon la couleur de la route.
        :return:
        """
        return "A implémenter"


class Partie(Jeu):
    """Classe qui est utilisé pour lancer une partie du jeu.
    Fait appel à la classe Jeu pour accéder à toutes les cartes et informations sur le plateau de jeu."""

    def __init__(self):
        super().__init__()
        self.les_joueurs = {}  # Dictionnaire contenant tous les noms + objet Joueur de la partie.
        self.ordre = []  # Liste de l'ordre dans lequel joue les joueurs. Contient le nom de chaque joueur dans l'ordre.
        self.nb_joueurs: int = 0
        self.pile_cartes_wagon = [carte for carte, nb_carte in self.carte_wagons.items() for k in range(nb_carte)]
        # Définit l'ordre des cartes wagons. C'est la pile de cartes.
        self.pile_cartes_destination=[destination for destination in self.carte_destination.keys()]

    def debut_partie(self):
        """
        Définition des joueurs
        :return:
        """
        self.nb_joueurs = int(input('Nombre de joueurs pour la partie'))
        for k in range(self.nb_joueurs):
            nom = input('Nom du Joueur ' + str(k + 1))
            couleur = input('Choisir sa couleur de Joueur parmi les suivantes :\n- blue\n- red\n - black \n - random')
            self.les_joueurs[nom] = Joueur(nom, couleur, 0)
            self.ordre.append(nom)
        # TODO : Demander le nb total de joueurs de la partie, nb joueurs humains. => compléter par des joueurs IAs
        # TODO: vérifier que nb_joueurs est compris entre 2 et 5.

    def rotation_joueur(self, index):
        """
        Réalise la rotation des joueurs selon l'indice fourni dans le sens horaire.
        :return:
        L'ordre des joueurs
        """
        if index != 0:
            temp_joueur = []
            while len(self.ordre) > index:
                temp_joueur.append(self.ordre.pop(index))
            while len(self.ordre) > 0:
                temp_joueur.append(self.ordre.pop(0))
            self.ordre = temp_joueur
        return "L'ordre des joueurs est établi comme suit : \n" + self.liste_joueurs()

    def choix_tour_joueur(self):
        """
        Définit le tour des joueurs en fonction de celui qui a le plus voyagé puis selon sens horaire.
        :return:
        L'ordre des joueurs de la partie
        """
        joueur_voyageur = input("Qui a le plus voyagé entre ces joueurs ? \n" + self.liste_joueurs())
        self.rotation_joueur(self.ordre.index(joueur_voyageur))

    def liste_joueurs(self):
        """
        Renvoie la liste des joueurs en partie dans l'ordre de leur tour.
        :return:
        """
        liste_joueurs = ""
        for joueur in self.ordre:
            liste_joueurs += joueur + "\n"
        return liste_joueurs

    def tour(self, joueur):
        """
        Réalise 1 tour de tous les joueurs où chacun joue leur tour de jeu en fonction de toutes les actions possibles.
        :return:
        """
        print("C'est le tour de " + joueur.nom_joueur)
        choix: int = int(input(
            "Que voulez-vous faire ?\n" + "1. Prendre des cartes Wagon\n2. Prendre possession d'une route\n3. "
                                          "Prendre des cartes Destination supplémentaires\nIndiquer le numéro "
                                          "de l'action choisie"))
        if choix == 1:
            self.prendre_cartes_wagon()
        elif choix == 2:
            self.prendre_route()
        else:
            print("Non disponible pour le moment")
            # self.prendre_cartes_Destination()

    def melange_cartes(self, pile_cartes: list):
        """
        Mélange des cartes.
        Renvoie un paquet totalement mélangé aléatoirement.
        :return:
        """
        n = len(pile_cartes)
        for k in range(n):
            index1, index2 = r.randint(0, n - 1), r.randint(0, n - 1)
            pile_cartes[index1], pile_cartes[index2] = pile_cartes[index2], pile_cartes[index1]
        return pile_cartes

    def melange_americain(self, paquet: list):
        """
        Mélange les cartes à la façon américaine.
        Renvoie un paquet mélangé selon cette façon.

        Principe du mélange :
            On prend la moitié du paquet.
            On mélange les cartes en les entrelaçant aléatoirement (entre 1 et 3 cartes de chaque petit paquet)
            On les réunit pour terminer le mélange.
        :return:
        """
        n = len(paquet)
        p1 = paquet[0:n // 2]
        n1 = len(p1)
        p2 = paquet[n // 2:]
        n2 = len(p2)
        # TODO : pour les tests, vérifier que len(p1)+len(p2)=len(paquet)
        for carte in p2:
            index = r.randint(0, n1)
            p1.insert(index, carte)
        return p1

    def prendre_cartes_wagon(self):
        """
         1. Prendre des cartes Wagon :
        – le joueur peut prendre 2 cartes Wagon.
        Il peut prendre n’importe quelle carte visible parmi les 5 posées sur la table ou tirer une carte du dessus de
        la pioche (tirage en aveugle). Si le joueur prend une carte visible, il la remplace immédiatement par une
        autre du dessus de la pioche. Il peut ensuite prendre une deuxième carte, soit visible, soit en aveugle (voir
        section Cartes Wagon pour les cartes Locomotive).
        :return:
        """
        """Indication sur les cartes Wagon : 
        Cartes Wagon 
        
        Il existe 8 types de wagons différents en plus de la locomotive. Les couleurs de chaque carte Wagon 
        correspondent aux couleurs présentes sur le plateau AFIN de relier les villes : bleu, violet, orange, blanc, 
        vert, jaune, noir et rouge. Les locomotives sont multicolores et, comme des cartes joker, peuvent remplacer 
        n’importe quelle couleur lors de la prise de possession d’une route."""

        """"
        Il est possible de ne jouer que des cartes Locomotive pour prendre une route. Si une carte Locomotive figure 
        parmi les 5 cartes visibles, le joueur peut la prendre, mais son tour s’arrête alors. La locomotive compte 
        comme si l’on avait pris 2 cartes. Si, après avoir pris une carte visible (qui n’est pas une locomotive), 
        la carte de remplacement est une locomotive, le joueur ne peut pas la prendre. Si, au cours du jeu, 
        3 cartes visibles sur 5 sont des locomotives, les 5 cartes sont alors immédiatement défaussées et remplacées 
        par 5 nouvelles cartes. 
        
        Note : Si un joueur a la chance de tirer une locomotive en aveugle, au sommet de la pioche, les autres 
        joueurs n’en savent rien et cette carte ne compte que pour une seule carte piochée. Un joueur peut avoir en 
        main et à tout moment autant de cartes qu’il le souhaite. Quand la pioche de cartes est épuisée, les cartes 
        défaussées sont soigneusement mélangées pour reconstituer une nouvelle pioche. Il est important de bien 
        mélanger les cartes car elles ont été défaussées par séries de couleurs ! Dans le cas peu probable où il n’y 
        aurait plus de cartes disponibles (si toutes les cartes sont dans les mains des joueurs) un joueur ne peut 
        plus prendre de cartes. Il ne peut donc que prendre possession d’une route ou tirer de nouvelles cartes 
        Destination. """

        print("Je prends des cartes Wagon")
        print("A implémenter")
        return None

    def prendre_route(self):
        """
        2. Prendre possession d’une route :
        – Le joueur peut s’emparer d’une route sur le plateau en posant autant de cartes Wagon de la couleur
        de la route que d’espaces composant la route. Après avoir défaussé ses cartes, le joueur pose alors ses wagons
        sur chaque espace constituant la route. Enfin, il déplace son marqueur de score en se référant au tableau de
        décompte des points.
        :return:
        """

        """Indication:
        Prendre possession des routes
        Pour prendre possession d’une route, un joueur doit jouer une série de cartes égale au
        nombre d’espaces composant la route. La série de cartes doit être composée de cartes du
        même type. La plupart des routes nécessitent une série de cartes de couleur spécifique. Par
        exemple, les routes bleues sont capturées en posant des cartes Wagon bleues. Certaines
        routes – en gris sur le plateau - peuvent être capturées en utilisant n’importe quelle série
        d’une même couleur.
        Lorsqu’une route a été capturée, le joueur pose ses wagons en plastique sur chacun des
        espaces qui constituent la route. Toutes les cartes utilisées pour s’approprier cette route
        sont défaussées.
        Un joueur peut prendre possession de n’importe quelle route sur le plateau de jeu. Il n’est
        pas obligé de se connecter avec les routes déjà à son actif. Un joueur ne peut jamais prendre
        plus d’une route par tour de jeu.
        Une route prise par un joueur devient sa propriété exclusive. Aucun
        autre joueur ne peut plus revendiquer son
        usage ou son occupation.
        Certaines villes sont reliées par des routes
        doubles. Un même joueur ne peut pas prendre
        2 routes reliant les 2 mêmes villes.
        Note importante : Dans une configuration
        à 2 ou 3 joueurs, seule l’une des routes constituant la double
        connexion peut être utilisée. Un joueur peut donc prendre
        possession de l’une des 2 routes disponibles, la route restante
        demeurant fermée jusqu’à la fin de la partie.
        """
        print("Je prends une route")
        print("A implémenter")
        return None

    def preparation_partie(self):
        """
        Prépare la partie selon les règles.
        Préparation du jeu :
        Mélangez les cartes Wagon et distribuez-en 4 à chacun des joueurs. Placez le reste
        des cartes près du plateau, face cachée, puis retournez les cinq premières cartes que
        vous posez à côté, face visible.
        Posez la carte Chemin le plus long, face visible, à côté du plateau.
        Mélangez les cartes Destination et distribuez-en 3 à chaque joueur. Chaque joueur
        peut maintenant regarder ses destinations afin de décider lesquelles conserver. Il doit
        garder au moins 2 cartes, mais peut conserver les 3 s’il le souhaite. Chaque carte rendue
        est placée sous le talon des cartes Destination. Le paquet de cartes Destination est ensuite
        placé face cachée à côté du plateau. Les joueurs gardent leurs destinations secrètes
        jusqu’à la fin du jeu.
        Vous êtes maintenant prêts à jouer.
        :return:
        """
        self.pile_cartes_wagon=self.melange_cartes(self.pile_cartes_wagon)
        self.pile_cartes_wagon=self.melange_americain(self.pile_cartes_wagon)
        self.pile_cartes_destination=self.melange_cartes(self.pile_cartes_destination)
        self.pile_cartes_destination=self.melange_americain(self.pile_cartes_destination)
        for joueur in self.les_joueurs.values():
            for k in range(4):
                joueur.main_cartes['Wagon'][self.pile_cartes_wagon.pop(0)] += 1
            for i in range(3):
                joueur.main_cartes['Destination'].append(self.pile_cartes_destination.pop(0))


    def partie(self):
        """
        fait tourner une partie complète du jeu. du début à la fin.
        :return:
        """
        self.debut_partie()
        self.preparation_partie()
        """
        # Règle du jeu :
        ## Tour de jeu
        Le joueur qui a le plus voyagé commence."""
        self.choix_tour_joueur()
        """Par la suite, on joue dans le sens des aiguilles d’une montre. 
        À son tour, le joueur doit faire une et une seule des trois actions suivantes : 
        1. Prendre des cartes Wagon
        2. Prendre possession d’une route
        3. Prendre des cartes Destination supplémentaires
        """
        i = 0
        nom = self.ordre[i]
        joueur = self.les_joueurs[nom]
        while joueur.wagons > 2:
            self.tour(joueur)
            if i >= len(self.ordre):
                i = 0
            else:
                i += 1
            nom = self.ordre[i]
            joueur = self.les_joueurs[nom]
        self.rotation_joueur(i)
        for nom in self.ordre:
            self.tour(self.les_joueurs[nom])
        print("Fin de partie\nAffichage du score bientôt disponible")
        """
        Fin du jeu
        Lorsque la réserve de wagons d’un joueur est de 0, 1 ou 2 wagons après avoir joué son tour, 
        chaque joueur, en incluant celui-ci, joue encore un tour. À l’issue de ce dernier tour, le jeu s’arrête et 
        chacun compte ses points """


if __name__ == '__main__':
    p = Partie()
    p.partie()

# A conserver au cas où, pour plus tard :

# def prendre_cartes_Destination(self):
#     """
#     3. Prendre des cartes Destination supplémentaires :
#     – Le joueur prend 3 cartes Destination du dessus de la pioche. Il doit en conserver au moins une,
#     mais peut aussi garder 2 ou 3 cartes. Chaque carte qui n’est pas conservée est posée face cachée sous la pioche
#     des cartes Destination.
#     :return:
#     """
#
# """Indication Prendre des cartes Destination Un joueur peut utiliser son tour de jeu pour récupérer des cartes
# Destination supplémentaires. Pour cela, il doit prendre 3 cartes sur le dessus de la pile des cartes Destination.
# Il doit conserver au moins l’une des trois cartes, mais peut bien sûr en garder 2 ou même 3. S’il reste moins de 3
# cartes Destination dans la pile, le joueur ne peut prendre que le nombre de cartes disponibles. Chaque carte qui
# n’est pas conservée par le joueur est remise face cachée sous la pile. Chaque carte Destination fait référence à
# deux villes de la carte et un nombre de points y est associé. Si le joueur réalise la connexion entre les deux
# villes d’une carte Destination, il remporte le nombre de points indiqué sur la carte et l’additionne,
# en fin de partie, aux points déjà acquis. La route reliant ces deux villes doit être formée uniquement par les
# trains de ce joueur. Si la connexion n’est pas réalisée, le joueur déduit de son nombre de points déjà acquis le
# nombre indiqué sur la carte. Les cartes Destination sont gardées secrètes tout au long de la partie. Elles sont
# rendues publiques à la fin de la partie et chaque joueur calcule son score. Au cours du jeu, un joueur peut avoir
# autant de cartes Destination qu’il le souhaite. """
#
#     print("Je prends une carte Destination")
#     print("A implémenter")
#     return None
