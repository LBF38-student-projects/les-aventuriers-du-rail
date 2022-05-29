# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2018
Modified on Fri Apr 1 16:22:00 2022

@author: Mathis URIEN
"""
import os
import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from menu_principal import *
import Joueur
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
        "Navigations entre les pages"
        # Buttons de l'écran Menu Principal
        self.ui.button_nouvelle_partie.clicked.connect(lambda: self.commencer_partie())
        self.ui.button_regles_jeu.clicked.connect(lambda: self.ouvrir_regles())
        self.ui.button_options.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Options))
        self.ui.button_credits.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Credits))
        # Buttons de l'écran Nouvelle Partie
        self.ui.button_commencer.clicked.connect(lambda: self.lancer_partie())
        self.ui.button_retour.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Menu_principal))
        # Buttons de l'écran Joueur
        self.ui.button_retour.text()
        # TODO: insérer un button de fin de partie quand le joueur ne peut plus rien faire.
        #  => à l'emplacement de interaction joueur
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

    def commencer_partie(self):
        print("On commence une nouvelle partie !")
        # On cache tous les inputs avant de connaître le nb de joueurs de la partie.
        self.show_inputs()
        self.ui.label_voyageur.hide()
        self.ui.selection_voyageur.hide()
        # Tant que les inputs ne sont pas remplis, on cache le bouton.
        self.ui.button_commencer.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Nouvelle_partie)
        # On initialise une nouvelle partie :
        self.partie = Partie_qt()
        self.les_joueurs=[] # liste des joueurs de la partie.
        self.ui.spinbox_nb_joueurs_tot.valueChanged.connect(lambda:self.show_inputs())
        self.ui.spinbox_nb_joueurs_ia.valueChanged.connect(lambda:self.show_inputs())
        self.ui.input_nom1.editingFinished.connect(lambda: self.get_player_inputs(self.ui.input_nom1,self.ui.input_couleur1))
        self.ui.input_couleur1.currentIndexChanged.connect(lambda: self.get_player_inputs(self.ui.input_nom1,self.ui.input_couleur1))
        for INPUT in self.inputs:
            INPUT[1].editingFinished.connect(lambda: self.get_player_inputs(INPUT[1],INPUT[3]))
            INPUT[3].currentIndexChanged.connect(lambda: self.get_player_inputs(INPUT[1],INPUT[3]))

    def get_player_inputs(self,input_nom,input_couleur):
        """
        Récupère les données des joueurs pour la partie.
        """
        nom=input_nom.text()
        couleur=input_couleur.currentText()
        self.les_joueurs.append([nom,couleur])
        print(nom,couleur)


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

    def show_inputs(self):
        self.hide_inputs()
        nb_joueurs_tot=self.ui.spinbox_nb_joueurs_tot.value()
        nb_joueurs_ia=self.ui.spinbox_nb_joueurs_ia.value()
        # Affichage des inputs en fonction des joueurs IRL/IAs:
        for k,INPUT in enumerate(self.inputs[:nb_joueurs_tot-nb_joueurs_ia]): # joueurs IRLs
            for i,elt in enumerate(INPUT[:-2]):
                elt.show()
                if i==1:
                    elt.clear()
                    elt.setDisabled(elt.isReadOnly())
                if i==3:
                    elt.setCurrentIndex(k)
            INPUT[-1].hide()
            INPUT[-2].hide()
        for k,INPUT in enumerate(self.inputs[nb_joueurs_tot-nb_joueurs_ia:nb_joueurs_tot]): # joueurs IAs
            for elt in INPUT:
                elt.show()
                if INPUT.index(elt)==1:
                    elt.setText(f"Joueur IA n°{k+1+nb_joueurs_tot-nb_joueurs_ia}")
                    elt.setEnabled(elt.isReadOnly())
                if INPUT.index(elt)==3:
                    elt.setCurrentIndex(elt.findText("random"))
        self.ui.stackedWidget.setCurrentWidget(self.ui.Nouvelle_partie)


    def print_text(self,elt):
        value=elt.text()
        print(value)

    def get_value(self,elt):
        print(elt.currentText())

    def lancer_partie(self):
        """
        Une fois la partie prête, on lance la partie avec l'interface du premier joueur.
        Puis, les tours s'enchaînent jusqu'à la fin de la partie.
        """
        # Button fin de partie
        button_fin_partie = QtWidgets.QPushButton(self.ui.Joueur)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(button_fin_partie.sizePolicy().hasHeightForWidth())
        button_fin_partie.setSizePolicy(sizePolicy)
        button_fin_partie.setMinimumSize(QtCore.QSize(0, 0))
        button_fin_partie.setObjectName("button_fin_partie")
        _translate = QtCore.QCoreApplication.translate
        button_fin_partie.setText(_translate("MainWindow", "Fin de partie"))
        # On cache les interactions avec le joueur
        self.ui.input_interaction.hide()
        self.ui.label_interaction_joueur.hide()
        self.ui.gridLayout_19.addWidget(button_fin_partie, 7, 0, 1, 1)
        # Connexion du button avec écran Fin de partie
        button_fin_partie.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Fin_partie))
        # lance l'écran du premier joueur:
        self.ui.stackedWidget.setCurrentWidget(self.ui.Joueur)

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
