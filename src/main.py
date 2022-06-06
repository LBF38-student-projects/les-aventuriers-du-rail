"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

import os
from pip._internal import main as pipmain

# TODO: installer les fonts si celles-ci ne le sont pas sur le PC actuel.
if __name__ == '__main__':
    try:
        # Installing fonts for the app
        # from fontTools.ttLib import TTFont
        # font1 = TTFont("fonts/ChippewaFallsNF.ttf")
        # font2 = TTFont("fonts/FREEBSCA.ttf")
        # font3 = TTFont("fonts/SHANLNC_.TTF")
        # Path to save : C:\WINDOWS\FONTS\CHIPPEWAFALLSNF.TTF
        # font1.save("C:\WINDOWS\FONTS\CHIPPEWAFALLSNF.TTF")

        from interfaceQt import *

        app = QApplication()
        window = MonAppli()
        window.show()
        app.exec_()

    except ModuleNotFoundError as module:
        print(module)

        pipmain(['install', 'PySide2'])
        pipmain(["install", "font-installer"])

        from interfaceQt import *

        app = QApplication()
        window = MonAppli()
        window.show()
        app.exec_()
