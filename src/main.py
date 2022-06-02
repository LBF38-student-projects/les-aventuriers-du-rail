"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""


if __name__ == '__main__':
    try:
        from interfaceQt import *

        app = QApplication()
        window = MonAppli()
        window.show()
        app.exec_()
    except ModuleNotFoundError as module:
        print(module)
        from pip._internal import main as pipmain

        pipmain(['install', 'PySide2'])

        from interfaceQt import *

        app = QApplication()
        window = MonAppli()
        window.show()
        app.exec_()
