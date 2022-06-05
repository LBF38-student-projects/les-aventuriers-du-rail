# -*- coding: utf-8 -*-

#  Copyright (c) 2022. Author(s): Mathis URIEN

################################################################################
## Form generated from reading UI file 'menu_principal.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide2.QtGui import (QFont,
                           QIcon, QPixmap)
from PySide2.QtWidgets import *


# import resource_rc


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                if MainWindow.objectName():
                        MainWindow.setObjectName(u"MainWindow")
                MainWindow.setEnabled(True)
                MainWindow.resize(980, 600)
                sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
                MainWindow.setSizePolicy(sizePolicy)
                MainWindow.setMinimumSize(QSize(980, 600))
                font = QFont()
                font.setPointSize(20)
                MainWindow.setFont(font)
                icon = QIcon()
                icon.addFile(u"img/cargo-train.png", QSize(), QIcon.Normal, QIcon.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet(u"QMainWindow{\n"
                                         "background-color: qradialgradient(spread:pad, cx:0.525, cy:0.511227, radius:1, fx:0.811445, fy:0.920433, stop:0.0895522 rgba(88, 255, 255, 255), stop:1 rgba(40, 152, 127, 255));\n"
                                         "}\n"
                                         "QPushButton{\n"
                                         "font: 20pt \"chippewafallsnf\";\n"
                                         "background-color:lightgrey;\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 20px;\n"
                                         "border-color: grey;\n"
                                         "}\n"
                                         "QLabel{\n"
                                         "font:12pt \"ShangriLaNFSmallCaps\";\n"
                                         "}\n"
                                         "QComboBox{\n"
                                         "font: 8pt \"ShangriLaNFSmallCaps\";\n"
                                         "background-color:lightgrey;\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: grey;\n"
                                         "}\n"
                                         "QSpinBox{\n"
                                         "font: 10pt \"ShangriLaNFSmallCaps\";\n"
                                         "background-color:lightgrey;\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: grey;\n"
                                         "}\n"
                                         "QLineEdit{\n"
                                         "font: 8pt \"ShangriLaNFSmallCaps\";\n"
                                         "background-color:lightgrey;\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: grey;\n"
                                         "}\n"
                                         "")
                self.actionQuitter = QAction(MainWindow)
                self.actionQuitter.setObjectName(u"actionQuitter")
                self.actionRegles_du_jeu = QAction(MainWindow)
                self.actionRegles_du_jeu.setObjectName(u"actionRegles_du_jeu")
                self.actionOptions = QAction(MainWindow)
                self.actionOptions.setObjectName(u"actionOptions")
                self.actionOptions.setShortcutVisibleInContextMenu(True)
                self.centralwidget = QWidget(MainWindow)
                self.centralwidget.setObjectName(u"centralwidget")
                self.centralwidget.setStyleSheet(u"")
                self.verticalLayout = QVBoxLayout(self.centralwidget)
                self.verticalLayout.setObjectName(u"verticalLayout")
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.stackedWidget = QStackedWidget(self.centralwidget)
                self.stackedWidget.setObjectName(u"stackedWidget")
                self.stackedWidget.setStyleSheet(u"")
                self.Menu_principal = QWidget()
                self.Menu_principal.setObjectName(u"Menu_principal")
                self.Menu_principal.setStyleSheet(u"QWidget#Menu_principal{\n"
                                                  "border-image: url(img/menu_principal.jpg);\n"
                                                  "background-repeat:no-repeat;\n"
                                                  "background-position:center;\n"
                                                  "}")
                self.gridLayout = QGridLayout(self.Menu_principal)
                self.gridLayout.setObjectName(u"gridLayout")
                self.gridLayout.setContentsMargins(50, 200, 50, 50)
                self.button_options = QPushButton(self.Menu_principal)
                self.button_options.setObjectName(u"button_options")

                self.gridLayout.addWidget(self.button_options, 4, 0, 1, 1)

                self.button_credits = QPushButton(self.Menu_principal)
                self.button_credits.setObjectName(u"button_credits")

                self.gridLayout.addWidget(self.button_credits, 4, 1, 1, 1)

                self.button_regles_jeu = QPushButton(self.Menu_principal)
                self.button_regles_jeu.setObjectName(u"button_regles_jeu")

                self.gridLayout.addWidget(self.button_regles_jeu, 2, 0, 1, 2)

                self.button_nouvelle_partie = QPushButton(self.Menu_principal)
                self.button_nouvelle_partie.setObjectName(u"button_nouvelle_partie")
                self.button_nouvelle_partie.setMinimumSize(QSize(0, 0))

                self.gridLayout.addWidget(self.button_nouvelle_partie, 1, 0, 1, 2)

                self.stackedWidget.addWidget(self.Menu_principal)
                self.Nouvelle_partie = QWidget()
                self.Nouvelle_partie.setObjectName(u"Nouvelle_partie")
                self.Nouvelle_partie.setAutoFillBackground(False)
                self.Nouvelle_partie.setStyleSheet(u"QWidget#Nouvelle_partie{\n"
                                                   "border-image:url(img/background_ticket_to_ride.jpg);\n"
                                                   "background-repeat:no-repeat;\n"
                                                   "background-position:center;\n"
                                                   "}\n"
                                                   "QPushButton{\n"
                                                   "font:10pt;\n"
                                                   "width: 100;\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QLabel{\n"
                                                   "font:10pt;\n"
                                                   "}\n"
                                                   "QLabel#titre_nouvelle_partie{\n"
                                                   "font:28pt \"chippewafallsnf\";\n"
                                                   "}")
                self.gridLayout_2 = QGridLayout(self.Nouvelle_partie)
                self.gridLayout_2.setObjectName(u"gridLayout_2")
                self.gridLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
                self.gridLayout_2.setContentsMargins(80, -1, 70, 30)
                self.choix_IA2 = QComboBox(self.Nouvelle_partie)
                self.choix_IA2.addItem("")
                self.choix_IA2.addItem("")
                self.choix_IA2.addItem("")
                self.choix_IA2.addItem("")
                self.choix_IA2.setObjectName(u"choix_IA2")

                self.gridLayout_2.addWidget(self.choix_IA2, 7, 3, 1, 1)

                self.label_difficulty5 = QLabel(self.Nouvelle_partie)
                self.label_difficulty5.setObjectName(u"label_difficulty5")
                sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
                sizePolicy1.setHorizontalStretch(0)
                sizePolicy1.setVerticalStretch(0)
                sizePolicy1.setHeightForWidth(self.label_difficulty5.sizePolicy().hasHeightForWidth())
                self.label_difficulty5.setSizePolicy(sizePolicy1)

                self.gridLayout_2.addWidget(self.label_difficulty5, 10, 1, 1, 1)

                self.titre_nouvelle_partie = QLabel(self.Nouvelle_partie)
                self.titre_nouvelle_partie.setObjectName(u"titre_nouvelle_partie")
                sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
                sizePolicy2.setHorizontalStretch(0)
                sizePolicy2.setVerticalStretch(0)
                sizePolicy2.setHeightForWidth(self.titre_nouvelle_partie.sizePolicy().hasHeightForWidth())
                self.titre_nouvelle_partie.setSizePolicy(sizePolicy2)
                self.titre_nouvelle_partie.setMinimumSize(QSize(200, 100))
                font1 = QFont()
                font1.setFamily(u"chippewafallsnf")
                font1.setPointSize(28)
                font1.setBold(False)
                font1.setItalic(False)
                font1.setWeight(50)
                font1.setStyleStrategy(QFont.PreferDefault)
                self.titre_nouvelle_partie.setFont(font1)
                self.titre_nouvelle_partie.setStyleSheet(u"")
                self.titre_nouvelle_partie.setFrameShape(QFrame.NoFrame)
                self.titre_nouvelle_partie.setFrameShadow(QFrame.Plain)
                self.titre_nouvelle_partie.setAlignment(Qt.AlignCenter)
                self.titre_nouvelle_partie.setWordWrap(False)
                self.titre_nouvelle_partie.setMargin(0)

                self.gridLayout_2.addWidget(self.titre_nouvelle_partie, 0, 0, 2, 5)

                self.choix_IA4 = QComboBox(self.Nouvelle_partie)
                self.choix_IA4.addItem("")
                self.choix_IA4.addItem("")
                self.choix_IA4.addItem("")
                self.choix_IA4.addItem("")
                self.choix_IA4.setObjectName(u"choix_IA4")

                self.gridLayout_2.addWidget(self.choix_IA4, 9, 3, 1, 1)

                self.input_j1 = QGridLayout()
                self.input_j1.setObjectName(u"input_j1")
                self.input_nom1 = QLineEdit(self.Nouvelle_partie)
                self.input_nom1.setObjectName(u"input_nom1")
                sizePolicy1.setHeightForWidth(self.input_nom1.sizePolicy().hasHeightForWidth())
                self.input_nom1.setSizePolicy(sizePolicy1)
                self.input_nom1.setMinimumSize(QSize(200, 24))

                self.input_j1.addWidget(self.input_nom1, 0, 1, 1, 1)

                self.label_couleur1 = QLabel(self.Nouvelle_partie)
                self.label_couleur1.setObjectName(u"label_couleur1")
                self.label_couleur1.setMinimumSize(QSize(114, 22))

                self.input_j1.addWidget(self.label_couleur1, 1, 0, 1, 1)

                self.label_nom1 = QLabel(self.Nouvelle_partie)
                self.label_nom1.setObjectName(u"label_nom1")
                self.label_nom1.setMinimumSize(QSize(114, 24))

                self.input_j1.addWidget(self.label_nom1, 0, 0, 1, 1)

                self.input_couleur1 = QComboBox(self.Nouvelle_partie)
                self.input_couleur1.addItem("")
                self.input_couleur1.addItem("")
                self.input_couleur1.addItem("")
                self.input_couleur1.addItem("")
                self.input_couleur1.addItem("")
                self.input_couleur1.addItem("")
                self.input_couleur1.addItem("")
                self.input_couleur1.setObjectName(u"input_couleur1")
                sizePolicy1.setHeightForWidth(self.input_couleur1.sizePolicy().hasHeightForWidth())
                self.input_couleur1.setSizePolicy(sizePolicy1)
                self.input_couleur1.setMinimumSize(QSize(200, 22))

                self.input_j1.addWidget(self.input_couleur1, 1, 1, 1, 1)

                self.separation1 = QFrame(self.Nouvelle_partie)
                self.separation1.setObjectName(u"separation1")
                self.separation1.setFrameShape(QFrame.HLine)
                self.separation1.setFrameShadow(QFrame.Sunken)

                self.input_j1.addWidget(self.separation1, 2, 0, 1, 2)

                self.gridLayout_2.addLayout(self.input_j1, 5, 0, 2, 1)

                self.input_j2 = QGridLayout()
                self.input_j2.setObjectName(u"input_j2")
                self.label_nom2 = QLabel(self.Nouvelle_partie)
                self.label_nom2.setObjectName(u"label_nom2")
                self.label_nom2.setMinimumSize(QSize(114, 24))

                self.input_j2.addWidget(self.label_nom2, 0, 0, 1, 1)

                self.label_couleur2 = QLabel(self.Nouvelle_partie)
                self.label_couleur2.setObjectName(u"label_couleur2")
                self.label_couleur2.setMinimumSize(QSize(114, 22))

                self.input_j2.addWidget(self.label_couleur2, 1, 0, 1, 1)

                self.input_couleur2 = QComboBox(self.Nouvelle_partie)
                self.input_couleur2.addItem("")
                self.input_couleur2.addItem("")
                self.input_couleur2.addItem("")
                self.input_couleur2.addItem("")
                self.input_couleur2.addItem("")
                self.input_couleur2.addItem("")
                self.input_couleur2.addItem("")
                self.input_couleur2.setObjectName(u"input_couleur2")
                self.input_couleur2.setMinimumSize(QSize(200, 22))

                self.input_j2.addWidget(self.input_couleur2, 1, 1, 1, 1)

                self.input_nom2 = QLineEdit(self.Nouvelle_partie)
                self.input_nom2.setObjectName(u"input_nom2")
                sizePolicy1.setHeightForWidth(self.input_nom2.sizePolicy().hasHeightForWidth())
                self.input_nom2.setSizePolicy(sizePolicy1)
                self.input_nom2.setMinimumSize(QSize(200, 24))

                self.input_j2.addWidget(self.input_nom2, 0, 1, 1, 1)

                self.separation2 = QFrame(self.Nouvelle_partie)
                self.separation2.setObjectName(u"separation2")
                self.separation2.setFrameShape(QFrame.HLine)
                self.separation2.setFrameShadow(QFrame.Sunken)

                self.input_j2.addWidget(self.separation2, 2, 0, 1, 2)

                self.gridLayout_2.addLayout(self.input_j2, 7, 0, 1, 1)

                self.choix_IA1 = QComboBox(self.Nouvelle_partie)
                self.choix_IA1.addItem("")
                self.choix_IA1.addItem("")
                self.choix_IA1.addItem("")
                self.choix_IA1.addItem("")
                self.choix_IA1.setObjectName(u"choix_IA1")

                self.gridLayout_2.addWidget(self.choix_IA1, 5, 3, 2, 1)

                self.nb_joueurs = QGridLayout()
                self.nb_joueurs.setObjectName(u"nb_joueurs")
                self.label_nb_joueurs_tot = QLabel(self.Nouvelle_partie)
                self.label_nb_joueurs_tot.setObjectName(u"label_nb_joueurs_tot")
                sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
                sizePolicy3.setHorizontalStretch(0)
                sizePolicy3.setVerticalStretch(0)
                sizePolicy3.setHeightForWidth(self.label_nb_joueurs_tot.sizePolicy().hasHeightForWidth())
                self.label_nb_joueurs_tot.setSizePolicy(sizePolicy3)
                font2 = QFont()
                font2.setFamily(u"ShangriLaNFSmallCaps")
                font2.setPointSize(10)
                font2.setBold(False)
                font2.setItalic(False)
                font2.setWeight(50)
                self.label_nb_joueurs_tot.setFont(font2)

                self.nb_joueurs.addWidget(self.label_nb_joueurs_tot, 0, 0, 1, 1)

                self.spinbox_nb_joueurs_tot = QSpinBox(self.Nouvelle_partie)
                self.spinbox_nb_joueurs_tot.setObjectName(u"spinbox_nb_joueurs_tot")
                sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                sizePolicy4.setHorizontalStretch(0)
                sizePolicy4.setVerticalStretch(0)
                sizePolicy4.setHeightForWidth(self.spinbox_nb_joueurs_tot.sizePolicy().hasHeightForWidth())
                self.spinbox_nb_joueurs_tot.setSizePolicy(sizePolicy4)
                self.spinbox_nb_joueurs_tot.setMinimumSize(QSize(50, 15))
                self.spinbox_nb_joueurs_tot.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
                self.spinbox_nb_joueurs_tot.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
                self.spinbox_nb_joueurs_tot.setMinimum(2)
                self.spinbox_nb_joueurs_tot.setMaximum(5)

                self.nb_joueurs.addWidget(self.spinbox_nb_joueurs_tot, 0, 1, 1, 1)

                self.label_nb_joueurs_ia = QLabel(self.Nouvelle_partie)
                self.label_nb_joueurs_ia.setObjectName(u"label_nb_joueurs_ia")
                sizePolicy3.setHeightForWidth(self.label_nb_joueurs_ia.sizePolicy().hasHeightForWidth())
                self.label_nb_joueurs_ia.setSizePolicy(sizePolicy3)
                self.label_nb_joueurs_ia.setFont(font2)

                self.nb_joueurs.addWidget(self.label_nb_joueurs_ia, 1, 0, 1, 1)

                self.spinbox_nb_joueurs_ia = QSpinBox(self.Nouvelle_partie)
                self.spinbox_nb_joueurs_ia.setObjectName(u"spinbox_nb_joueurs_ia")
                sizePolicy4.setHeightForWidth(self.spinbox_nb_joueurs_ia.sizePolicy().hasHeightForWidth())
                self.spinbox_nb_joueurs_ia.setSizePolicy(sizePolicy4)
                self.spinbox_nb_joueurs_ia.setMinimumSize(QSize(50, 15))
                self.spinbox_nb_joueurs_ia.setMaximum(4)

                self.nb_joueurs.addWidget(self.spinbox_nb_joueurs_ia, 1, 1, 1, 1)

                self.gridLayout_2.addLayout(self.nb_joueurs, 2, 0, 1, 1)

                self.choix_IA5 = QComboBox(self.Nouvelle_partie)
                self.choix_IA5.addItem("")
                self.choix_IA5.addItem("")
                self.choix_IA5.addItem("")
                self.choix_IA5.addItem("")
                self.choix_IA5.setObjectName(u"choix_IA5")

                self.gridLayout_2.addWidget(self.choix_IA5, 10, 3, 1, 1)

                self.input_j3 = QGridLayout()
                self.input_j3.setObjectName(u"input_j3")
                self.label_nom3 = QLabel(self.Nouvelle_partie)
                self.label_nom3.setObjectName(u"label_nom3")
                self.label_nom3.setMinimumSize(QSize(114, 24))

                self.input_j3.addWidget(self.label_nom3, 0, 0, 1, 1)

                self.label_couleur3 = QLabel(self.Nouvelle_partie)
                self.label_couleur3.setObjectName(u"label_couleur3")
                self.label_couleur3.setMinimumSize(QSize(114, 22))

                self.input_j3.addWidget(self.label_couleur3, 1, 0, 1, 1)

                self.input_couleur3 = QComboBox(self.Nouvelle_partie)
                self.input_couleur3.addItem("")
                self.input_couleur3.addItem("")
                self.input_couleur3.addItem("")
                self.input_couleur3.addItem("")
                self.input_couleur3.addItem("")
                self.input_couleur3.addItem("")
                self.input_couleur3.addItem("")
                self.input_couleur3.setObjectName(u"input_couleur3")
                self.input_couleur3.setMinimumSize(QSize(200, 22))

                self.input_j3.addWidget(self.input_couleur3, 1, 1, 1, 1)

                self.input_nom3 = QLineEdit(self.Nouvelle_partie)
                self.input_nom3.setObjectName(u"input_nom3")
                sizePolicy1.setHeightForWidth(self.input_nom3.sizePolicy().hasHeightForWidth())
                self.input_nom3.setSizePolicy(sizePolicy1)
                self.input_nom3.setMinimumSize(QSize(200, 24))

                self.input_j3.addWidget(self.input_nom3, 0, 1, 1, 1)

                self.separation3 = QFrame(self.Nouvelle_partie)
                self.separation3.setObjectName(u"separation3")
                self.separation3.setFrameShape(QFrame.HLine)
                self.separation3.setFrameShadow(QFrame.Sunken)

                self.input_j3.addWidget(self.separation3, 2, 0, 1, 2)

                self.gridLayout_2.addLayout(self.input_j3, 8, 0, 1, 1)

                self.label_difficulty1 = QLabel(self.Nouvelle_partie)
                self.label_difficulty1.setObjectName(u"label_difficulty1")
                sizePolicy1.setHeightForWidth(self.label_difficulty1.sizePolicy().hasHeightForWidth())
                self.label_difficulty1.setSizePolicy(sizePolicy1)

                self.gridLayout_2.addWidget(self.label_difficulty1, 5, 1, 2, 1)

                self.label_difficulty4 = QLabel(self.Nouvelle_partie)
                self.label_difficulty4.setObjectName(u"label_difficulty4")
                sizePolicy1.setHeightForWidth(self.label_difficulty4.sizePolicy().hasHeightForWidth())
                self.label_difficulty4.setSizePolicy(sizePolicy1)

                self.gridLayout_2.addWidget(self.label_difficulty4, 9, 1, 1, 1)

                self.label_difficulty3 = QLabel(self.Nouvelle_partie)
                self.label_difficulty3.setObjectName(u"label_difficulty3")
                sizePolicy1.setHeightForWidth(self.label_difficulty3.sizePolicy().hasHeightForWidth())
                self.label_difficulty3.setSizePolicy(sizePolicy1)

                self.gridLayout_2.addWidget(self.label_difficulty3, 8, 1, 1, 1)

                self.label_difficulty2 = QLabel(self.Nouvelle_partie)
                self.label_difficulty2.setObjectName(u"label_difficulty2")
                sizePolicy1.setHeightForWidth(self.label_difficulty2.sizePolicy().hasHeightForWidth())
                self.label_difficulty2.setSizePolicy(sizePolicy1)

                self.gridLayout_2.addWidget(self.label_difficulty2, 7, 1, 1, 1)

                self.choix_IA3 = QComboBox(self.Nouvelle_partie)
                self.choix_IA3.addItem("")
                self.choix_IA3.addItem("")
                self.choix_IA3.addItem("")
                self.choix_IA3.addItem("")
                self.choix_IA3.setObjectName(u"choix_IA3")

                self.gridLayout_2.addWidget(self.choix_IA3, 8, 3, 1, 1)

                self.input_j5 = QGridLayout()
                self.input_j5.setObjectName(u"input_j5")
                self.label_nom5 = QLabel(self.Nouvelle_partie)
                self.label_nom5.setObjectName(u"label_nom5")
                self.label_nom5.setMinimumSize(QSize(114, 24))

                self.input_j5.addWidget(self.label_nom5, 0, 0, 1, 1)

                self.label_couleur5 = QLabel(self.Nouvelle_partie)
                self.label_couleur5.setObjectName(u"label_couleur5")
                self.label_couleur5.setMinimumSize(QSize(114, 22))

                self.input_j5.addWidget(self.label_couleur5, 1, 0, 1, 1)

                self.input_couleur5 = QComboBox(self.Nouvelle_partie)
                self.input_couleur5.addItem("")
                self.input_couleur5.addItem("")
                self.input_couleur5.addItem("")
                self.input_couleur5.addItem("")
                self.input_couleur5.addItem("")
                self.input_couleur5.addItem("")
                self.input_couleur5.addItem("")
                self.input_couleur5.setObjectName(u"input_couleur5")
                self.input_couleur5.setMinimumSize(QSize(200, 22))

                self.input_j5.addWidget(self.input_couleur5, 1, 1, 1, 1)

                self.input_nom5 = QLineEdit(self.Nouvelle_partie)
                self.input_nom5.setObjectName(u"input_nom5")
                sizePolicy1.setHeightForWidth(self.input_nom5.sizePolicy().hasHeightForWidth())
                self.input_nom5.setSizePolicy(sizePolicy1)
                self.input_nom5.setMinimumSize(QSize(200, 24))

                self.input_j5.addWidget(self.input_nom5, 0, 1, 1, 1)

                self.separation5 = QFrame(self.Nouvelle_partie)
                self.separation5.setObjectName(u"separation5")
                self.separation5.setFrameShape(QFrame.HLine)
                self.separation5.setFrameShadow(QFrame.Sunken)

                self.input_j5.addWidget(self.separation5, 2, 0, 1, 2)

                self.gridLayout_2.addLayout(self.input_j5, 10, 0, 1, 1)

                self.input_j4 = QGridLayout()
                self.input_j4.setObjectName(u"input_j4")
                self.label_nom4 = QLabel(self.Nouvelle_partie)
                self.label_nom4.setObjectName(u"label_nom4")
                self.label_nom4.setMinimumSize(QSize(114, 24))

                self.input_j4.addWidget(self.label_nom4, 0, 0, 1, 1)

                self.label_couleur4 = QLabel(self.Nouvelle_partie)
                self.label_couleur4.setObjectName(u"label_couleur4")
                self.label_couleur4.setMinimumSize(QSize(114, 22))

                self.input_j4.addWidget(self.label_couleur4, 1, 0, 1, 1)

                self.input_couleur4 = QComboBox(self.Nouvelle_partie)
                self.input_couleur4.addItem("")
                self.input_couleur4.addItem("")
                self.input_couleur4.addItem("")
                self.input_couleur4.addItem("")
                self.input_couleur4.addItem("")
                self.input_couleur4.addItem("")
                self.input_couleur4.addItem("")
                self.input_couleur4.setObjectName(u"input_couleur4")
                self.input_couleur4.setMinimumSize(QSize(200, 22))

                self.input_j4.addWidget(self.input_couleur4, 1, 1, 1, 1)

                self.input_nom4 = QLineEdit(self.Nouvelle_partie)
                self.input_nom4.setObjectName(u"input_nom4")
                sizePolicy1.setHeightForWidth(self.input_nom4.sizePolicy().hasHeightForWidth())
                self.input_nom4.setSizePolicy(sizePolicy1)
                self.input_nom4.setMinimumSize(QSize(200, 24))

                self.input_j4.addWidget(self.input_nom4, 0, 1, 1, 1)

                self.separation4 = QFrame(self.Nouvelle_partie)
                self.separation4.setObjectName(u"separation4")
                self.separation4.setFrameShape(QFrame.HLine)
                self.separation4.setFrameShadow(QFrame.Sunken)

                self.input_j4.addWidget(self.separation4, 2, 0, 1, 2)

                self.gridLayout_2.addLayout(self.input_j4, 9, 0, 1, 1)

                self.button_commencer = QPushButton(self.Nouvelle_partie)
                self.button_commencer.setObjectName(u"button_commencer")
                sizePolicy4.setHeightForWidth(self.button_commencer.sizePolicy().hasHeightForWidth())
                self.button_commencer.setSizePolicy(sizePolicy4)
                self.button_commencer.setMinimumSize(QSize(0, 0))
                font3 = QFont()
                font3.setFamily(u"chippewafallsnf")
                font3.setPointSize(10)
                font3.setBold(False)
                font3.setItalic(False)
                font3.setWeight(50)
                self.button_commencer.setFont(font3)
                self.button_commencer.setLayoutDirection(Qt.LeftToRight)

                self.gridLayout_2.addWidget(self.button_commencer, 11, 4, 1, 1)

                self.button_retour = QPushButton(self.Nouvelle_partie)
                self.button_retour.setObjectName(u"button_retour")
                sizePolicy4.setHeightForWidth(self.button_retour.sizePolicy().hasHeightForWidth())
                self.button_retour.setSizePolicy(sizePolicy4)
                self.button_retour.setMinimumSize(QSize(0, 0))

                self.gridLayout_2.addWidget(self.button_retour, 12, 4, 1, 1)

                self.separation_principale = QFrame(self.Nouvelle_partie)
                self.separation_principale.setObjectName(u"separation_principale")
                sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
                sizePolicy5.setHorizontalStretch(0)
                sizePolicy5.setVerticalStretch(0)
                sizePolicy5.setHeightForWidth(self.separation_principale.sizePolicy().hasHeightForWidth())
                self.separation_principale.setSizePolicy(sizePolicy5)
                self.separation_principale.setAutoFillBackground(False)
                self.separation_principale.setStyleSheet(u"")
                self.separation_principale.setLineWidth(3)
                self.separation_principale.setMidLineWidth(0)
                self.separation_principale.setFrameShape(QFrame.HLine)
                self.separation_principale.setFrameShadow(QFrame.Sunken)

                self.gridLayout_2.addWidget(self.separation_principale, 4, 0, 1, 5)

                self.horizontalLayout = QHBoxLayout()
                self.horizontalLayout.setObjectName(u"horizontalLayout")
                self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
                self.label_voyageur = QLabel(self.Nouvelle_partie)
                self.label_voyageur.setObjectName(u"label_voyageur")
                sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
                sizePolicy6.setHorizontalStretch(0)
                sizePolicy6.setVerticalStretch(0)
                sizePolicy6.setHeightForWidth(self.label_voyageur.sizePolicy().hasHeightForWidth())
                self.label_voyageur.setSizePolicy(sizePolicy6)
                self.label_voyageur.setFont(font2)
                self.label_voyageur.setWordWrap(True)

                self.horizontalLayout.addWidget(self.label_voyageur)

                self.selection_voyageur = QComboBox(self.Nouvelle_partie)
                self.selection_voyageur.addItem("")
                self.selection_voyageur.addItem("")
                self.selection_voyageur.setObjectName(u"selection_voyageur")
                sizePolicy4.setHeightForWidth(self.selection_voyageur.sizePolicy().hasHeightForWidth())
                self.selection_voyageur.setSizePolicy(sizePolicy4)

                self.horizontalLayout.addWidget(self.selection_voyageur)

                self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 5)

                self.stackedWidget.addWidget(self.Nouvelle_partie)
                self.Joueur = QWidget()
                self.Joueur.setObjectName(u"Joueur")
                self.Joueur.setStyleSheet(u"QWidget#Joueur{\n"
                                          "background-color: rgb(240, 240, 240);\n"
                                          "}\n"
                                          "QLabel{\n"
                                          "font:10pt;\n"
                                          "}\n"
                                          "QPushButton{\n"
                                          "font:12pt;\n"
                                          "border-radius:10px;\n"
                                          "}")
                self.gridLayout_19 = QGridLayout(self.Joueur)
                self.gridLayout_19.setObjectName(u"gridLayout_19")
                self.score_joueur = QLabel(self.Joueur)
                self.score_joueur.setObjectName(u"score_joueur")
                self.score_joueur.setFont(font2)
                self.score_joueur.setStyleSheet(
                        u"background-color: qradialgradient(spread:pad, cx:0, cy:0, radius:1.377, fx:0, fy:0, stop:0  rgb(136, "
                        u"136, 136), stop:1 rgb(240, 240, 240));\n "
                        "border-radius: 10;\n"
                        "border-width:2;\n"
                        "border-style:solid;\n"
                        "border-color:rgb(120,120,120);")
                self.score_joueur.setScaledContents(False)
                self.score_joueur.setAlignment(Qt.AlignCenter)

                self.gridLayout_19.addWidget(self.score_joueur, 7, 6, 1, 1)

                self.main_wagons = QHBoxLayout()
                self.main_wagons.setSpacing(0)
                self.main_wagons.setObjectName(u"main_wagons")
                self.main_wagons.setContentsMargins(5, -1, 5, -1)
                self.main_wagon1 = QLabel(self.Joueur)
                self.main_wagon1.setObjectName(u"main_wagon1")
                self.main_wagon1.setMinimumSize(QSize(100, 64))
                self.main_wagon1.setFont(font2)
                self.main_wagon1.setText("")
                self.main_wagon1.setStyleSheet("background-image:url(img/wagon_vert.jpg)")
                self.main_wagon1.setScaledContents(False)
                self.main_wagon1.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

                self.main_wagons.addWidget(self.main_wagon1)

                self.main_wagon2 = QLabel(self.Joueur)
                self.main_wagon2.setObjectName(u"main_wagon2")
                self.main_wagon2.setMinimumSize(QSize(100, 64))
                self.main_wagon2.setStyleSheet("background-image:url(img/wagon_rouge.jpg)")
                self.main_wagon2.setScaledContents(False)
                self.main_wagon2.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

                self.main_wagons.addWidget(self.main_wagon2)

                self.main_wagon3 = QLabel(self.Joueur)
                self.main_wagon3.setObjectName(u"main_wagon3")
                self.main_wagon3.setMinimumSize(QSize(100, 64))
                self.main_wagon3.setStyleSheet("background-image:url(img/wagon_rose.jpg)")
                self.main_wagon3.setScaledContents(False)
                self.main_wagon3.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

                self.main_wagons.addWidget(self.main_wagon3)

                self.main_wagon4 = QLabel(self.Joueur)
                self.main_wagon4.setObjectName(u"main_wagon4")
                self.main_wagon4.setMinimumSize(QSize(100, 64))
                self.main_wagon4.setStyleSheet("background-image:url(img/wagon_orange.jpg)")
                self.main_wagon4.setScaledContents(False)
                self.main_wagon4.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

                self.main_wagons.addWidget(self.main_wagon4)

                self.main_wagon5 = QLabel(self.Joueur)
                self.main_wagon5.setObjectName(u"main_wagon5")
                self.main_wagon5.setMinimumSize(QSize(100, 64))
                self.main_wagon5.setStyleSheet("background-image:url(img/wagon_noir.jpg)")
                self.main_wagon5.setScaledContents(False)
                self.main_wagon5.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

                self.main_wagons.addWidget(self.main_wagon5)

                self.main_wagon6 = QLabel(self.Joueur)
                self.main_wagon6.setObjectName(u"main_wagon6")
                self.main_wagon6.setMinimumSize(QSize(100, 64))
                self.main_wagon6.setStyleSheet("background-image:url(img/wagon_jaune.jpg)")
                self.main_wagon6.setScaledContents(False)
                self.main_wagon6.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

                self.main_wagons.addWidget(self.main_wagon6)

                self.main_wagon7 = QLabel(self.Joueur)
                self.main_wagon7.setObjectName(u"main_wagon7")
                self.main_wagon7.setMinimumSize(QSize(100, 64))
                self.main_wagon7.setStyleSheet("background-image:url(img/wagon_bleu.jpg)")
                self.main_wagon7.setScaledContents(False)
                self.main_wagon7.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

                self.main_wagons.addWidget(self.main_wagon7)

                self.main_wagon8 = QLabel(self.Joueur)
                self.main_wagon8.setObjectName(u"main_wagon8")
                self.main_wagon8.setMinimumSize(QSize(100, 64))
                self.main_wagon8.setStyleSheet("background-image:url(img/wagon_blanc.jpg)")
                self.main_wagon8.setScaledContents(False)
                self.main_wagon8.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

                self.main_wagons.addWidget(self.main_wagon8)

                self.main_wagon9 = QLabel(self.Joueur)
                self.main_wagon9.setObjectName(u"main_wagon9")
                self.main_wagon9.setMinimumSize(QSize(100, 64))
                self.main_wagon9.setStyleSheet("background-image:url(img/locomotive.jpg")
                self.main_wagon9.setScaledContents(False)
                self.main_wagon9.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

                self.main_wagons.addWidget(self.main_wagon9)

                self.main_wagons.setStretch(1, 1)
                self.main_wagons.setStretch(2, 1)
                self.main_wagons.setStretch(3, 1)
                self.main_wagons.setStretch(4, 1)
                self.main_wagons.setStretch(5, 1)
                self.main_wagons.setStretch(6, 1)
                self.main_wagons.setStretch(7, 1)
                self.main_wagons.setStretch(8, 1)

                self.gridLayout_19.addLayout(self.main_wagons, 7, 1, 1, 5)

                self.interaction_joueur = QVBoxLayout()
                self.interaction_joueur.setObjectName(u"interaction_joueur")
                self.label_interaction_joueur = QLabel(self.Joueur)
                self.label_interaction_joueur.setObjectName(u"label_interaction_joueur")
                sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                sizePolicy7.setHorizontalStretch(0)
                sizePolicy7.setVerticalStretch(0)
                sizePolicy7.setHeightForWidth(self.label_interaction_joueur.sizePolicy().hasHeightForWidth())
                self.label_interaction_joueur.setSizePolicy(sizePolicy7)
                self.label_interaction_joueur.setMinimumSize(QSize(135, 34))
                self.label_interaction_joueur.setStyleSheet(u"font:8pt;")
                self.label_interaction_joueur.setWordWrap(True)

                self.interaction_joueur.addWidget(self.label_interaction_joueur)

                self.button_take_road = QPushButton(self.Joueur)
                self.button_take_road.setObjectName(u"button_take_road")
                font4 = QFont()
                font4.setFamily(u"chippewafallsnf")
                font4.setPointSize(8)
                font4.setBold(False)
                font4.setItalic(False)
                font4.setWeight(50)
                self.button_take_road.setFont(font4)
                self.button_take_road.setStyleSheet(u"font:8pt;\n"
                                                    "")
                self.button_take_road.setCheckable(False)

                self.interaction_joueur.addWidget(self.button_take_road)

                self.gridLayout_19.addLayout(self.interaction_joueur, 7, 0, 1, 1)

                self.button_fin_partie = QPushButton(self.Joueur)
                self.button_fin_partie.setObjectName(u"button_fin_partie")

                self.gridLayout_19.addWidget(self.button_fin_partie, 1, 0, 1, 1)

                self.plateau_jeu = QHBoxLayout()
                self.plateau_jeu.setObjectName(u"plateau_jeu")
                self.spacer_gauche = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.plateau_jeu.addItem(self.spacer_gauche)

                self.wagons_visibles = QVBoxLayout()
                self.wagons_visibles.setSpacing(5)
                self.wagons_visibles.setObjectName(u"wagons_visibles")
                self.wagons_visibles.setContentsMargins(-1, 0, -1, 0)
                self.wagon_spacer_haut = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

                self.wagons_visibles.addItem(self.wagon_spacer_haut)

                self.wagon1 = QLabel(self.Joueur)
                self.wagon1.setObjectName(u"wagon1")
                self.wagon1.setMinimumSize(QSize(100, 64))
                self.wagon1.setPixmap(QPixmap(u"img/wagon_jaune.jpg"))
                self.wagon1.setScaledContents(False)

                self.wagons_visibles.addWidget(self.wagon1)

                self.wagon2 = QLabel(self.Joueur)
                self.wagon2.setObjectName(u"wagon2")
                self.wagon2.setMinimumSize(QSize(100, 64))
                self.wagon2.setPixmap(QPixmap(u"img/wagon_noir.jpg"))
                self.wagon2.setScaledContents(False)

                self.wagons_visibles.addWidget(self.wagon2)

                self.wagon3 = QLabel(self.Joueur)
                self.wagon3.setObjectName(u"wagon3")
                self.wagon3.setMinimumSize(QSize(100, 64))
                self.wagon3.setPixmap(QPixmap(u"img/wagon_orange.jpg"))
                self.wagon3.setScaledContents(False)

                self.wagons_visibles.addWidget(self.wagon3)

                self.wagon4 = QLabel(self.Joueur)
                self.wagon4.setObjectName(u"wagon4")
                self.wagon4.setMinimumSize(QSize(100, 64))
                self.wagon4.setPixmap(QPixmap(u"img/wagon_rose.jpg"))
                self.wagon4.setScaledContents(False)

                self.wagons_visibles.addWidget(self.wagon4)

                self.wagon5 = QLabel(self.Joueur)
                self.wagon5.setObjectName(u"wagon5")
                self.wagon5.setMinimumSize(QSize(100, 64))
                self.wagon5.setPixmap(QPixmap(u"img/wagon_bleu.jpg"))
                self.wagon5.setScaledContents(False)

                self.wagons_visibles.addWidget(self.wagon5)

                self.wagon_spacer_bas = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

                self.wagons_visibles.addItem(self.wagon_spacer_bas)

                self.plateau_jeu.addLayout(self.wagons_visibles)

                self.carte_spacer_gauche = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.plateau_jeu.addItem(self.carte_spacer_gauche)

                self.emplacement_carte = QGraphicsView(self.Joueur)
                self.emplacement_carte.setObjectName(u"emplacement_carte")
                self.emplacement_carte.setMinimumSize(QSize(603, 380))
                # self.emplacement_carte.setStyleSheet(u"background-image:url(img/carte_usa.jpg)")
                self.emplacement_carte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.emplacement_carte.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.emplacement_carte.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
                self.emplacement_carte.setResizeAnchor(QGraphicsView.AnchorViewCenter)

                self.plateau_jeu.addWidget(self.emplacement_carte)

                self.carte_spacer_droit = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.plateau_jeu.addItem(self.carte_spacer_droit)

                self.main_destination = QVBoxLayout()
                self.main_destination.setSpacing(3)
                self.main_destination.setObjectName(u"main_destination")
                self.main_destination.setSizeConstraint(QLayout.SetFixedSize)
                self.main_destination.setContentsMargins(-1, 0, -1, 0)
                self.destination_spacer_haut = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

                self.main_destination.addItem(self.destination_spacer_haut)

                self.destination_1 = QLabel(self.Joueur)
                self.destination_1.setObjectName(u"destination_1")
                sizePolicy4.setHeightForWidth(self.destination_1.sizePolicy().hasHeightForWidth())
                self.destination_1.setSizePolicy(sizePolicy4)
                self.destination_1.setMinimumSize(QSize(100, 64))
                self.destination_1.setMaximumSize(QSize(100, 64))
                self.destination_1.setPixmap(QPixmap(u"img/boston_miami.jpg"))
                self.destination_1.setScaledContents(True)

                self.main_destination.addWidget(self.destination_1)

                self.destination_2 = QLabel(self.Joueur)
                self.destination_2.setObjectName(u"destination_2")
                sizePolicy6.setHeightForWidth(self.destination_2.sizePolicy().hasHeightForWidth())
                self.destination_2.setSizePolicy(sizePolicy6)
                self.destination_2.setMinimumSize(QSize(100, 64))
                self.destination_2.setMaximumSize(QSize(100, 64))
                self.destination_2.setPixmap(QPixmap(u"img/calgary_phoenix.jpg"))
                self.destination_2.setScaledContents(True)

                self.main_destination.addWidget(self.destination_2)

                self.destination_3 = QLabel(self.Joueur)
                self.destination_3.setObjectName(u"destination_3")
                sizePolicy6.setHeightForWidth(self.destination_3.sizePolicy().hasHeightForWidth())
                self.destination_3.setSizePolicy(sizePolicy6)
                self.destination_3.setMinimumSize(QSize(100, 64))
                self.destination_3.setMaximumSize(QSize(100, 64))
                self.destination_3.setPixmap(QPixmap(u"img/denver_el_paso.jpg"))
                self.destination_3.setScaledContents(True)

                self.main_destination.addWidget(self.destination_3)

                self.destination_spacer_bas = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

                self.main_destination.addItem(self.destination_spacer_bas)

                self.plateau_jeu.addLayout(self.main_destination)

                self.spacer_droit = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.plateau_jeu.addItem(self.spacer_droit)

                self.gridLayout_19.addLayout(self.plateau_jeu, 4, 0, 3, 7)

                self.pioche_wagon = QLabel(self.Joueur)
                self.pioche_wagon.setObjectName(u"pioche_wagon")
                self.pioche_wagon.setMinimumSize(QSize(100, 64))
                self.pioche_wagon.setPixmap(QPixmap(u"img/dos_wagon.jpg"))
                self.pioche_wagon.setScaledContents(False)
                self.pioche_wagon.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

                self.gridLayout_19.addWidget(self.pioche_wagon, 2, 0, 1, 1)

                self.titre_nom_joueur = QLabel(self.Joueur)
                self.titre_nom_joueur.setObjectName(u"titre_nom_joueur")
                sizePolicy1.setHeightForWidth(self.titre_nom_joueur.sizePolicy().hasHeightForWidth())
                self.titre_nom_joueur.setSizePolicy(sizePolicy1)
                self.titre_nom_joueur.setMinimumSize(QSize(471, 46))
                self.titre_nom_joueur.setStyleSheet(u"background-color:rgb(121, 255, 251);\n"
                                                    "border-radius:20;\n"
                                                    "border-color:rgb(50,50,50);\n"
                                                    "border-width:2;\n"
                                                    "border-style:solid;")
                self.titre_nom_joueur.setScaledContents(False)
                self.titre_nom_joueur.setAlignment(Qt.AlignCenter)

                self.gridLayout_19.addWidget(self.titre_nom_joueur, 1, 1, 1, 5)

                self.score_autre_joueurs = QHBoxLayout()
                self.score_autre_joueurs.setObjectName(u"score_autre_joueurs")
                self.autre_j1 = QLabel(self.Joueur)
                self.autre_j1.setObjectName(u"autre_j1")
                self.autre_j1.setStyleSheet(u"")
                self.autre_j1.setAlignment(Qt.AlignCenter)
                self.autre_j1.setWordWrap(True)

                self.score_autre_joueurs.addWidget(self.autre_j1)

                self.autre_j2 = QLabel(self.Joueur)
                self.autre_j2.setObjectName(u"autre_j2")
                self.autre_j2.setStyleSheet(u"")
                self.autre_j2.setAlignment(Qt.AlignCenter)
                self.autre_j2.setWordWrap(True)

                self.score_autre_joueurs.addWidget(self.autre_j2)

                self.autre_j3 = QLabel(self.Joueur)
                self.autre_j3.setObjectName(u"autre_j3")
                self.autre_j3.setStyleSheet(u"")
                self.autre_j3.setAlignment(Qt.AlignCenter)
                self.autre_j3.setWordWrap(True)

                self.score_autre_joueurs.addWidget(self.autre_j3)

                self.autre_j4 = QLabel(self.Joueur)
                self.autre_j4.setObjectName(u"autre_j4")
                self.autre_j4.setStyleSheet(u"")
                self.autre_j4.setAlignment(Qt.AlignCenter)
                self.autre_j4.setWordWrap(True)

                self.score_autre_joueurs.addWidget(self.autre_j4)

                self.gridLayout_19.addLayout(self.score_autre_joueurs, 2, 1, 1, 5)

                self.button_fin_tour = QPushButton(self.Joueur)
                self.button_fin_tour.setObjectName(u"button_fin_tour")

                self.gridLayout_19.addWidget(self.button_fin_tour, 1, 6, 1, 1)

                self.pioche_destination = QLabel(self.Joueur)
                self.pioche_destination.setObjectName(u"pioche_destination")
                self.pioche_destination.setMinimumSize(QSize(100, 64))
                self.pioche_destination.setPixmap(QPixmap(u"img/dos_destination.jpg"))
                self.pioche_destination.setScaledContents(False)
                self.pioche_destination.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

                self.gridLayout_19.addWidget(self.pioche_destination, 2, 6, 1, 1)

                self.stackedWidget.addWidget(self.Joueur)
                self.pioche_wagon.raise_()
                self.pioche_destination.raise_()
                self.titre_nom_joueur.raise_()
                self.score_joueur.raise_()
                self.button_fin_partie.raise_()
                self.button_fin_tour.raise_()
                self.Fin_partie = QWidget()
                self.Fin_partie.setObjectName(u"Fin_partie")
                self.Fin_partie.setStyleSheet(u"QWidget#Fin_partie{\n"
                                              "border-image:url(img/background_ticket_to_ride.jpg);\n"
                                              "background-repeat:no-repeat;\n"
                                              "background-position:center;\n"
                                              "}\n"
                                              "QPushButton{\n"
                                              "font:16pt;\n"
                                              "padding:2px;\n"
                                              "}")
                self.verticalLayout_9 = QVBoxLayout(self.Fin_partie)
                self.verticalLayout_9.setObjectName(u"verticalLayout_9")
                self.verticalLayout_9.setContentsMargins(55, 25, 55, 25)
                self.titre_fin_partie = QHBoxLayout()
                self.titre_fin_partie.setObjectName(u"titre_fin_partie")
                self.titre_spacer_gauche = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.titre_fin_partie.addItem(self.titre_spacer_gauche)

                self.label_titre = QLabel(self.Fin_partie)
                self.label_titre.setObjectName(u"label_titre")
                font5 = QFont()
                font5.setFamily(u"chippewafallsnf")
                font5.setPointSize(28)
                font5.setBold(False)
                font5.setItalic(False)
                font5.setWeight(50)
                self.label_titre.setFont(font5)
                self.label_titre.setStyleSheet(u"font:28pt \"chippewafallsnf\";\n"
                                               "")
                self.label_titre.setAlignment(Qt.AlignCenter)

                self.titre_fin_partie.addWidget(self.label_titre)

                self.titre_spacer_droit = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.titre_fin_partie.addItem(self.titre_spacer_droit)

                self.verticalLayout_9.addLayout(self.titre_fin_partie)

                self.spacer_haut = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Preferred)

                self.verticalLayout_9.addItem(self.spacer_haut)

                self.score_final = QHBoxLayout()
                self.score_final.setObjectName(u"score_final")
                self.score_spacer_gauche = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.score_final.addItem(self.score_spacer_gauche)

                self.position_joueur = QVBoxLayout()
                self.position_joueur.setSpacing(20)
                self.position_joueur.setObjectName(u"position_joueur")
                self.label_resultat1 = QLabel(self.Fin_partie)
                self.label_resultat1.setObjectName(u"label_resultat1")
                font6 = QFont()
                font6.setFamily(u"ShangriLaNFSmallCaps")
                font6.setPointSize(12)
                font6.setBold(False)
                font6.setItalic(False)
                font6.setWeight(50)
                self.label_resultat1.setFont(font6)

                self.position_joueur.addWidget(self.label_resultat1)

                self.label_resultat2 = QLabel(self.Fin_partie)
                self.label_resultat2.setObjectName(u"label_resultat2")
                self.label_resultat2.setFont(font6)

                self.position_joueur.addWidget(self.label_resultat2)

                self.label_resultat3 = QLabel(self.Fin_partie)
                self.label_resultat3.setObjectName(u"label_resultat3")
                self.label_resultat3.setFont(font6)

                self.position_joueur.addWidget(self.label_resultat3)

                self.label_resultat4 = QLabel(self.Fin_partie)
                self.label_resultat4.setObjectName(u"label_resultat4")
                self.label_resultat4.setFont(font6)

                self.position_joueur.addWidget(self.label_resultat4)

                self.label_resultat5 = QLabel(self.Fin_partie)
                self.label_resultat5.setObjectName(u"label_resultat5")
                self.label_resultat5.setFont(font6)

                self.position_joueur.addWidget(self.label_resultat5)

                self.score_final.addLayout(self.position_joueur)

                self.score_spacer_droit = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.score_final.addItem(self.score_spacer_droit)

                self.verticalLayout_9.addLayout(self.score_final)

                self.spacer_bas = QSpacerItem(20, 127, QSizePolicy.Minimum, QSizePolicy.Expanding)

                self.verticalLayout_9.addItem(self.spacer_bas)

                self.buttons_fin_partie = QHBoxLayout()
                self.buttons_fin_partie.setObjectName(u"buttons_fin_partie")
                self.button_statistiques = QPushButton(self.Fin_partie)
                self.button_statistiques.setObjectName(u"button_statistiques")

                self.buttons_fin_partie.addWidget(self.button_statistiques)

                self.buttons_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.buttons_fin_partie.addItem(self.buttons_spacer)

                self.button_nouvelle_partie_3 = QPushButton(self.Fin_partie)
                self.button_nouvelle_partie_3.setObjectName(u"button_nouvelle_partie_3")

                self.buttons_fin_partie.addWidget(self.button_nouvelle_partie_3)

                self.button_menu = QPushButton(self.Fin_partie)
                self.button_menu.setObjectName(u"button_menu")

                self.buttons_fin_partie.addWidget(self.button_menu)

                self.verticalLayout_9.addLayout(self.buttons_fin_partie)

                self.stackedWidget.addWidget(self.Fin_partie)
                self.Statistiques = QWidget()
                self.Statistiques.setObjectName(u"Statistiques")
                self.verticalLayout_4 = QVBoxLayout(self.Statistiques)
                self.verticalLayout_4.setObjectName(u"verticalLayout_4")
                self.titre_statistiques = QHBoxLayout()
                self.titre_statistiques.setObjectName(u"titre_statistiques")
                self.titre_stats_pacer_gauche = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.titre_statistiques.addItem(self.titre_stats_pacer_gauche)

                self.label_titre_stats = QLabel(self.Statistiques)
                self.label_titre_stats.setObjectName(u"label_titre_stats")
                self.label_titre_stats.setFont(font5)
                self.label_titre_stats.setStyleSheet(u"font: 28pt \"chippewafallsnf\";")
                self.label_titre_stats.setAlignment(Qt.AlignCenter)

                self.titre_statistiques.addWidget(self.label_titre_stats)

                self.titre_stats_spacer_droit = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.titre_statistiques.addItem(self.titre_stats_spacer_droit)

                self.verticalLayout_4.addLayout(self.titre_statistiques)

                self.spacer_bas_2 = QSpacerItem(20, 140, QSizePolicy.Minimum, QSizePolicy.Preferred)

                self.verticalLayout_4.addItem(self.spacer_bas_2)

                self.table_stats = QTableView(self.Statistiques)
                self.table_stats.setObjectName(u"table_stats")

                self.verticalLayout_4.addWidget(self.table_stats)

                self.spacer_haut_2 = QSpacerItem(20, 140, QSizePolicy.Minimum, QSizePolicy.Preferred)

                self.verticalLayout_4.addItem(self.spacer_haut_2)

                self.layout_buttons_stats = QHBoxLayout()
                self.layout_buttons_stats.setObjectName(u"layout_buttons_stats")
                self.button_menu_principal = QPushButton(self.Statistiques)
                self.button_menu_principal.setObjectName(u"button_menu_principal")

                self.layout_buttons_stats.addWidget(self.button_menu_principal)

                self.buttons_spacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.layout_buttons_stats.addItem(self.buttons_spacer_5)

                self.button_nouvelle_partie_6 = QPushButton(self.Statistiques)
                self.button_nouvelle_partie_6.setObjectName(u"button_nouvelle_partie_6")

                self.layout_buttons_stats.addWidget(self.button_nouvelle_partie_6)

                self.button_retour_4 = QPushButton(self.Statistiques)
                self.button_retour_4.setObjectName(u"button_retour_4")

                self.layout_buttons_stats.addWidget(self.button_retour_4)

                self.verticalLayout_4.addLayout(self.layout_buttons_stats)

                self.stackedWidget.addWidget(self.Statistiques)
                self.Options = QWidget()
                self.Options.setObjectName(u"Options")
                self.Options.setStyleSheet(u"QWidget#Options{\n"
                                           "border-image:url(img/background_ticket_to_ride.jpg);\n"
                                           "background-repeat:no-repeat;\n"
                                           "background-position:center;\n"
                                           "}")
                self.verticalLayout_2 = QVBoxLayout(self.Options)
                self.verticalLayout_2.setObjectName(u"verticalLayout_2")
                self.verticalLayout_2.setContentsMargins(55, 25, 55, 25)
                self.titre_options = QHBoxLayout()
                self.titre_options.setObjectName(u"titre_options")
                self.titre_spacer_gauche_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.titre_options.addItem(self.titre_spacer_gauche_2)

                self.label_titre_options = QLabel(self.Options)
                self.label_titre_options.setObjectName(u"label_titre_options")
                self.label_titre_options.setFont(font5)
                self.label_titre_options.setStyleSheet(u"font: 28pt \"chippewafallsnf\";")
                self.label_titre_options.setAlignment(Qt.AlignCenter)

                self.titre_options.addWidget(self.label_titre_options)

                self.titre_spacer_droit_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.titre_options.addItem(self.titre_spacer_droit_2)

                self.verticalLayout_2.addLayout(self.titre_options)

                self.options_spacer_haut = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

                self.verticalLayout_2.addItem(self.options_spacer_haut)

                self.layout_options = QHBoxLayout()
                self.layout_options.setObjectName(u"layout_options")
                self.layout_options.setContentsMargins(60, -1, 60, -1)
                self.label_idee_options = QLabel(self.Options)
                self.label_idee_options.setObjectName(u"label_idee_options")
                self.label_idee_options.setFont(font6)
                self.label_idee_options.setWordWrap(True)

                self.layout_options.addWidget(self.label_idee_options)

                self.verticalLayout_2.addLayout(self.layout_options)

                self.options_spacer_bas = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

                self.verticalLayout_2.addItem(self.options_spacer_bas)

                self.buttons_options = QHBoxLayout()
                self.buttons_options.setObjectName(u"buttons_options")
                self.button_credits_3 = QPushButton(self.Options)
                self.button_credits_3.setObjectName(u"button_credits_3")

                self.buttons_options.addWidget(self.button_credits_3)

                self.buttons_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.buttons_options.addItem(self.buttons_spacer_2)

                self.button_nouvelle_partie_4 = QPushButton(self.Options)
                self.button_nouvelle_partie_4.setObjectName(u"button_nouvelle_partie_4")

                self.buttons_options.addWidget(self.button_nouvelle_partie_4)

                self.button_retour_2 = QPushButton(self.Options)
                self.button_retour_2.setObjectName(u"button_retour_2")

                self.buttons_options.addWidget(self.button_retour_2)

                self.verticalLayout_2.addLayout(self.buttons_options)

                self.stackedWidget.addWidget(self.Options)
                self.Credits = QWidget()
                self.Credits.setObjectName(u"Credits")
                self.Credits.setStyleSheet(u"QWidget#Credits{\n"
                                           "border-image:url(img/background_ticket_to_ride.jpg);\n"
                                           "background-repeat:no-repeat;\n"
                                           "background-position:center;\n"
                                           "}")
                self.verticalLayout_3 = QVBoxLayout(self.Credits)
                self.verticalLayout_3.setObjectName(u"verticalLayout_3")
                self.verticalLayout_3.setContentsMargins(55, 25, 55, 25)
                self.titre_credits = QHBoxLayout()
                self.titre_credits.setObjectName(u"titre_credits")
                self.titre_spacer_gauche_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.titre_credits.addItem(self.titre_spacer_gauche_3)

                self.label_titre_credits = QLabel(self.Credits)
                self.label_titre_credits.setObjectName(u"label_titre_credits")
                self.label_titre_credits.setFont(font5)
                self.label_titre_credits.setStyleSheet(u"font:28pt \"chippewafallsnf\";")
                self.label_titre_credits.setAlignment(Qt.AlignCenter)

                self.titre_credits.addWidget(self.label_titre_credits)

                self.titre_spacer_droit_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.titre_credits.addItem(self.titre_spacer_droit_3)

                self.verticalLayout_3.addLayout(self.titre_credits)

                self.credits_spacer_haut = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

                self.verticalLayout_3.addItem(self.credits_spacer_haut)

                self.layout_credits = QHBoxLayout()
                self.layout_credits.setObjectName(u"layout_credits")
                self.layout_credits.setContentsMargins(60, -1, 60, -1)
                self.label_credits = QLabel(self.Credits)
                self.label_credits.setObjectName(u"label_credits")
                self.label_credits.setFont(font6)
                self.label_credits.setStyleSheet(u"font:12pt \"ShangriLaNFSmallCaps\";")
                self.label_credits.setWordWrap(True)

                self.layout_credits.addWidget(self.label_credits)

                self.verticalLayout_3.addLayout(self.layout_credits)

                self.credits_spacer_bas = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Expanding)

                self.verticalLayout_3.addItem(self.credits_spacer_bas)

                self.buttons_credits = QHBoxLayout()
                self.buttons_credits.setObjectName(u"buttons_credits")
                self.buttons_spacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.buttons_credits.addItem(self.buttons_spacer_3)

                self.button_retour_3 = QPushButton(self.Credits)
                self.button_retour_3.setObjectName(u"button_retour_3")

                self.buttons_credits.addWidget(self.button_retour_3)

                self.verticalLayout_3.addLayout(self.buttons_credits)

                self.stackedWidget.addWidget(self.Credits)

                self.verticalLayout.addWidget(self.stackedWidget)

                MainWindow.setCentralWidget(self.centralwidget)
                # if QT_CONFIG(shortcut)
                self.label_nb_joueurs_tot.setBuddy(self.spinbox_nb_joueurs_tot)
                self.label_nb_joueurs_ia.setBuddy(self.spinbox_nb_joueurs_ia)
                # endif // QT_CONFIG(shortcut)

                self.retranslateUi(MainWindow)
                self.actionQuitter.triggered.connect(MainWindow.close)

                self.stackedWidget.setCurrentIndex(0)

                QMetaObject.connectSlotsByName(MainWindow)

        # setupUi

        def retranslateUi(self, MainWindow):
                MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Les aventuriers du rail", None))
                self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
                # if QT_CONFIG(shortcut)
                self.actionQuitter.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
                # endif // QT_CONFIG(shortcut)
                self.actionRegles_du_jeu.setText(QCoreApplication.translate("MainWindow", u"R\u00e8gles du jeu", None))
                # if QT_CONFIG(shortcut)
                self.actionRegles_du_jeu.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
                # endif // QT_CONFIG(shortcut)
                self.actionOptions.setText(QCoreApplication.translate("MainWindow", u"Options", None))
                # if QT_CONFIG(shortcut)
                self.actionOptions.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
                # endif // QT_CONFIG(shortcut)
                self.button_options.setText(QCoreApplication.translate("MainWindow", u"Options", None))
                self.button_credits.setText(QCoreApplication.translate("MainWindow", u"Credits", None))
                self.button_regles_jeu.setText(QCoreApplication.translate("MainWindow", u"Règles du jeu", None))
                self.button_nouvelle_partie.setText(QCoreApplication.translate("MainWindow", u"Nouvelle Partie", None))
                self.choix_IA2.setItemText(0, QCoreApplication.translate("MainWindow", u"IA novice", None))
                self.choix_IA2.setItemText(1, QCoreApplication.translate("MainWindow", u"IA normal", None))
                self.choix_IA2.setItemText(2, QCoreApplication.translate("MainWindow", u"IA expert", None))
                self.choix_IA2.setItemText(3, QCoreApplication.translate("MainWindow", u"IA al\u00e9atoire", None))

                self.label_difficulty5.setText(QCoreApplication.translate("MainWindow", u"Difficult\u00e9 IA 5", None))
                self.titre_nouvelle_partie.setText(QCoreApplication.translate("MainWindow", u"Nouvelle Partie", None))
                self.choix_IA4.setItemText(0, QCoreApplication.translate("MainWindow", u"IA novice", None))
                self.choix_IA4.setItemText(1, QCoreApplication.translate("MainWindow", u"IA normal", None))
                self.choix_IA4.setItemText(2, QCoreApplication.translate("MainWindow", u"IA expert", None))
                self.choix_IA4.setItemText(3, QCoreApplication.translate("MainWindow", u"IA al\u00e9atoire", None))

                self.label_couleur1.setText(QCoreApplication.translate("MainWindow", u"Couleur du joueur 1", None))
                self.label_nom1.setText(QCoreApplication.translate("MainWindow", u"Nom du joueur 1", None))
                self.input_couleur1.setItemText(0, QCoreApplication.translate("MainWindow", u"bleu", None))
                self.input_couleur1.setItemText(1, QCoreApplication.translate("MainWindow", u"rouge", None))
                self.input_couleur1.setItemText(2, QCoreApplication.translate("MainWindow", u"vert", None))
                self.input_couleur1.setItemText(3, QCoreApplication.translate("MainWindow", u"jaune", None))
                self.input_couleur1.setItemText(4, QCoreApplication.translate("MainWindow", u"orange", None))
                self.input_couleur1.setItemText(5, QCoreApplication.translate("MainWindow", u"random", None))
                self.input_couleur1.setItemText(6,
                                                QCoreApplication.translate("MainWindow", u"personnalis\u00e9e", None))

                self.label_nom2.setText(QCoreApplication.translate("MainWindow", u"Nom du joueur 1", None))
                self.label_couleur2.setText(QCoreApplication.translate("MainWindow", u"Couleur du joueur 1", None))
                self.input_couleur2.setItemText(0, QCoreApplication.translate("MainWindow", u"bleu", None))
                self.input_couleur2.setItemText(1, QCoreApplication.translate("MainWindow", u"rouge", None))
                self.input_couleur2.setItemText(2, QCoreApplication.translate("MainWindow", u"vert", None))
                self.input_couleur2.setItemText(3, QCoreApplication.translate("MainWindow", u"jaune", None))
                self.input_couleur2.setItemText(4, QCoreApplication.translate("MainWindow", u"orange", None))
                self.input_couleur2.setItemText(5, QCoreApplication.translate("MainWindow", u"random", None))
                self.input_couleur2.setItemText(6,
                                                QCoreApplication.translate("MainWindow", u"personnalis\u00e9e", None))

                self.choix_IA1.setItemText(0, QCoreApplication.translate("MainWindow", u"IA novice", None))
                self.choix_IA1.setItemText(1, QCoreApplication.translate("MainWindow", u"IA normal", None))
                self.choix_IA1.setItemText(2, QCoreApplication.translate("MainWindow", u"IA expert", None))
                self.choix_IA1.setItemText(3, QCoreApplication.translate("MainWindow", u"IA al\u00e9atoire", None))

                self.label_nb_joueurs_tot.setText(
                        QCoreApplication.translate("MainWindow", u"Nombre de joueurs pour la partie", None))
                self.label_nb_joueurs_ia.setText(
                        QCoreApplication.translate("MainWindow", u"Nombre de joueurs IAs", None))
                self.choix_IA5.setItemText(0, QCoreApplication.translate("MainWindow", u"IA novice", None))
                self.choix_IA5.setItemText(1, QCoreApplication.translate("MainWindow", u"IA normal", None))
                self.choix_IA5.setItemText(2, QCoreApplication.translate("MainWindow", u"IA expert", None))
                self.choix_IA5.setItemText(3, QCoreApplication.translate("MainWindow", u"IA al\u00e9atoire", None))

                self.label_nom3.setText(QCoreApplication.translate("MainWindow", u"Nom du joueur 1", None))
                self.label_couleur3.setText(QCoreApplication.translate("MainWindow", u"Couleur du joueur 1", None))
                self.input_couleur3.setItemText(0, QCoreApplication.translate("MainWindow", u"bleu", None))
                self.input_couleur3.setItemText(1, QCoreApplication.translate("MainWindow", u"rouge", None))
                self.input_couleur3.setItemText(2, QCoreApplication.translate("MainWindow", u"vert", None))
                self.input_couleur3.setItemText(3, QCoreApplication.translate("MainWindow", u"jaune", None))
                self.input_couleur3.setItemText(4, QCoreApplication.translate("MainWindow", u"orange", None))
                self.input_couleur3.setItemText(5, QCoreApplication.translate("MainWindow", u"random", None))
                self.input_couleur3.setItemText(6,
                                                QCoreApplication.translate("MainWindow", u"personnalis\u00e9e", None))

                self.label_difficulty1.setText(QCoreApplication.translate("MainWindow", u"Difficult\u00e9 IA 1", None))
                self.label_difficulty4.setText(QCoreApplication.translate("MainWindow", u"Difficult\u00e9 IA 4", None))
                self.label_difficulty3.setText(QCoreApplication.translate("MainWindow", u"Difficult\u00e9 IA 3", None))
                self.label_difficulty2.setText(QCoreApplication.translate("MainWindow", u"Difficult\u00e9 IA 2", None))
                self.choix_IA3.setItemText(0, QCoreApplication.translate("MainWindow", u"IA novice", None))
                self.choix_IA3.setItemText(1, QCoreApplication.translate("MainWindow", u"IA normal", None))
                self.choix_IA3.setItemText(2, QCoreApplication.translate("MainWindow", u"IA expert", None))
                self.choix_IA3.setItemText(3, QCoreApplication.translate("MainWindow", u"IA al\u00e9atoire", None))

                self.label_nom5.setText(QCoreApplication.translate("MainWindow", u"Nom du joueur 1", None))
                self.label_couleur5.setText(QCoreApplication.translate("MainWindow", u"Couleur du joueur 1", None))
                self.input_couleur5.setItemText(0, QCoreApplication.translate("MainWindow", u"bleu", None))
                self.input_couleur5.setItemText(1, QCoreApplication.translate("MainWindow", u"rouge", None))
                self.input_couleur5.setItemText(2, QCoreApplication.translate("MainWindow", u"vert", None))
                self.input_couleur5.setItemText(3, QCoreApplication.translate("MainWindow", u"jaune", None))
                self.input_couleur5.setItemText(4, QCoreApplication.translate("MainWindow", u"orange", None))
                self.input_couleur5.setItemText(5, QCoreApplication.translate("MainWindow", u"random", None))
                self.input_couleur5.setItemText(6,
                                                QCoreApplication.translate("MainWindow", u"personnalis\u00e9e", None))

                self.label_nom4.setText(QCoreApplication.translate("MainWindow", u"Nom du joueur 1", None))
                self.label_couleur4.setText(QCoreApplication.translate("MainWindow", u"Couleur du joueur 1", None))
                self.input_couleur4.setItemText(0, QCoreApplication.translate("MainWindow", u"bleu", None))
                self.input_couleur4.setItemText(1, QCoreApplication.translate("MainWindow", u"rouge", None))
                self.input_couleur4.setItemText(2, QCoreApplication.translate("MainWindow", u"vert", None))
                self.input_couleur4.setItemText(3, QCoreApplication.translate("MainWindow", u"jaune", None))
                self.input_couleur4.setItemText(4, QCoreApplication.translate("MainWindow", u"orange", None))
                self.input_couleur4.setItemText(5, QCoreApplication.translate("MainWindow", u"random", None))
                self.input_couleur4.setItemText(6,
                                                QCoreApplication.translate("MainWindow", u"personnalis\u00e9e", None))

                self.button_commencer.setText(QCoreApplication.translate("MainWindow", u"Commencer", None))
                self.button_retour.setText(QCoreApplication.translate("MainWindow", u"Retour", None))
                self.label_voyageur.setText(
                        QCoreApplication.translate("MainWindow", u"Qui a le plus voyag\u00e9 entre ces joueurs ?",
                                                   None))
                self.selection_voyageur.setItemText(0, "")
                self.selection_voyageur.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                                  u"Ajouter le nom des joueurs dynamiquement",
                                                                                  None))

                self.score_joueur.setText(QCoreApplication.translate("MainWindow", u"0", None))
                self.main_wagon1.setText("")
                self.main_wagon2.setText("")
                self.main_wagon3.setText("")
                self.main_wagon4.setText("")
                self.main_wagon5.setText("")
                self.main_wagon6.setText("")
                self.main_wagon7.setText("")
                self.main_wagon8.setText("")
                self.main_wagon9.setText("")
                self.label_interaction_joueur.setText(
                        QCoreApplication.translate("MainWindow", u"Interaction avec le joueur", None))
                self.button_take_road.setText(QCoreApplication.translate("MainWindow", u"Prendre une route", None))
                self.button_fin_partie.setText(QCoreApplication.translate("MainWindow", u"Fin de partie", None))
                self.wagon1.setText("")
                self.wagon2.setText("")
                self.wagon3.setText("")
                self.wagon4.setText("")
                self.wagon5.setText("")
                self.destination_1.setText("")
                self.destination_2.setText("")
                self.destination_3.setText("")
                self.pioche_wagon.setText("")
                self.titre_nom_joueur.setText(
                        QCoreApplication.translate("MainWindow", u"Nom du joueur - Tour n\u00b0X", None))
                self.autre_j1.setText(QCoreApplication.translate("MainWindow", u"Nom_joueur : X pts", None))
                self.autre_j2.setText(QCoreApplication.translate("MainWindow", u"Nom_joueur : X pts", None))
                self.autre_j3.setText(QCoreApplication.translate("MainWindow", u"Nom_joueur : X pts", None))
                self.autre_j4.setText(QCoreApplication.translate("MainWindow", u"Nom_joueur : X pts", None))
                self.button_fin_tour.setText(QCoreApplication.translate("MainWindow", u"Fin du tour", None))
                self.pioche_destination.setText("")
                self.label_titre.setText(
                        QCoreApplication.translate("MainWindow", u"Fin de partie - R\u00e9sultats", None))
                self.label_resultat1.setText(
                        QCoreApplication.translate("MainWindow", u"Position : Nom joueur 1 - Score final", None))
                self.label_resultat2.setText(
                        QCoreApplication.translate("MainWindow", u"Position : Nom joueur 2 - Score final", None))
                self.label_resultat3.setText(
                        QCoreApplication.translate("MainWindow", u"Position : Nom joueur 3 - Score final", None))
                self.label_resultat4.setText(
                        QCoreApplication.translate("MainWindow", u"Position : Nom joueur 4 - Score final", None))
                self.label_resultat5.setText(
                        QCoreApplication.translate("MainWindow", u"Position : Nom joueur 5 - Score final", None))
                self.button_statistiques.setText(QCoreApplication.translate("MainWindow", u"Statistiques", None))
                self.button_nouvelle_partie_3.setText(
                        QCoreApplication.translate("MainWindow", u"Nouvelle Partie", None))
                self.button_menu.setText(QCoreApplication.translate("MainWindow", u"Menu principal", None))
                self.label_titre_stats.setText(
                        QCoreApplication.translate("MainWindow", u"Statistiques de partie", None))
                self.button_menu_principal.setText(QCoreApplication.translate("MainWindow", u"Menu principal", None))
                self.button_nouvelle_partie_6.setText(
                        QCoreApplication.translate("MainWindow", u"Nouvelle Partie", None))
                self.button_retour_4.setText(QCoreApplication.translate("MainWindow", u"Retour", None))
                self.label_titre_options.setText(QCoreApplication.translate("MainWindow", u"Options du jeu", None))
                self.label_idee_options.setText(QCoreApplication.translate("MainWindow",
                                                                           u"Id\u00e9e d'options : color picker pour couleur, "
                                                                           u"param par d\u00e9faut pour nouvelle partie, "
                                                                           u"param par d\u00e9faut pour IA, ...",
                                                                           None))
                self.button_credits_3.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9dits", None))
                self.button_nouvelle_partie_4.setText(
                        QCoreApplication.translate("MainWindow", u"Nouvelle Partie", None))
                self.button_retour_2.setText(QCoreApplication.translate("MainWindow", u"Retour", None))
                self.label_titre_credits.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9dits du jeu", None))
                self.label_credits.setText(QCoreApplication.translate("MainWindow",
                                                                      u"Nous sommes 2 \u00e9tudiants ing\u00e9nieur en "
                                                                      u"premi\u00e8re ann\u00e9e \u00e0 l'ENSTA Bretagne, "
                                                                      u"\u00e9cole d'ing\u00e9nieurs pluridisciplinaires "
                                                                      u"situ\u00e9 \u00e0 Brest. \n "
                                                                      " Dans le cadre d'un projet informatique de fin "
                                                                      "d'ann\u00e9e, nous avons r\u00e9alis\u00e9 ce jeu afin "
                                                                      "de mettre en pratique nos connaissances acquises en "
                                                                      "programmation orient\u00e9e objet et Python. \n "
                                                                      " Par ailleurs, la propri\u00e9t\u00e9 intellectuelle "
                                                                      "du jeu revient aux cr\u00e9ateurs. Nous avons "
                                                                      "tent\u00e9 de reprendre le maximum de r\u00e8gles dans "
                                                                      "notre jeu. Cependant, des fonctionnalit\u00e9s peuvent "
                                                                      "manquer pour cause de difficult\u00e9 "
                                                                      "d'impl\u00e9mentation.\n "
                                                                      "En vous souhaitant une agr\u00e9able partie, \n"
                                                                      "Bon jeu !\n"
                                                                      " \n"
                                                                      " Mathis URIEN & Kenza BELA\u00cfD", None))
                self.button_retour_3.setText(QCoreApplication.translate("MainWindow", u"Retour", None))
        # retranslateUi


if __name__ == '__main__':
        import sys

        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
