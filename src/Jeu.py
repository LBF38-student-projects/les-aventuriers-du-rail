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
            "Los Angeles": [["San Francisco", "yellow"],
                            ["Las Vegas", "grey"],
                            ["Phoenix", "grey"],
                            ["El Paso", "black"]],
            "San Francisco": [["Portland", "orange"],
                              ["Salt Lake City", "orange"],
                              ["Los Angeles", "grey"]],
            "Portland": [["Seattle", "grey"],
                         ["Salt Lake City", "blue"],
                         ["San Francisco", "orange"]],
            "Seattle": [["Portland", "grey"],
                        ["Helena", "yellow"],
                        ["Vancouver", "grey"],
                        ["Calgary", "grey"]],
            "Vancouver": [["Seattle", "grey"],
                          ["Calgary", "grey"]],
            "Calgary": [["Winnipeg", "white"],
                        ["Helena", "grey"],
                        ["Seattle", "grey"],
                        ["Vancouver", "grey"]],
            "Helena": [["Seattle", "yellow"],
                       ["Calgary", "grey"],
                       ["Winnipeg", "blue"],
                       ["Duluth", "orange"],
                       ["Omaha", "red"],
                       ["Denver", "orange"],
                       ["Salt Lake City", "grey"]],
            "Salt Lake City": [["Portland", "blue"],
                               ["San Francisco", "orange"],
                               ["Las Vegas", "orange"],
                               ["Denver", "yellow"],
                               ["Helena", "grey"]],
            "Las Vegas": [["Salt Lake City", "orange"],
                          ["Los Angeles", "grey"]],
            "Phoenix": [["El Paso", "grey"],
                        ["Santa Fe", "grey"],
                        ["Los Angeles", "grey"],
                        ["Denver", "white"]],
            "El Paso": [["Santa Fe", "grey"],
                        ["Phoenix", "grey"],
                        ["Los Angeles", "black"],
                        ["Houston", "orange"],
                        ["Dallas", "red"],
                        ["Oklahoma City", "yellow"]],
            "Santa Fe": [["Phoenix", "grey"],
                         ["Denver", "grey"],
                         ["Oklahoma City", "blue"],
                         ["El Paso", "grey"]],
            "Denver": [["Santa Fe", "grey"],
                       ["Phoenix", "white"],
                       ["Salt Lake City", "yellow"],
                       ["Helena", "orange"],
                       ["Omaha", "grey"],
                       ["Kansas City", "black"],
                       ["Oklahoma City", "red"]],
            "Oklahoma City": [["Denver", "red"],
                              ["Kansas City", "grey"],
                              ["Santa Fe", "blue"],
                              ["El Paso", "yellow"],
                              ["Dallas", "grey"],
                              ["Little Rock", "grey"]],
            "Kansas City": [["Denver", "orange"],
                            ["Omaha", "grey"],
                            ["Saint Louis", "grey"],
                            ["Oklahoma City", "grey"]],
            "Omaha": [["Denver", "grey"],
                      ["Kansas City", "grey"],
                      ["Chicago", "blue"],
                      ["Duluth", "grey"],
                      ["Helena", "yellow"]],
            "Duluth": [["Winnipeg", "white"],
                       ["Helena", "orange"],
                       ["Sault Ste Marie", "grey"],
                       ["Toronto", "grey"],
                       ["Chicago", "red"],
                       ["Omaha", "grey"]],
            "Sault Ste Marie": [["Winnipeg", "grey"],
                                ["Duluth", "grey"],
                                ["Toronto", "grey"],
                                ["Montreal", "black"]],
            "Winnipeg": [["Calgary", "white"],
                         ["Helena", "blue"],
                         ["Duluth", "black"],
                         ["Sault Ste Marie", "grey"]],
            "Dallas": [["Houston", "grey"],
                       ["El Paso", "red"],
                       ["Oklahoma City", "grey"],
                       ["Little Rock", "grey"]],
            "Houston": [["Dallas", "grey"],
                        ["El Paso", "orange"],
                        ["New Orleans", "grey"]],
            "New Orleans": [["Houston", "grey"],
                            ["Little Rock", "orange"],
                            ["Atlanta", "yellow"],
                            ["Miami", "red"]],
            "Little Rock": [["New Orleans", "orange"],
                            ["Dallas", "grey"],
                            ["Oklahoma City", "grey"],
                            ["Saint Louis", "grey"],
                            ["Nashville", "white"]],
            "Saint Louis": [["Little Rock", "grey"],
                            ["Kansas City", "grey"],
                            ["Chicago", "white"],
                            ["Pittsburgh", "orange"],
                            ["Nashville", "grey"]],
            "Chicago": [["Saint Louis", "white"],
                        ["Omaha", "blue"],
                        ["Duluth", "red"],
                        ["Toronto", "white"],
                        ["Pittsburgh", "orange"]],
            "Nashville": [["Saint Louis", "grey"],
                          ["Pittsburgh", "yellow"],
                          ["Little Rock", "white"],
                          ["Atlanta", "grey"],
                          ["Raleigh", "black"]],
            "Atlanta": [["Nashville", "grey"],
                        ["Raleigh", "grey"],
                        ["Charleston", "grey"],
                        ["New Orleans", "yellow"],
                        ["Miami", "blue"]],
            "Miami": [["New Orleans", "red"],
                      ["Atlanta", "blue"],
                      ["Charleston", "grey"]],
            "Charleston": [["Miami", "grey"],
                           ["Atlanta", "grey"],
                           ["Raleigh", "grey"]],
            "Pittsburgh": [["Washington", "grey"],
                           ["Raleigh", "grey"],
                           ["Nashville", "yellow"],
                           ["Saint Louis", "orange"],
                           ["Chicago", "black"],
                           ["Toronto", "grey"],
                           ["New York", "orange"]],
            "Toronto": [["Pittsburgh", "grey"],
                        ["Chicago", "white"],
                        ["Duluth", "grey"],
                        ["Sault Ste Marie", "grey"],
                        ["Montreal", "grey"]],
            "Montreal": [["Boston", "grey"],
                         ["New York", "blue"],
                         ["Toronto", "grey"],
                         ["Sault Ste Marie", "black"]],
            "Boston": [["Montreal", "grey"],
                       ["New York", "yellow"]],
            "New York": [["Boston", "yellow"],
                         ["Montreal", "blue"],
                         ["Pittsburgh", "orange"],
                         ["Washington", "black"]],
            "Washington": [["New York", "black"],
                           ["Pittsburgh", "grey"],
                           ["Raleigh", "grey"]],
            "Raleigh": [["Washington", "grey"],
                        ["Pittsburgh", "grey"],
                        ["Nashville", "black"],
                        ["Atlanta", "grey"],
                        ["Charleston", "grey"]],
        }

    def plateau(self):
        """Définit le plateau du jeu
        => Construit le graphe des villes
        Affiche un point pour chaque ville avec le nom en dessous
        Relie chaque ville par un trait gris quand non occupé
        """
        plateau = plt.figure()

        for keys in self.villes.keys():
            x, y = self.villes[keys]
            """Affichage des points + noms des villes :"""
            plt.plot(x, y, 'ro')
            plt.text(x - 1, y - 1, keys)
        """Affichage des liens entre les villes :"""
        for keys in self.liens_villes.keys():
            x_ville, y_ville = self.villes[keys]
            for liste in self.liens_villes[keys]:
                nom_lien, couleur_lien = liste
                x_liens, y_liens = self.villes[nom_lien]
                plt.plot((x_ville, x_liens), (y_ville, y_liens), couleur_lien, linewidth=5)
        return plateau

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
    # """
    # Couleurs :
    # yellow: y
    # green: g
    # blue: b
    # black: k
    # white: w ?
    # grey: grey
    # """
    # plt.plot((1,2),(3,5),'orange')
    # plt.show()
    # dico={
    #     "test":{
    #         "test2":2,
    #         "autre":5
    #     }
    #     "autre key":10,
    #     "finalement":5
    # }
