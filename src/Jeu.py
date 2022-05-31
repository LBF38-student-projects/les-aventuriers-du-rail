"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

import matplotlib.pyplot as plt


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
            # Penser à mettre les nombres de segments par lien.
            # "test":{
            #     "nom":["cou",5],
            # }
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
        # plateau = plt.figure()
        fig, ax = plt.subplots()
        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        im = plt.imread("img/carte_usa.jpg")

        """Affichage des liens entre les villes :"""
        for ville in self.liens_villes.keys():
            x_ville, y_ville = self.villes[ville]
            for ville2 in self.liens_villes[ville].keys():
                nom_lien, couleur_lien = ville2, self.liens_villes[ville][ville2][0]
                x_liens, y_liens = self.villes[nom_lien]
                rx=603/36
                ry=380/23
                plt.plot((x_ville*rx, x_liens*rx), (y_ville*ry, y_liens*ry), color=couleur_lien,linewidth=5)
                # Pour les lignes en tirets : linestyle="dashed"
        """Affichage des points + noms des villes :"""
        for ville in self.villes.keys():
            x, y = self.villes[ville]
            rx=603/36
            ry=380/23
            plt.plot(x*rx, y*ry, 'ro')
            plt.text((x - 1)*rx, (y - 1)*ry, ville)
        """Arrière-plan du plateau :"""
        # ax = plt.axes()
        # ax.set_facecolor('lightgrey')
        # ax.imshow(im, extent=[1,36,1,22.7])
        ax.imshow(im, extent=[0,603,0,380])
        plt.axis(False)

        # im = ax.imshow(im)
        # format image: 603x380
        # Grille pour les points du graphe: 36x22.5
        # Rapport : 1.6
        plt.show()
        # return plateau

    def melange_cartes(self, cartes):
        """
        Mélange des cartes.
        Renvoie un paquet totalement mélangé aléatoirement.
        :param cartes:
        :return:
        """
        return "A implémenter"

    def capture_route(self):
        """
        Capture la route si le joueur a suffisamment de cartes wagon selon la couleur de la route.
        :return:
        """
        return "A implémenter"


if __name__ == '__main__':
    jeu = Jeu()
    jeu.plateau()
