# -*- coding: utf-8 -*-
"""
Created on Sat May  29 12:00:26 2022
Modified on Sun May 30 03:22:00 2022

@author: Mathis URIEN
"""
import os
import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from menu_principal import *
from Joueur import *
from Partie import Partie_qt
import numpy as np


# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre
# créée avec QT Designer. Nous configurons après l'interface utilisateur
# dans le constructeur (la méthode init()) de notre classe

class MonAppli(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.les_wagons = [self.ui.wagon1, self.ui.wagon2, self.ui.wagon3, self.ui.wagon4, self.ui.wagon5]
        self.les_destinations = [self.ui.destination_1, self.ui.destination_2, self.ui.destination_3]
        self.autres_joueurs = [self.ui.autre_j1, self.ui.autre_j2, self.ui.autre_j3, self.ui.autre_j4]
        self.img_destinations = {
            "dos": "img/dos_destination.jpg",
            'Los Angeles to New York': 'img/los_angeles_new_york.jpg',
            'Duluth to Houston': 'img/duluth_houston.jpg',
            'Sault Ste Marie to Nashville': 'img/sault_ste_marie_nashville.jpg',
            'New York to Atlanta': 'img/new_york_atlanta.jpg',
            'Portland to Nashville': 'img/portland_nashville.jpg',
            'Vancouver to Montreal': 'img/vancouver_montreal.jpg',
            'Duluth to El Paso': 'img/duluth_el_paso.jpg',
            'Toronto to Miami': 'img/toronto_miami.jpg',
            'Portland to Phoenix': 'img/portland_phoenix.jpg',
            'Dallas to New York': 'img/dallas_new_york.jpg',
            'Calgary to Salt Lake City': 'img/calgary_salt_lake_city.jpg',
            'Calgary to Phoenix': 'img/calgary_phoenix.jpg',
            'Los Angeles to Miami': 'img/los_angeles_miami.jpg',
            'Winnipeg to Little Rock': 'img/winnipeg_little_rock.jpg',
            'San Francisco to Atlanta': 'img/san_francisco_atlanta.jpg',
            'Kansas City to Houston': 'img/kansas_city_houston.jpg',
            'Los Angeles to Chicago': 'img/los_angeles_chicago.jpg',
            'Denver to Pittsburgh': 'img/denver_pittsburgh.jpg',
            'Chicago to Santa Fe': 'img/chicago_santa_fe.jpg',
            'Vancouver to Santa Fe': 'img/vancouver_santa_fe.jpg',
            'Boston to Miami': 'img/boston_miami.jpg',
            'Chicago to New Orleans': 'img/chicago_new_orleans.jpg',
            'Montreal to Atlanta': 'img/montreal_atlanta.jpg',
            'Seattle to New York': 'img/seattle_new_york.jpg',
            'Denver to El Paso': 'img/denver_el_paso.jpg',
            'Helena to Los Angeles': 'img/helena_los_angeles.jpg',
            'Winnipeg to Houston': 'img/winnipeg_houston.jpg',
            'Montreal to New Orleans': 'img/montreal_new_orleans.jpg',
            'Sault Ste Marie to Oklahoma City': 'img/sault_ste_marie_oklahoma_city.jpg',
            'Seattle to Los Angeles': 'img/seattle_los_angeles.jpg'
        }
        self.img_wagons = {
            "dos": "img/dos_wagon.jpg",
            "blanc": "img/wagon_blanc.jpg",
            "bleu": "img/wagon_bleu.jpg",
            "jaune": "img/wagon_jaune.jpg",
            "noir": "img/wagon_noir.jpg",
            "orange": "img/wagon_orange.jpg",
            "rose": "img/wagon_rose.jpg",
            "rouge": "img/wagon_rouge.jpg",
            "vert": "img/wagon_vert.jpg",
            "locomotive": "img/locomotive.jpg"
        }
        "Navigations entre les pages"
        # Buttons de l'écran Menu Principal
        self.ui.button_nouvelle_partie.clicked.connect(self.commencer_partie)
        self.ui.button_regles_jeu.clicked.connect(lambda: self.ouvrir_regles())
        self.ui.button_options.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Options))
        self.ui.button_credits.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Credits))
        # Buttons de l'écran Nouvelle Partie
        self.ui.button_commencer.clicked.connect(self.start_game)
        self.ui.button_retour.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Menu_principal))
        # Buttons de l'écran Joueur
        # Création des boutons pour la fin de partie et la fin de tour.
        # => utile pour la fin de tour et la fin de partie.
        self.create_button_fin_partie()
        self.create_button_fin_tour()
        self.create_label_nb_wagons(5)
        self.ui.button_fin_tour.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Joueur))
        # Connexion du button fin_partie avec écran Fin de partie
        self.ui.button_fin_partie.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Fin_partie))
        # Buttons de l'écran Fin de Partie
        self.ui.button_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Menu_principal))
        self.ui.button_nouvelle_partie_3.clicked.connect(lambda: self.commencer_partie())
        self.ui.button_statistiques.clicked.connect(lambda: self.show_stats())
        # Buttons de l'écran Options
        self.ui.button_credits_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Credits))
        self.ui.button_nouvelle_partie_4.clicked.connect(lambda: self.commencer_partie())
        self.ui.button_retour_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Menu_principal))
        # Buttons de l'écran Crédits
        self.ui.button_retour_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Menu_principal))

        # Making QLabels clickable
        # QLabels = [self.ui.wagon1, self.ui.wagon2, self.ui.wagon3, self.ui.wagon4, self.ui.wagon5, self.ui.pioche_wagon,
        #            self.ui.destination_1, self.ui.destination_2, self.ui.destination_3, self.ui.pioche_destination]
        # for label in QLabels:
        #     label.mouseReleaseEvent = self.print_value
        self.ui.wagon1.mouseReleaseEvent = self.prendre_wagon1
        self.ui.wagon2.mouseReleaseEvent = self.prendre_wagon2
        self.ui.wagon3.mouseReleaseEvent = self.prendre_wagon3
        self.ui.wagon4.mouseReleaseEvent = self.prendre_wagon4
        self.ui.wagon5.mouseReleaseEvent = self.prendre_wagon5
        self.ui.pioche_wagon.mouseReleaseEvent = self.prendre_pioche_wagon

    def prendre_wagon1(self,event):
        self.partie.pile_cartes_wagon.pop(0)
        self.update_wagon_stack()

    def prendre_wagon2(self, event):
        self.partie.pile_cartes_wagon.pop(1)
        self.update_wagon_stack()

    def prendre_wagon3(self,event):
        self.partie.pile_cartes_wagon.pop(2)
        self.update_wagon_stack()

    def prendre_wagon4(self,event):
        self.partie.pile_cartes_wagon.pop(3)
        self.update_wagon_stack()

    def prendre_wagon5(self,event):
        self.partie.pile_cartes_wagon.pop(4)
        self.update_wagon_stack()

    def prendre_pioche_wagon(self,event):
        self.partie.pile_cartes_wagon.pop(5)
        self.update_wagon_stack()

    def print_value(self, event):
        print(f"clicked: {event}")

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        print(event.pos())
        if self.ui.wagon1.mousePressEvent(event):
            print("Wagon 1 clicked")

    def commencer_partie(self):
        print("On commence une nouvelle partie !")
        # On cache tous les inputs avant de connaître le nb de joueurs de la partie.
        self.show_inputs()

        # On update les choix pour les niveaux d'IAs. Au cas où il y ait eu une évolution dans les niveaux possibles.
        self.update_IA_difficulties()

        # Tant que les inputs ne sont pas remplis, on cache le bouton et la question pour l'ordre.
        self.ui.label_voyageur.hide()
        self.ui.selection_voyageur.hide()
        self.ui.button_commencer.hide()

        # Affichage de l'écran Nouvelle Partie.
        self.ui.stackedWidget.setCurrentWidget(self.ui.Nouvelle_partie)

        # On initialise une nouvelle partie :
        self.partie = Partie_qt()

        # liste des joueurs de la partie.
        # Format : [[nom_j1,couleur_j1, IA],...,[nom_jn,couleur_jn,IA]]
        # IA: False si Joueur IRL, sinon contient Difficulté IA.
        self.init_les_joueurs()

        # Pour définir l'ordre de passage des joueurs.
        self.joueur_le_plus_voyageur: str = ""

        # Récupération des nbs de joueurs IRLs/IAs
        self.ui.spinbox_nb_joueurs_tot.valueChanged.connect(lambda: self.show_inputs())
        self.ui.spinbox_nb_joueurs_ia.valueChanged.connect(lambda: self.show_inputs())

        # Récupération des infos pour chaque joueur
        # J1
        self.ui.input_nom1.editingFinished.connect(
            lambda: self.get_player_inputs(0, self.ui.input_nom1, self.ui.input_couleur1))
        self.ui.input_couleur1.currentIndexChanged.connect(
            lambda: self.get_player_inputs(0, self.ui.input_nom1, self.ui.input_couleur1))
        # J2
        self.ui.input_nom2.editingFinished.connect(
            lambda: self.get_player_inputs(1, self.ui.input_nom2, self.ui.input_couleur2))
        self.ui.input_couleur2.currentIndexChanged.connect(
            lambda: self.get_player_inputs(1, self.ui.input_nom2, self.ui.input_couleur2))
        # J3
        self.ui.input_nom3.editingFinished.connect(
            lambda: self.get_player_inputs(2, self.ui.input_nom3, self.ui.input_couleur3))
        self.ui.input_couleur3.currentIndexChanged.connect(
            lambda: self.get_player_inputs(2, self.ui.input_nom3, self.ui.input_couleur3))
        # J4
        self.ui.input_nom4.editingFinished.connect(
            lambda: self.get_player_inputs(3, self.ui.input_nom4, self.ui.input_couleur4))
        self.ui.input_couleur4.currentIndexChanged.connect(
            lambda: self.get_player_inputs(3, self.ui.input_nom4, self.ui.input_couleur4))
        # J5
        self.ui.input_nom5.editingFinished.connect(
            lambda: self.get_player_inputs(4, self.ui.input_nom5, self.ui.input_couleur5))
        self.ui.input_couleur5.currentIndexChanged.connect(
            lambda: self.get_player_inputs(4, self.ui.input_nom5, self.ui.input_couleur5))

        # Pour les IAs:
        self.ui.choix_IA1.currentIndexChanged.connect(
            lambda: self.get_IA_inputs(0, self.ui.input_nom1, self.ui.input_couleur1, self.ui.choix_IA1))
        self.ui.choix_IA2.currentIndexChanged.connect(
            lambda: self.get_IA_inputs(1, self.ui.input_nom2, self.ui.input_couleur2, self.ui.choix_IA2))
        self.ui.choix_IA3.currentIndexChanged.connect(
            lambda: self.get_IA_inputs(2, self.ui.input_nom3, self.ui.input_couleur3, self.ui.choix_IA3))
        self.ui.choix_IA4.currentIndexChanged.connect(
            lambda: self.get_IA_inputs(3, self.ui.input_nom4, self.ui.input_couleur4, self.ui.choix_IA4))
        self.ui.choix_IA5.currentIndexChanged.connect(
            lambda: self.get_IA_inputs(4, self.ui.input_nom5, self.ui.input_couleur5, self.ui.choix_IA5))

        # Récupération du choix du premier joueur. (le plus voyageur)
        self.choose_first_player()

    def update_IA_difficulties(self):
        """
        Update all IA difficulties combo boxes according to the IA player's levels dictionnary.
        """
        self.IA_difficulties = [self.ui.choix_IA1, self.ui.choix_IA2, self.ui.choix_IA3, self.ui.choix_IA4,
                                self.ui.choix_IA5]
        levels = list(IA_player().levels.keys())
        for choix in self.IA_difficulties:
            for k in range(4):
                choix.setItemText(k, levels[k])

    def choose_first_player(self):
        """
        Permet le choix du premier joueur.
        """
        self.update_selection_voyageur()
        self.ui.selection_voyageur.currentIndexChanged.connect(lambda: self.get_first_player())

    def show_selection_voyageur(self):
        """
        Show the label and its combo box
        """
        self.ui.label_voyageur.show()
        self.ui.selection_voyageur.show()

    def update_selection_voyageur(self):
        for index, joueur in enumerate(self.les_joueurs[:self.nb_joueurs_tot]):
            self.ui.selection_voyageur.setItemText(index + 1, joueur[0])

    def get_first_player(self):
        """
        Récupère le nom du premier joueur.
        """
        self.joueur_le_plus_voyageur = self.ui.selection_voyageur.currentText()
        if self.joueur_le_plus_voyageur:
            self.ui.button_commencer.show()
        else:
            self.ui.button_commencer.hide()

    def get_player_inputs(self, index, input_nom, input_couleur):
        """
        Récupère les données des joueurs pour la partie.
        """
        nom = input_nom.text()
        couleur = input_couleur.currentText()
        self.les_joueurs[index] = [nom, couleur, False]
        self.update_selection_voyageur()
        self.show_selection_voyageur()

    def get_IA_inputs(self, index, input_nom, input_couleur, input_level):
        """
        Récupère le niveau d'un IA si celui-ci est modifié.
        """
        nom = input_nom.text()
        couleur = input_couleur.currentText()
        level = input_level.currentText()
        self.les_joueurs[index] = [nom, couleur, level]
        self.update_selection_voyageur()
        self.show_selection_voyageur()

    def init_les_joueurs(self):
        """
        Initialise/Réinitialise la variable d'instance les_joueurs
        """
        self.les_joueurs = [[f"Joueur IA n°{k + 1}", "random", False] for k in
                            range(5)]

    def hide_inputs(self):
        """
        Hide the inputs defined for the new game.
        """
        self.inputs = [[self.ui.label_nom1, self.ui.input_nom1, self.ui.label_couleur1, self.ui.input_couleur1,
                        self.ui.separation1, self.ui.label_difficulty1, self.ui.choix_IA1],
                       [self.ui.label_nom2, self.ui.input_nom2, self.ui.label_couleur2, self.ui.input_couleur2,
                        self.ui.separation2, self.ui.label_difficulty2, self.ui.choix_IA2],
                       [self.ui.label_nom3, self.ui.input_nom3, self.ui.label_couleur3, self.ui.input_couleur3,
                        self.ui.separation3, self.ui.label_difficulty3, self.ui.choix_IA3],
                       [self.ui.label_nom4, self.ui.input_nom4, self.ui.label_couleur4, self.ui.input_couleur4,
                        self.ui.separation4, self.ui.label_difficulty4, self.ui.choix_IA4],
                       [self.ui.label_nom5, self.ui.input_nom5, self.ui.label_couleur5, self.ui.input_couleur5,
                        self.ui.separation5, self.ui.label_difficulty5, self.ui.choix_IA5]]
        for INPUT in self.inputs:
            for elt in INPUT:
                elt.hide()
        # On réinitialise les joueurs car ne sont plus affichés.
        self.init_les_joueurs()

    def show_inputs(self):
        self.hide_inputs()
        self.nb_joueurs_tot = self.ui.spinbox_nb_joueurs_tot.value()
        nb_joueurs_ia = self.ui.spinbox_nb_joueurs_ia.value()
        # Affichage des inputs en fonction des joueurs IRL/IAs:
        for k, INPUT in enumerate(self.inputs[:self.nb_joueurs_tot - nb_joueurs_ia]):  # joueurs IRLs
            for i, elt in enumerate(INPUT[:-2]):
                elt.show()
                if i == 1:
                    elt.clear()
                    elt.setDisabled(elt.isReadOnly())
                if i == 3:
                    elt.setCurrentIndex(k)
            INPUT[-1].hide()
            INPUT[-2].hide()
        for k, INPUT in enumerate(self.inputs[self.nb_joueurs_tot - nb_joueurs_ia:self.nb_joueurs_tot]):  # joueurs IAs
            for elt in INPUT:
                elt.show()
                if INPUT.index(elt) == 1:
                    elt.setText(f"Joueur IA n°{k + 1 + self.nb_joueurs_tot - nb_joueurs_ia}")
                    elt.setEnabled(elt.isReadOnly())
                if INPUT.index(elt) == 3:
                    elt.setCurrentIndex(elt.findText("random"))
            self.get_IA_inputs(k, INPUT[1], INPUT[3], INPUT[-1])
        self.ui.stackedWidget.setCurrentWidget(self.ui.Nouvelle_partie)

    def update_main_joueur(self, joueur):
        """
        Update the current player's wagons cards display.
        """
        pass

    def update_main_destination(self, joueur):
        """
        Update the current player's destination cards display.
        """
        self.hide_destinations()
        for d, destination in enumerate(self.les_destinations):
            destination_path = self.img_destinations[joueur.main_destination[d]]
            destination.setPixmap(QtGui.QPixmap(destination_path))
            destination.show()

    def hide_destinations(self):
        """
        Hide all destinations cards
        """
        for destination in self.les_destinations:
            destination.hide()

    def update_wagon_stack(self):
        """
        Update the wagon stack. Shuffle the deck if necessary.
        """
        self.hide_wagons()
        self.partie.update_wagons_stack() # On vérifie pour les locomotives et refait la pile si tout dans la défausse.
        for w, wagon in enumerate(self.les_wagons):
            if self.partie.pile_cartes_wagon and w<len(self.partie.pile_cartes_wagon):
                wagon_path = self.img_wagons[self.partie.pile_cartes_wagon[w]]
                wagon.setPixmap(QtGui.QPixmap(wagon_path))
                wagon.show()
            else:
                wagon.hide()

    def hide_wagons(self):
        """
        Hide all wagons cards
        """
        for wagon in self.les_wagons:
            wagon.hide()

    def hide_autres_joueurs(self):
        """
        Hide the others players.
        """
        for autre in self.autres_joueurs:
            autre.hide()

    def update_autres_joueurs(self, joueur):
        """
        Update the display of other players' scores.
        """
        self.hide_autres_joueurs()
        other_players = self.partie.ordre.copy()
        other_players.pop(other_players.index(joueur.nom_joueur))
        for p, player in enumerate(other_players):
            player = self.partie.les_joueurs[player]
            plain_text = f"{player.nom_joueur}: {player.nb_points}"
            self.autres_joueurs[p].setText(plain_text)
            self.autres_joueurs[p].show()

    def create_label_nb_wagons(self,nb_wagons):
        self.ui.main_nb_wagon1 = QtWidgets.QLabel(self.ui.Joueur)
        self.ui.main_nb_wagon1.setMinimumSize(QtCore.QSize(100, 64))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ui.main_nb_wagon1.setFont(font)
        self.ui.main_nb_wagon1.setText(f"{nb_wagons}")
        self.ui.main_nb_wagon1.setObjectName("main_nb_wagon1")
        self.ui.main_nb_wagon1.move(QtCore.QPoint(self.ui.main_wagon1.width(),self.ui.main_wagon1.height()))
        # FIXME: bien positionner le label

    def create_button_fin_tour(self):
        """
        Création du bouton fin de tour pour que le joueur puisse déclarer qu'il a fini son tour.
        """
        # Button fin de tour
        self.ui.button_fin_tour = QtWidgets.QPushButton(self.ui.Joueur)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.button_fin_tour.sizePolicy().hasHeightForWidth())
        self.ui.button_fin_tour.setSizePolicy(sizePolicy)
        self.ui.button_fin_tour.setMinimumSize(QtCore.QSize(0, 0))
        self.ui.button_fin_tour.setObjectName("button_fin_tour")
        _translate = QtCore.QCoreApplication.translate
        self.ui.button_fin_tour.setText(_translate("MainWindow", "Fin de tour"))
        self.ui.button_fin_tour.move(QtCore.QPoint(self.x()+500,self.y()))
        print(f"button fin tour: {self.x()+20,self.y(),self.size().height()}")

    def create_button_fin_partie(self):
        """
        Creation d'un bouton pour la fin de partie quand la partie est terminée. Permet d'accéder à l'écran de fin de partie.
        """
        # Button fin de partie
        self.ui.button_fin_partie = QtWidgets.QPushButton(self.ui.Joueur)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.button_fin_partie.sizePolicy().hasHeightForWidth())
        self.ui.button_fin_partie.setSizePolicy(sizePolicy)
        self.ui.button_fin_partie.setMinimumSize(QtCore.QSize(0, 0))
        self.ui.button_fin_partie.setObjectName("button_fin_partie")
        _translate = QtCore.QCoreApplication.translate
        self.ui.button_fin_partie.setText(_translate("MainWindow", "Fin de partie"))

    def tour_joueur(self, joueur):
        """
        Une fois la partie prête, la partie est lancée via la méthode partie(ihm_partie) de la classe Partie() dans le module Partie.py
        Puis, les tours s'enchaînent jusqu'à la fin de la partie. => cf. dans la méthode partie()
        """
        # On initialise/réinitialise les variables pour l'affichage du joueur actuel.
        self.ui.titre_nom_joueur.setText(joueur.nom_joueur)
        self.ui.score_joueur.setText(str(joueur.nb_points))
        self.update_main_joueur(joueur)
        self.update_main_destination(joueur)
        self.update_wagon_stack()
        self.update_autres_joueurs(joueur)

        # On cache et remplace les interactions avec le joueur par les buttons fin_tour ou fin_partie
        # si le tour ou la partie est fini.
        # self.ui.input_interaction.hide()
        # self.ui.label_interaction_joueur.hide()
        # self.ui.gridLayout_19.addWidget(self.ui.button_fin_partie, 7, 0, 1, 1)
        # self.ui.button_fin_partie.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Fin_partie))

        # Change d'affichage pour l'écran Joueur
        self.ui.stackedWidget.setCurrentWidget(self.ui.Joueur)

    def check_fin_tour(self):
        """
        Return if fin_tour : bool
        """
        return not self.fin_tour

    def start_game(self):
        """
        fait tourner une partie complète du jeu. du début à la fin.
        """
        print("Préparation de la partie")
        self.partie.debut_partie(self)
        self.partie.preparation_partie()
        self.partie.choix_tour_joueur(self)
        #
        # Main boucle for the game
        i = 0
        nom = self.partie.ordre[i]
        joueur = self.partie.les_joueurs[nom]
        print(joueur)
        # print("premier tour test")
        # # self.partie.tour(joueur,self)
        self.tour_joueur(joueur)
        # print("fin premier tour test")
        # self.ui.stackedWidget.setCurrentWidget(self.ui.Joueur)
        # fin_tour = False
        # while joueur.wagons > 2:
        #     if not fin_tour:
        #         print(f"Tour du joueur n°{i}")
        #         fin_tour = self.partie.tour(joueur, self)
        #         # time.sleep(10)
        #     else:
        #         if i == len(self.partie.ordre) - 1:
        #             i = 0
        #         else:
        #             i += 1
        #         nom = self.partie.ordre[i]
        #         joueur = self.partie.les_joueurs[nom]
        #         fin_tour = False
        # self.partie.rotation_joueur(i)
        # print("Dernier tour")
        # for nom in self.partie.ordre:
        #     fin_tour=self.partie.tour(self.partie.les_joueurs[nom], self)
        # self.ui.stackedWidget.setCurrentWidget(self.ui.Fin_partie)
        # print("Fin de partie\nAffichage du score bientôt disponible")

    def ouvrir_regles(self):
        """
        Ouvre les règles.
        Voir si cela présente des erreurs sur d'autres ordis
        """
        return os.startfile(os.path.abspath("../docs/règles les aventuriers du rail.pdf"))

    def show_stats(self):
        """
        Montre les stats des joueurs pr chaque joueur:
        - cartes destinations réussies/échouées
        - routes prises et pts associés
        - nb cartes wagons à la fin.
        """
        print("Cette fonctionnalité arrive bientôt !")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
