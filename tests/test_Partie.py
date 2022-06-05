#  Copyright (c) 2022. Authors: Mathis URIEN

# Imports :
import sys

sys.path.insert(0, "../src/")
import unittest
from Partie import Partie_qt
from Joueur import Joueur, IA_player


class TestPartieQt(unittest.TestCase):
    def setUp(self) -> None:
        self.partie = Partie_qt()
        self.joueur_ia = IA_player()
        self.joueur = Joueur("JoueurTest", "bleu")

    def testInstance(self):
        """
        Test le setUp.
        """
        self.assertIsInstance(self.partie, Partie_qt)
        self.assertIsInstance(self.joueur_ia, IA_player)
        self.assertIsInstance(self.joueur_ia, Joueur)
        self.assertIsInstance(self.joueur, Joueur)

    def testJeu(self):
        """
        Test sur les propriétés et méthodes de Jeu
        """
        pass


def test_melange_americain():
    assert False
