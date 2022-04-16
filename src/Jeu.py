"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""


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
            "LA to NYC": 21,
            "Duluth to Houston": 8,
            "Sault Ste Marie to Nashville": 8,
            "NYC to Atlanta": 6,
            "Portland to Nashville": 17,
            "Vancouver to Montréal": 20,
            "Duluth to El Paso": 10,
            "Toronto to Miami": 10,
            "Portland to Phoenix": 11,
            "Dallas to NYC": 11,
            "Calgary to Salt Lake City": 7,
            "Calgary to Phoenix": 13,
            "LA to Miami": 20,
            "Winnipeg to Little Rock": 11,
            "San Francisco to Atlanta": 17,
            "Kansas City to Houston": 5,
            "LA to Chicago": 16,
            "Denver to Pittsburgh": 11,
            "Chicago to Santa Fe": 9,
            "Vancouver to Santa Fe": 13,
            "Boston to Miami": 12,
            "Chicago to New Orleans": 7,
            "Montreal to Atlanta": 9,
            "Seattle to NYC": 22,
            "Denver to El Paso": 4,
            "Helena to LA": 8,
            "Winnipeg to Houston": 12,
            "Montreal to New Orleans": 13,
            "Sault Ste Marie to Oklahoma City": 9,
            "Seattle to Los Angeles": 9
        }
        self.villes={
            "Los Angeles":(5,3),
            "San Francisco":(3,5),
            "Portland":(4,8),
            "Seatle":(4.5,9),
            "Vancouver":(4.5,10),
            "Calcary":(7.5,10),
            "Helena":(10,12),
            "Salt Lake City":(9,12),
            "Las Vegas":(12,5),
            "Phoenix":(14,12),
            "El Paso":(10,3),
            "Santa Fe":(25,15),
            "Denver":(9,17),
            "Oklahoma City":(23,20),
            "Kansas City":(12,23),
            "Omaha":(16,15),
            "Duluth":(13,5),
            "Winnipeg":(6,14),
            "Dallas":(8,20),
            "Houston":(22,10),
            "New Orleans":(12,26),
            "Little Rock":(24,13),
            "Saint Louis":(17,2),
            "Chicago":(5,23),
            "Nashville":(8,14),
            "Atlanta":(6,13),
            "Miami":(16,24),
            "Charleston":(21,12),
            "Pittsburg":(13,23),
            "Toronto":(9,19),
            "Montreal":(22,17),
            "Boston":(7,15),
            "New York":(16,13),
            "Washington":(12,20),
            "Raleigh":(21,19)
        }

    def plateau(self):
        """Définit le plateau du jeu
        => Construit le graphe des villes
        Affiche un point pour chaque ville avec le nom en dessous
        Relie chaque ville par un trait gris quand non occupé
        """



        # A compléter
