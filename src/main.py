"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

from pip._internal import main as pipmain

# pipmain()

# TODO: installer les fonts si celles-ci ne le sont pas sur le PC actuel.
if __name__ == '__main__':
    try:
        from interfaceQt import *

        app = QApplication()
        window = MonAppli()
        window.show()
        app.exec_()
    except ModuleNotFoundError as module:
        print(module)

        pipmain(['install', 'PySide2'])

        from interfaceQt import *

        app = QApplication()
        window = MonAppli()
        window.show()
        app.exec_()
