# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choix_routeWCYGHh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class Ui_take_road(object):
    def setupUi(self, take_road):
        if take_road.objectName():
            take_road.setObjectName(u"take_road")
        take_road.resize(648, 309)
        take_road.setStyleSheet(u"QPushButton{\n"
                                "font: 12pt \"chippewafallsnf\";\n"
                                "background-color:lightgrey;\n"
                                "border-style: outset;\n"
                                "border-width: 2px;\n"
                                "border-radius: 10px;\n"
                                "border-color: grey;\n"
                                "padding: 1px 3px 1px 3px;\n"
                                "}\n"
                                "QLabel{\n"
                                "font:8pt \"ShangriLaNFSmallCaps\";\n"
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
                                "}")
        self.verticalLayout = QVBoxLayout(take_road)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_title = QHBoxLayout()
        self.layout_title.setObjectName(u"layout_title")
        self.spacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_title.addItem(self.spacer_left)

        self.label_title = QLabel(take_road)
        self.label_title.setObjectName(u"label_title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMinimumSize(QSize(104, 20))
        self.label_title.setStyleSheet(u"font: 24pt \"chippewafallsnf\";\n"
                                       "")

        self.layout_title.addWidget(self.label_title)

        self.spacer_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_title.addItem(self.spacer_right)

        self.verticalLayout.addLayout(self.layout_title)

        self.layout_road = QHBoxLayout()
        self.layout_road.setObjectName(u"layout_road")
        self.label_road = QLabel(take_road)
        self.label_road.setObjectName(u"label_road")

        self.layout_road.addWidget(self.label_road)

        self.spacer_road = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.layout_road.addItem(self.spacer_road)

        self.choose_road = QComboBox(take_road)
        self.choose_road.addItem("")
        self.choose_road.addItem("")
        self.choose_road.setObjectName(u"choose_road")
        self.choose_road.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.layout_road.addWidget(self.choose_road)

        self.verticalLayout.addLayout(self.layout_road)

        self.layout_wagons = QHBoxLayout()
        self.layout_wagons.setObjectName(u"layout_wagons")
        self.label_wagons = QLabel(take_road)
        self.label_wagons.setObjectName(u"label_wagons")

        self.layout_wagons.addWidget(self.label_wagons)

        self.spacer_wagons = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.layout_wagons.addItem(self.spacer_wagons)

        self.choose_wagons = QComboBox(take_road)
        self.choose_wagons.addItem("")
        self.choose_wagons.addItem("")
        self.choose_wagons.setObjectName(u"choose_wagons")

        self.layout_wagons.addWidget(self.choose_wagons)

        self.verticalLayout.addLayout(self.layout_wagons)

        self.layout_locomotive = QHBoxLayout()
        self.layout_locomotive.setObjectName(u"layout_locomotive")
        self.label_locomotive = QLabel(take_road)
        self.label_locomotive.setObjectName(u"label_locomotive")

        self.layout_locomotive.addWidget(self.label_locomotive)

        self.spacer_locomotive = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.layout_locomotive.addItem(self.spacer_locomotive)

        self.choose_locomotive = QComboBox(take_road)
        self.choose_locomotive.addItem("")
        self.choose_locomotive.addItem("")
        self.choose_locomotive.addItem("")
        self.choose_locomotive.setObjectName(u"choose_locomotive")

        self.layout_locomotive.addWidget(self.choose_locomotive)

        self.verticalLayout.addLayout(self.layout_locomotive)

        self.layout_nb_locomotive = QHBoxLayout()
        self.layout_nb_locomotive.setObjectName(u"layout_nb_locomotive")
        self.label_nb_locomotive = QLabel(take_road)
        self.label_nb_locomotive.setObjectName(u"label_nb_locomotive")

        self.layout_nb_locomotive.addWidget(self.label_nb_locomotive)

        self.spacer_locomotive_2 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.layout_nb_locomotive.addItem(self.spacer_locomotive_2)

        self.spinbox_nb_locomotive = QSpinBox(take_road)
        self.spinbox_nb_locomotive.setObjectName(u"spinbox_nb_locomotive")

        self.layout_nb_locomotive.addWidget(self.spinbox_nb_locomotive)

        self.verticalLayout.addLayout(self.layout_nb_locomotive)

        self.dialog_buttons = QDialogButtonBox(take_road)
        self.dialog_buttons.setObjectName(u"dialog_buttons")
        self.dialog_buttons.setOrientation(Qt.Horizontal)
        self.dialog_buttons.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.dialog_buttons)

        self.retranslateUi(take_road)
        self.dialog_buttons.accepted.connect(take_road.accept)
        self.dialog_buttons.rejected.connect(take_road.reject)

        QMetaObject.connectSlotsByName(take_road)

    # setupUi

    def retranslateUi(self, take_road):
        take_road.setWindowTitle(
            QCoreApplication.translate("take_road", u"Les aventuriers du rail - Choix d'une route", None))
        self.label_title.setText(QCoreApplication.translate("take_road", u"Prendre une route", None))
        self.label_road.setText(QCoreApplication.translate("take_road", u"Quelle route voulez-vous prendre ?", None))
        self.choose_road.setItemText(0, QCoreApplication.translate("take_road", u"Choisissez votre route", None))
        self.choose_road.setItemText(1, QCoreApplication.translate("take_road", u"Los Angeles - New York", None))

        self.label_wagons.setText(QCoreApplication.translate("take_road", u"La route est grise. \n"
                                                                          "Avec quel wagon voulez-vous la prendre ?",
                                                             None))
        self.choose_wagons.setItemText(0, QCoreApplication.translate("take_road", u"Choisissez le type de wagon", None))
        self.choose_wagons.setItemText(1, QCoreApplication.translate("take_road", u"bleu", None))

        self.label_locomotive.setText(
            QCoreApplication.translate("take_road", u"Vous n'avez pas assez de wagons {couleur}. \n"
                                                    "Voulez-vous compl\u00e9ter avec des locomotives ?", None))
        self.choose_locomotive.setItemText(0, QCoreApplication.translate("take_road", u"Choisissez votre r\u00e9ponse",
                                                                         None))
        self.choose_locomotive.setItemText(1, QCoreApplication.translate("take_road", u"Oui", None))
        self.choose_locomotive.setItemText(2, QCoreApplication.translate("take_road", u"Non", None))

        self.label_nb_locomotive.setText(
            QCoreApplication.translate("take_road", u"Combien de wagons locomotives voulez-vous utiliser ?", None))
    # retranslateUi
