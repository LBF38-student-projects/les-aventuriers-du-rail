#  Copyright (c) 2022. Authors: Mathis URIEN

# Imports :
import unittest
import Partie
from Joueur import Joueur, IA_player
from Score import Score


class TestPartieQt(unittest.TestCase):
    def setUp(self) -> None:
        self.partie = Partie.Partie_qt()
        self.joueur_ia = IA_player()
        self.joueur = Joueur()

    def testJeu(self):
        """
        Test sur les propriétés et méthodes de Jeu
        """
        pass


def test_melange_americain():
    assert False
