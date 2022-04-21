"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

# Imports :
from Jeu import Jeu
from Joueur import Joueur
from Score import Score


class Partie():
    """Classe qui est utilisé pour lancer une partie du jeu.
    Fait appel à la classe Jeu pour accéder à toutes les cartes et informations sur le plateau de jeu."""

    def __init__(self):
        self.les_joueurs = []
        self.nb_joueurs: int = 0


    def debut_partie(self):
        """
        Définition des joueurs
        :return:
        """
        self.nb_joueurs = int(input('Nombre de joueurs pour la partie'))
        for k in range(self.nb_joueurs):
            self.les_joueurs.append(Joueur(input('Nom du Joueur ' + str(k + 1)), input(
                'Choisir sa couleur de Joueur parmi les suivantes : \n - blue \n - red \n - black \n - random'), 0))

    def choix_tour_joueur(self):
        """
        Définit le tour des joueurs en fonction de celui qui a le plus voyagé puis selon sens horaire.
        :return:
        L'ordre des joueurs de la partie
        """
        joueur_voyageur = input("Qui a le plus voyagé entre ces joueurs ? \n" + self.liste_joueurs())
        index_premier = 0
        j = self.les_joueurs[0]
        while j.nom_joueur != joueur_voyageur:
            index_premier += 1
            j = self.les_joueurs[index_premier]
        if index_premier == 0:
            return "L'ordre des joueurs est établi comme suit : \n" + self.liste_joueurs()
        else:
            temp_joueur = []
            while len(self.les_joueurs) > index_premier:
                temp_joueur.append(self.les_joueurs.pop(index_premier))
            while len(self.les_joueurs) > 0:
                temp_joueur.append(self.les_joueurs.pop(0))
            self.les_joueurs = temp_joueur
            return "L'ordre des joueurs est établi comme suit : \n" + self.liste_joueurs()

    def liste_joueurs(self):
        """
        Renvoie la liste des joueurs en partie dans l'ordre de leur tour.
        :return:
        """
        liste_joueurs = ""
        for joueur in self.les_joueurs:
            liste_joueurs += joueur.nom_joueur + "\n"
        return liste_joueurs

    def tour(self, joueur):
        """
        Réalise 1 tour pour 1 joueur de toutes les actions possibles.
        :return:
        """
        print("C'est le tour de " + joueur.nom_joueur)
        choix: int = int(input(
            "Que voulez-vous faire ?\n" + "1. Prendre des cartes Wagon\n2. Prendre possession d'une route\n3. "
                                          "Prendre des cartes Destination supplémentaires\nIndiquer le numéro "
                                          "de l'action choisie"))
        if choix == 1:
            self.prendre_cartes_wagon()
        elif choix == 2:
            self.prendre_route()
        else:
            self.prendre_cartes_Destination()

    def prendre_cartes_wagon(self):
        """
         1. Prendre des cartes Wagon :
        – le joueur peut prendre 2 cartes Wagon.
        Il peut prendre n’importe quelle carte visible parmi les 5 posées sur la table ou tirer une carte du dessus de
        la pioche (tirage en aveugle). Si le joueur prend une carte visible, il la remplace immédiatement par une
        autre du dessus de la pioche. Il peut ensuite prendre une deuxième carte, soit visible, soit en aveugle (voir
        section Cartes Wagon pour les cartes Locomotive).
        :return:
        """
        """Indication sur les cartes Wagon : 
        Cartes Wagon 
        
        Il existe 8 types de wagons différents en plus de la locomotive. Les couleurs de chaque carte Wagon 
        correspondent aux couleurs présentes sur le plateau afin de relier les villes : bleu, violet, orange, blanc, 
        vert, jaune, noir et rouge. Les locomotives sont multicolores et, comme des cartes joker, peuvent remplacer 
        n’importe quelle couleur lors de la prise de possession d’une route."""

        """"
        Il est possible de ne jouer que des cartes Locomotive pour prendre une route. Si une carte Locomotive figure 
        parmi les 5 cartes visibles, le joueur peut la prendre, mais son tour s’arrête alors. La locomotive compte 
        comme si l’on avait pris 2 cartes. Si, après avoir pris une carte visible (qui n’est pas une locomotive), 
        la carte de remplacement est une locomotive, le joueur ne peut pas la prendre. Si, au cours du jeu, 
        3 cartes visibles sur 5 sont des locomotives, les 5 cartes sont alors immédiatement défaussées et remplacées 
        par 5 nouvelles cartes. 
        
        Note : Si un joueur a la chance de tirer une locomotive en aveugle, au sommet de la pioche, les autres 
        joueurs n’en savent rien et cette carte ne compte que pour une seule carte piochée. Un joueur peut avoir en 
        main et à tout moment autant de cartes qu’il le souhaite. Quand la pioche de cartes est épuisée, les cartes 
        défaussées sont soigneusement mélangées pour reconstituer une nouvelle pioche. Il est important de bien 
        mélanger les cartes car elles ont été défaussées par séries de couleurs ! Dans le cas peu probable où il n’y 
        aurait plus de cartes disponibles (si toutes les cartes sont dans les mains des joueurs) un joueur ne peut 
        plus prendre de cartes. Il ne peut donc que prendre possession d’une route ou tirer de nouvelles cartes 
        Destination. """

        print("Je prends des cartes Wagon")
        print("A implémenter")
        return None

    def prendre_route(self):
        """
        2. Prendre possession d’une route :
        – Le joueur peut s’emparer d’une route sur le plateau en posant autant de cartes Wagon de la couleur
        de la route que d’espaces composant la route. Après avoir défaussé ses cartes, le joueur pose alors ses wagons
        sur chaque espace constituant la route. Enfin, il déplace son marqueur de score en se référant au tableau de
        décompte des points.
        :return:
        """

        """Indication:
        Prendre possession des routes
        Pour prendre possession d’une route, un joueur doit jouer une série de cartes égale au
        nombre d’espaces composant la route. La série de cartes doit être composée de cartes du
        même type. La plupart des routes nécessitent une série de cartes de couleur spécifique. Par
        exemple, les routes bleues sont capturées en posant des cartes Wagon bleues. Certaines
        routes – en gris sur le plateau - peuvent être capturées en utilisant n’importe quelle série
        d’une même couleur.
        Lorsqu’une route a été capturée, le joueur pose ses wagons en plastique sur chacun des
        espaces qui constituent la route. Toutes les cartes utilisées pour s’approprier cette route
        sont défaussées.
        Un joueur peut prendre possession de n’importe quelle route sur le plateau de jeu. Il n’est
        pas obligé de se connecter avec les routes déjà à son actif. Un joueur ne peut jamais prendre
        plus d’une route par tour de jeu.
        Une route prise par un joueur devient sa propriété exclusive. Aucun
        autre joueur ne peut plus revendiquer son
        usage ou son occupation.
        Certaines villes sont reliées par des routes
        doubles. Un même joueur ne peut pas prendre
        2 routes reliant les 2 mêmes villes.
        Note importante : Dans une configuration
        à 2 ou 3 joueurs, seule l’une des routes constituant la double
        connexion peut être utilisée. Un joueur peut donc prendre
        possession de l’une des 2 routes disponibles, la route restante
        demeurant fermée jusqu’à la fin de la partie.
        """
        print("Je prends une route")
        print("A implémenter")
        return None

    def prendre_cartes_Destination(self):
        """
        3. Prendre des cartes Destination supplémentaires :
        – Le joueur prend 3 cartes Destination du dessus de la pioche. Il doit en conserver au moins une,
        mais peut aussi garder 2 ou 3 cartes. Chaque carte qui n’est pas conservée est posée face cachée sous la pioche
        des cartes Destination.
        :return:
        """

        """Indication
        Prendre des cartes
        Destination
        Un joueur peut utiliser son tour de jeu pour récupérer des cartes
        Destination supplémentaires. Pour cela, il doit prendre 3 cartes
        sur le dessus de la pile des cartes Destination. Il doit conserver
        au moins l’une des trois cartes, mais peut bien sûr en garder 2
        ou même 3. S’il reste moins de 3 cartes Destination dans la pile,
        le joueur ne peut prendre que le nombre de cartes disponibles. Chaque carte qui n’est pas conservée par le joueur est remise face cachée sous la pile.
        Chaque carte Destination fait référence à deux villes de la carte et un nombre de points y est associé. Si le joueur réalise la connexion entre les deux
        villes d’une carte Destination, il remporte le nombre de points indiqué sur la carte et l’additionne, en fin de partie, aux points déjà acquis. La route
        reliant ces deux villes doit être formée uniquement par les trains de ce joueur. Si la connexion n’est pas réalisée, le joueur déduit de son nombre de
        points déjà acquis le nombre indiqué sur la carte.
        Les cartes Destination sont gardées secrètes tout au long de la partie. Elles sont rendues publiques à la fin de la partie et chaque joueur calcule son
        score. Au cours du jeu, un joueur peut avoir autant de cartes Destination qu’il le souhaite.
        """

        print("Je prends une carte Destination")
        print("A implémenter")
        return None

    def partie(self):
        """
        Fait tourner une partie complète du jeu. Du début à la fin.
        :return:
        """
        self.debut_partie()

        """
        # Règle du jeu :
        ## Tour de jeu
        Le joueur qui a le plus voyagé commence."""
        self.choix_tour_joueur()
        """Par la suite, on joue dans le sens des aiguilles d’une montre. 
        À son tour, le joueur doit faire une et une seule des trois actions suivantes : 
        1. Prendre des cartes Wagon : 
        – le joueur peut prendre 2 cartes Wagon. 
        Il peut prendre n’importe quelle carte visible parmi les 5 posées sur la table ou tirer une carte du dessus de 
        la pioche (tirage en aveugle). Si le joueur prend une carte visible, il la remplace immédiatement par une 
        autre du dessus de la pioche. Il peut ensuite prendre une deuxième carte, soit visible, soit en aveugle (voir 
        section Cartes Wagon pour les cartes Locomotive). 
        
        2. Prendre possession d’une route : 
        – Le joueur peut s’emparer d’une route sur le plateau en posant autant de cartes Wagon de la couleur 
        de la route que d’espaces composant la route. Après avoir défaussé ses cartes, le joueur pose alors ses wagons 
        sur chaque espace constituant la route. Enfin, il déplace son marqueur de score en se référant au tableau de 
        décompte des points.
        
        3. Prendre des cartes Destination supplémentaires :
        – Le joueur prend 3 cartes Destination du dessus de la pioche. Il doit en conserver au moins une, 
        mais peut aussi garder 2 ou 3 cartes. Chaque carte qui n’est pas conservée est posée face cachée sous la pioche 
        des cartes Destination.
        """
        for joueur in self.les_joueurs:
            print(self.tour(joueur))  # Tour à implémenter avec chaque action possible.


if __name__ == '__main__':
    p = Partie()
    p.partie()
    # test=input('test de input')
