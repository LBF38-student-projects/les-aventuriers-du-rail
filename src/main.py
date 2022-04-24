"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

# Imports :
from Partie import Partie
from Jeu import Jeu
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.show(Jeu().plateau())
    p=Partie()
    p.partie()

