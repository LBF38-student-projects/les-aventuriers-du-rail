# -*- coding: utf-8 -*-
"""
Created on Sat May  29 12:00:26 2022
Modified on Sun May 30 03:22:00 2022

@author: Mathis URIEN
"""
import os
from PySide2.QtGui import (QMouseEvent)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from Joueur import *
from Partie import Partie_qt
from ui_choix_route import *
from ui_menu_principal import *


# import numpy as np


# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre
# créée avec QT Designer. Nous configurons après l'interface utilisateur
# dans le constructeur (la méthode init()) de notre classe

# DONE: maj de menu_principal.py en fonction des nouvelles modifs du fichier éponyme du dossier Qt Designer.
#  => comparer les fichiers.

class MonAppli(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pioche_wagons = [self.ui.wagon1, self.ui.wagon2, self.ui.wagon3, self.ui.wagon4, self.ui.wagon5]
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
            "white": "img/wagon_blanc.jpg",
            "blue": "img/wagon_bleu.jpg",
            "yellow": "img/wagon_jaune.jpg",
            "black": "img/wagon_noir.jpg",
            "orange": "img/wagon_orange.jpg",
            "pink": "img/wagon_rose.jpg",
            "red": "img/wagon_rouge.jpg",
            "green": "img/wagon_vert.jpg",
            "locomotive": "img/locomotive.jpg",
            "back": "img/dos_wagon.jpg"
        }
        self.partie: Partie_qt = None

        "Navigations entre les pages"
        # Buttons de l'écran Menu Principal
        self.ui.button_nouvelle_partie.clicked.connect(self.commencer_partie)
        self.ui.button_regles_jeu.clicked.connect(lambda: self.ouvrir_regles())
        self.ui.button_options.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Options))
        self.ui.button_credits.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Credits))

        # Buttons de l'écran Nouvelle Partie
        self.ui.button_commencer.clicked.connect(lambda: self.partie.partie(self))
        self.ui.button_retour.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Menu_principal))

        # Buttons de l'écran Joueur
        # Création des boutons pour la fin de partie et la fin de tour.
        # => utile pour la fin de tour et la fin de partie.
        self.ui.button_fin_tour.clicked.connect(lambda: self.partie.change_turn(self))
        # Connexion du button fin_partie avec écran Fin de partie
        self.ui.button_fin_partie.clicked.connect(lambda: self.fin_partie())
        # Connexion pour le button take_road
        self.ui.button_take_road.clicked.connect(lambda: self.open_take_road())

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

        # Connexions de la fenêtre take_road
        self.init_take_road()

        # Pour démarrer sur l'écran Menu Principal
        self.ui.stackedWidget.setCurrentWidget(self.ui.Menu_principal)

    def init_take_road(self):
        """
        Ouvrir une nouvelle fenêtre.
        """
        self.dialog_take_road = QDialog()
        self.ui_take_road = Ui_take_road()
        self.ui_take_road.setupUi(self.dialog_take_road)
        self.dialog_take_road.setWindowIcon(self.windowIcon())

    def open_take_road(self):
        self.update_choix_route()
        self.dialog_take_road.setModal(True)
        self.dialog_take_road.show()

    def update_wagons_road(self):
        """
        Update l'affichage de la combobox pour les wagons à utiliser pour prendre la route sélectionnée.
        """
        self.ui_take_road.choose_wagons.clear()
        self.ui_take_road.choose_wagons.addItem("Choisissez le type de wagon")
        for wagon in self.partie.current_player.main_wagon:
            self.ui_take_road.choose_wagons.addItem(self.partie.traduction_color[wagon])

    def enable_prendre_wagons(self):
        """
        Autorise la possibilité de clicker sur les cartes de la pioche ou celles visibles.
        """
        self.ui.wagon1.mouseReleaseEvent = self.prendre_wagon1
        self.ui.wagon2.mouseReleaseEvent = self.prendre_wagon2
        self.ui.wagon3.mouseReleaseEvent = self.prendre_wagon3
        self.ui.wagon4.mouseReleaseEvent = self.prendre_wagon4
        self.ui.wagon5.mouseReleaseEvent = self.prendre_wagon5
        self.ui.pioche_wagon.mouseReleaseEvent = self.prendre_pioche_wagon

    def disable_prendre_wagons(self):
        """
        Autorise la possibilité de clicker sur les cartes de la pioche ou celles visibles.
        """
        self.ui.wagon1.mouseReleaseEvent = None
        self.ui.wagon2.mouseReleaseEvent = None
        self.ui.wagon3.mouseReleaseEvent = None
        self.ui.wagon4.mouseReleaseEvent = None
        self.ui.wagon5.mouseReleaseEvent = None
        self.ui.pioche_wagon.mouseReleaseEvent = None

    def prendre_destinations(self):
        """
        Pour prendre des cartes destinations.
        """
        print("Action bientôt disponible !!")
        pass

    def update_choix_route(self):
        """
        Update les possibilités de route à prendre.
        """
        self.init_take_road()
        self.hide_take_road()
        self.ui_take_road.choose_road.clear()
        self.ui_take_road.choose_road.addItem("Choisir une route parmi celles-ci")
        self.partie.les_routes.sort()  # sorting by alphabetic order
        for route in self.partie.les_routes:
            ville1, ville2 = route
            text = f"{ville1} - {ville2}"
            self.ui_take_road.choose_road.addItem(text)
        self.ui_take_road.choose_road.currentTextChanged.connect(lambda: self.changed_choose_road())

    def changed_choose_road(self):
        print("choix route")
        nom_route = self.ui_take_road.choose_road.currentText()
        print(nom_route)
        ville1, ville2 = [k.strip() for k in nom_route.strip().split("-")]
        couleur, nb_segments = self.partie.villes[ville1].liens[ville2]  # contient [couleur,nb_segments]
        # Vérification que le joueur peut prendre une route :
        self.ui_take_road.label_wagons.hide()
        self.ui_take_road.choose_wagons.hide()
        if couleur == "grey":
            self.ui_take_road.label_wagons.setText(f"La route est grise. Il y a {nb_segments} segments."
                                                   f"\nAvec quel wagon voulez-vous la prendre ?")
            self.update_wagons_road()
            self.ui_take_road.label_wagons.show()
            self.ui_take_road.choose_wagons.show()
            self.ui_take_road.choose_wagons.setEnabled(True)
            self.ui_take_road.choose_wagons.currentTextChanged.connect(lambda: self.changed_choose_wagons())
        else:
            self.ui_take_road.label_wagons.setText(f"La route est {self.partie.traduction_color[couleur]}. "
                                                   f"Il y a {nb_segments} segments.")
            self.ui_take_road.choose_wagons.clear()
            self.ui_take_road.choose_wagons.addItem(f"{self.partie.traduction_color[couleur]}")
            self.ui_take_road.choose_wagons.setEnabled(False)
            self.ui_take_road.label_wagons.show()
            self.ui_take_road.choose_wagons.show()
            self.changed_choose_wagons()

    def changed_choose_wagons(self):
        print("choix type wagons")
        self.ui_take_road.label_locomotive.hide()
        self.ui_take_road.choose_locomotive.hide()
        type_wagon = self.ui_take_road.choose_wagons.currentText()
        if type_wagon in self.partie.current_player.convert_color_id:
            type_wagon = self.partie.current_player.convert_color_id[type_wagon]
        if "locomotive" not in type_wagon and type_wagon in self.partie.current_player.main_wagon.keys():
            print(type_wagon)
            self.ui_take_road.label_locomotive.setText("Voulez-vous utiliser des wagons locomotives ?")
            self.ui_take_road.label_locomotive.show()
            self.ui_take_road.choose_locomotive.show()
            self.ui_take_road.choose_locomotive.currentTextChanged.connect(self.changed_choose_locomotive)

    def changed_choose_locomotive(self):
        print("choix locomotive")
        self.ui_take_road.label_nb_locomotive.hide()
        self.ui_take_road.spinbox_nb_locomotive.hide()
        if "Oui" in self.ui_take_road.choose_locomotive.currentText():
            self.ui_take_road.spinbox_nb_locomotive.setMaximum(self.partie.current_player.main_wagon["locomotive"])
            self.ui_take_road.label_nb_locomotive.show()
            self.ui_take_road.spinbox_nb_locomotive.show()
        self.dialog_take_road.accepted.connect(lambda: self.partie.prendre_route(self))

    def hide_take_road(self):
        """
        Cache les élts secondaires pour le choix d'une route.
        """
        to_hide = [self.ui_take_road.label_wagons, self.ui_take_road.choose_wagons,
                   self.ui_take_road.label_locomotive, self.ui_take_road.choose_locomotive,
                   self.ui_take_road.label_nb_locomotive, self.ui_take_road.spinbox_nb_locomotive]
        for h in to_hide:
            h.hide()

    def show_take_road(self):
        """
        Montre les elts pour choisir une route
        """
        to_show = [self.ui_take_road.label_wagons, self.ui_take_road.choose_wagons,
                   self.ui_take_road.label_locomotive, self.ui_take_road.choose_locomotive,
                   self.ui_take_road.label_nb_locomotive, self.ui_take_road.spinbox_nb_locomotive]
        for s in to_show:
            s.show()

    def update_route_prise(self):
        """
        Affiche le plateau et les routes.
        """
        scene = QGraphicsScene(self.ui.emplacement_carte)
        canvas = FigureCanvas(self.partie.show_route_prise())
        proxy_widget = scene.addWidget(canvas)
        self.ui.emplacement_carte.setScene(scene)
        self.ui.emplacement_carte.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.emplacement_carte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.ui.emplacement_carte.setMinimumSize(640,480)
        # self.ui.emplacement_carte.setViewportMargins(0,0,0,0)

    def prendre_wagon(self, idx, visible):
        indication_carte = self.partie.prendre_cartes_wagon(idx, visible)
        self.ui.label_interaction_joueur.setText(indication_carte)
        self.update_wagon_stack()
        self.update_main_joueur(self.partie.current_player)
        if self.partie.count_wagon_card >= 2:
            print(self.partie.count_wagon_card)
            self.fin_tour()
        elif self.partie.count_wagon_card == 1:
            self.ui.button_take_road.setEnabled(False)
            self.ui.pioche_destination.setEnabled(False)

    def prendre_wagon1(self, event):
        self.prendre_wagon(0, True)

    def prendre_wagon2(self, event):
        self.prendre_wagon(1, True)

    def prendre_wagon3(self, event):
        self.prendre_wagon(2, True)

    def prendre_wagon4(self, event):
        self.prendre_wagon(3, True)

    def prendre_wagon5(self, event):
        self.prendre_wagon(4, True)

    def prendre_pioche_wagon(self, event):
        self.prendre_wagon(5, False)

    def print_value(self, event):
        print(f"clicked: {event}")

    def mousePressEvent(self, event: QMouseEvent) -> None:
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
        self.ui.spinbox_nb_joueurs_ia.setMaximum(self.ui.spinbox_nb_joueurs_tot.value())

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
        self.ui.selection_voyageur.clear()
        for index, joueur in enumerate(self.les_joueurs[:self.nb_joueurs_tot]):
            self.ui.selection_voyageur.addItem(joueur[0])

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
        self.les_joueurs = [[f"Joueur {k + 1}", "random", False] for k in
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
        self.ui.spinbox_nb_joueurs_ia.setMaximum(self.ui.spinbox_nb_joueurs_tot.value())
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
        self.ui_main_wagons = [self.ui.main_wagon1, self.ui.main_wagon2, self.ui.main_wagon3, self.ui.main_wagon4,
                               self.ui.main_wagon5, self.ui.main_wagon6, self.ui.main_wagon7, self.ui.main_wagon8,
                               self.ui.main_wagon9]
        ordre_couleur = list(self.img_wagons)[:-1]
        for u, ui_wagon in enumerate(self.ui_main_wagons):
            couleur = ordre_couleur[u]
            ui_wagon.setText(f"{joueur.main_wagon[couleur]}")
            ui_wagon.setStyleSheet(f"background-image:url({self.img_wagons[couleur]});\n"
                                   f"background-repeat:no-repeat;\n"
                                   f"background-position:bottom;\n")

    def update_main_destination(self, joueur):
        """
        Update the current player's destination cards display.
        """
        self.hide_destinations()
        for d, destination in enumerate(self.les_destinations):
            destination_path = self.img_destinations[joueur.main_destination[d]]
            destination.setPixmap(QPixmap(destination_path))
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
        self.partie.update_wagons_stack()  # On vérifie pour les locomotives et refait la pile si tout dans la défausse.
        for w, wagon in enumerate(self.pioche_wagons):
            if self.partie.pile_cartes_wagon and w < len(self.partie.pile_cartes_wagon):
                wagon_path = self.img_wagons[self.partie.pile_cartes_wagon[w]]
                wagon.setPixmap(QPixmap(wagon_path))
                wagon.show()
            else:
                wagon.hide()
        # print(self.partie.pile_cartes_wagon)

    def hide_wagons(self):
        """
        Hide all wagons cards
        """
        for wagon in self.pioche_wagons:
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
            plain_text = f"{player.nom_joueur} : {player.nb_points} pts"
            self.autres_joueurs[p].setText(plain_text)
            self.autres_joueurs[p].show()

    def tour_joueur(self, joueur):
        """
        Une fois la partie prête, la partie est lancée via la méthode partie(ihm_partie) de la classe Partie() dans
        le module Partie.py Puis, les tours s'enchaînent jusqu'à la fin de la partie. => cf. dans la méthode partie()
        """
        # On initialise/réinitialise les variables pour l'affichage du joueur actuel.
        self.ui.titre_nom_joueur.setText(joueur.nom_joueur)
        self.ui.titre_nom_joueur.setStyleSheet(f"background-color:{joueur.couleur};\n"
                                               "border-radius:20;\n"
                                               "border-color:rgb(50,50,50);\n"
                                               "border-width:2;\n"
                                               "border-style:solid;\n"
                                               "font:18pt;")
        self.ui.button_fin_tour.hide()
        # self.ui.button_fin_partie.hide()
        self.ui.label_interaction_joueur.setText("A votre tour !")
        self.ui.score_joueur.setText(str(joueur.nb_points))
        self.update_main_joueur(joueur)
        self.update_main_destination(joueur)
        self.update_wagon_stack()
        self.update_autres_joueurs(joueur)
        self.update_choix_route()
        self.update_route_prise()

        # On active les actions possibles pour le joueur au cours de son tour
        self.ui.button_take_road.setEnabled(True)
        self.enable_prendre_wagons()
        self.ui.pioche_destination.setEnabled(True)

        if self.partie.LAST_TURN:
            self.ui.button_fin_partie.show()

        # Change d'affichage pour l'écran Joueur
        self.ui.stackedWidget.setCurrentWidget(self.ui.Joueur)

    def fin_tour(self):
        """
        Bloque toutes les options du joueur pour signaler la fin de tour.
        """
        self.ui.button_take_road.setEnabled(False)
        self.disable_prendre_wagons()
        self.ui.pioche_destination.setEnabled(False)
        self.ui.button_fin_tour.show()

    def fin_partie(self):
        """
        Met à jour l'ihm du joueur actuel pour afficher le bouton de fin de partie.
        """
        self.les_resultats = [self.ui.label_resultat1, self.ui.label_resultat2, self.ui.label_resultat3,
                              self.ui.label_resultat4, self.ui.label_resultat5]
        for resultat in self.les_resultats:
            resultat.hide()
        self.partie.end_game(self)
        tableau_resultats = [[joueur.nb_points, nom] for nom, joueur in self.partie.les_joueurs.items()]
        tableau_resultats.sort(reverse=True)
        for n, joueur in enumerate(tableau_resultats):
            self.les_resultats[n].setText(f"{n + 1}: {joueur[1]} - {joueur[0]} points ")
            self.les_resultats[n].show()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Fin_partie)

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
    app = QApplication()
    window = MonAppli()
    window.show()
    app.exec_()

    # Tests

    # # Code pour afficher un graphique dans un QGraphicView.
    # from PyQt5 import QtWidgets
    #
    # import matplotlib.pyplot as plt
    # from matplotlib.figure import Figure
    # from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    #
    # import numpy as np
    #
    # app = QApplication(sys.argv)
    #
    # scene = QGraphicsScene()
    # view = QGraphicsView(scene)
    #
    # figure = Figure()
    # axes = figure.gca()
    # # axes.set_title("My Plot")
    # x = np.linspace(1, 10)
    # y = np.linspace(1, 10)
    # y1 = np.linspace(11, 20)
    # axes.plot(x, y, "-k", label="first one")
    # axes.plot(x, y1, "-b", label="second one")
    # axes.axis(False)
    # # axes.legend()
    # # axes.grid(True)
    #
    # canvas = FigureCanvas(figure)
    # proxy_widget = scene.addWidget(canvas)
    # # or
    # # proxy_widget = QGraphicsProxyWidget()
    # # proxy_widget.setWidget(canvas)
    # # scene.addItem(proxy_widget)
    #
    # # view.resize(640, 480)
    # view.show()
    #
    # sys.exit(app.exec_())
