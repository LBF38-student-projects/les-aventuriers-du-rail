"""
Projet informatique
@author: Mathis URIEN, Kenza BELAID
"""

# Imports:
import pygame, sys, os
from pygame.locals import *
from Partie import *


class Screen:
    def __init__(self, title, width=640, height=445, fill="white"):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.current = False

    def make_current(self):
        pygame.display.set_caption(self.title)
        self.current = True
        self.screen = pygame.display.set_mode((self.width, self.height))

    def end_current(self):
        self.current = False

    def check_update(self):
        return self.current

    def screen_update(self):
        if self.current:
            self.screen.fill(self.fill)

    def return_title(self):
        return self.screen


# class Button:
#     def __init__(self, x, y, sx, sy, bcolour, fbcolour, font, fontsize, fcolour, text):
#         self.x = x
#         self.y = y
#         self.sx = sx
#         self.sy = sy
#         self.bcolour = bcolour
#         self.fbcolour = fbcolour
#         self.fcolour = fcolour
#         self.fontsize = fontsize
#         self.text = text
#         self.current = False
#         self.buttonf = pygame.font.SysFont(font, fontsize)
#
#     def show_button(self, display):
#         if self.current:
#             pygame.draw.rect(display, self.fbcolour, (self.x, self.y, self.sx, self.sy))
#         else:
#             pygame.draw.rect(display, self.bcolour, (self.x, self.y, self.sx, self.sy))
#         textsurface = self.buttonf.render(self.text, False, self.fcolour)
#         display.blit(textsurface, (self.x + self.sx / 2 - (self.fontsize / 2) * (len(self.text) / 2) - 5,
#                                    (self.y + self.sy / 2 - (self.fontsize / 2) - 4)))
#
#     def focus_check(self, mousepos, mouseclick):
#         if self.x <= mousepos[0] <= self.x + self.sx and self.y <= mousepos[1] <= self.y + self.sy:
#             self.current = True
#             return mouseclick[0]
#         else:
#             self.current = False
#             return False


# def launch_game():
#     pygame.init()
#     pygame.font.init()
#     menuScreen = Screen("Les aventuriers du rail")
#     screen2 = Screen("Screen 2")
#
#     win = menuScreen.make_current()
#     done = False
#     testButton = Button(0, 0, 150, 50, "black", "blue", "arial", 20, "white", "Menu")
#     returnButton = Button(0, 0, 150, 50, "orange", "green", "arial", 20, "black", "Back")
#
#     toggle = False
#
#     while not done:
#         menuScreen.screen_update()
#         screen2.screen_update()
#         mouse_pos = pygame.mouse.get_pos()
#         mouse_click = pygame.mouse.get_pressed()
#         keys = pygame.key.get_pressed()
#
#         # menuScreen Page code
#         if menuScreen.check_update():
#             screen2button = testButton.focus_check(mouse_pos, mouse_click)
#             testButton.show_button(menuScreen.return_title())
#             if screen2button:
#                 win = screen2.make_current()
#                 menuScreen.end_current()
#
#         # Screen 2 Page code
#         elif screen2.check_update():
#             # Back Button
#             returnm = returnButton.focus_check(mouse_pos, mouse_click)
#             returnButton.show_button(screen2.return_title())
#             if returnm:
#                 win = menuScreen.make_current()
#                 screen2.end_current()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True
#         pygame.display.update()
#     pygame.quit()


# def game():
#     size = width, height = 1920 // 2, 1080 // 2
#     screen = pygame.display.set_mode(size)
#     run = True
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     run = False
#         screen.fill("blue")
#         pygame.display.flip()
#         # screen.blit(plateau, ((width - size_plateau[0]) // 2, (height - size_plateau[1]) // 2))


# def IHM():
#     pygame.init()
#
#     # Initialize the screen
#     size = width, height = 1920 // 2, 1080 // 2
#     screen = pygame.display.set_mode(size, pygame.RESIZABLE)
#     pygame.display.set_caption("Les aventuriers du rail")
#
#     # Images import
#     plateau = pygame.image.load("img\carte_usa.jpg")
#     wagon_blanc = pygame.image.load("img\wagon_blanc.jpg")
#     wagon_bleu = pygame.image.load("img\wagon_bleu.jpg")
#     wagon_jaune = pygame.image.load("img\wagon_jaune.jpg")
#     wagon_noir = pygame.image.load("img\wagon_noir.jpg")
#     wagon_orange = pygame.image.load("img\wagon_orange.jpg")
#     wagon_rose = pygame.image.load("img\wagon_rose.jpg")
#     wagon_rouge = pygame.image.load("img\wagon_rouge.jpg")
#     wagon_vert = pygame.image.load("img\wagon_vert.jpg")
#     locomotive = pygame.image.load("img\locomotive.jpg")
#     dos_destination = pygame.image.load("img\dos_destination.jpg")
#     table_points = pygame.image.load("img/table_points.jpg")
#     dos_wagon = pygame.image.load("img\dos_wagon.jpg")
#     dos_wagon = pygame.transform.rotate(dos_wagon, 90)
#     les_wagons=[wagon_blanc,wagon_bleu,wagon_jaune,wagon_noir,wagon_orange,wagon_rose,wagon_rouge,wagon_vert,locomotive]
#     size_plateau = plateau.get_size()
#
#     # basic font for user typed
#     base_font = pygame.font.Font(None, 32)
#     user_text = ""
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#                 # Check for backspace
#                 if event.key == pygame.K_BACKSPACE:
#                     # get text input from 0 to -1 i.e. end.
#                     user_text = user_text[:-1]
#                 # Unicode standard is used for string
#                 # formation
#                 else:
#                     user_text += event.unicode
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mx, my = pygame.mouse.get_pos()
#                 print((mx, my))
#             if event.type == pygame.VIDEORESIZE:
#                 screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
#
#         # background
#         screen.fill("grey")
#         screen.blit(plateau,
#                     ((screen.get_width() - size_plateau[0]) // 2, (screen.get_height() - size_plateau[1]) // 2))
#         low_bar = pygame.Rect(0, (screen.get_height() + plateau.get_height()) // 2 + 5, screen.get_width(),
#                               screen.get_height())
#         pygame.draw.rect(screen, "blue", low_bar)
#
#         # textes
#         text_surface = base_font.render(user_text, True, (255, 255, 255))
#         questions_surface = base_font.render("Interaction avec le joueur", True, "black")
#
#         # Affichage texte pour interaction joueur
#         screen.blit(questions_surface, (10, (screen.get_height() + plateau.get_height()) // 2 + 10))
#         screen.blit(text_surface, (10, (screen.get_height() + plateau.get_height()) // 2 + questions_surface.get_height()+10))
#
#
#         # Affichage de la pile
#         for k in range(5):
#             screen.blit(wagon_bleu,
#                         (50, (screen.get_height() - plateau.get_height()) // 2 + wagon_bleu.get_height() * k + k * 5))
#
#         # Affichage texte : Pioche
#         pioche_surface = base_font.render("Pioche", True, "black")
#         screen.blit(pioche_surface, (50,(screen.get_height() - plateau.get_height()) // 2-pioche_surface.get_height()))
#
#         # Affichage des cartes Destination
#         for i in range(3):
#             screen.blit(dos_destination, ((screen.get_width() + plateau.get_width()) // 2 + 20,
#                                           (screen.get_height() - plateau.get_height()) // 2 + (
#                                                       dos_destination.get_height() + 5) * i))
#         # Affichage texte : Pioche
#         destination_surface = base_font.render("Destination", True, "black")
#         screen.blit(destination_surface,
#                     (50, (screen.get_height() - plateau.get_height()) // 2 - pioche_surface.get_height()))
#
#         # Affichage des cartes de la main du joueur
#         for w,wagon in enumerate(les_wagons):
#             screen.blit(wagon,
#                         (questions_surface.get_width()+20+(wagon.get_width()+5)*w, (screen.get_height() + plateau.get_height()) // 2 + 10))
#
#
#
#         # screen.blit(dos_wagon, ((screen.get_width() + plateau.get_width()) // 2 + 10, 50))
#
#         # Affichage du compteur de points
#         pygame.draw.circle(screen, "red", [screen.get_width(), screen.get_height()],
#                            (screen.get_height() - plateau.get_height()) // 2 - 5, 0)
#         nb_points=5
#         points_surface = base_font.render(str(nb_points), True, "black")
#         screen.blit(points_surface, (screen.get_width()-(points_surface.get_width()+20), screen.get_height()-(points_surface.get_height()+20)))
#
#         # Affichage du titre/pseudo du joueur (?)
#         pygame.draw.polygon(screen, "green",
#                             [[screen.get_width() // 2 - 250, 0], [screen.get_width() // 2 + 250, 0],
#                              [screen.get_width() // 2 + 225, 35], [screen.get_width() // 2 - 225, 35]])
#         title_surface = base_font.render("Les aventuriers du rail", True, "black")
#         screen.blit(title_surface, (screen.get_width() // 2 - title_surface.get_width() // 2, 10))
#
#         pygame.display.update()


# TODO: faire une fonction pour changer les cartes de la pioche en fonction de la pioche de la partie
# TODO: faire une fonction pour les cartes du joueur
# TODO: faire une fonction pour ajouter une route prise
# TODO: faire une fonction pour récupérer les instructions du joueur => texte input
# TODO: faire une classe pour gérer tout l'IHM ?
# TODO: faire une fenêtre pour gérer le début d'une partie

# def ihm_debut_partie():
#     """Interface pour un début de partie"""
#     screen=Screen("Les aventuriers du rail",)
def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('img', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image: {}'.format(fullname))
        raise SystemExit(message)
    return image, image.get_rect()


def text_objects(text, font):
    paragraph_size = (600, 500)
    font_size = font.get_height()

    # Step 1
    paragraph_surface = pygame.Surface(paragraph_size)

    # Set colorkey to fake transparent paragraph surface
    paragraph_surface.fill((255, 255, 255))
    paragraph_surface.set_colorkey((255, 255, 255))

    # Step 2
    split_lines = text.splitlines()

    # Step 3: center the text vertically
    off_set = (paragraph_size[1] - len(split_lines) * (font_size + 1)) // 2

    # Step 4
    for idx, line in enumerate(split_lines):
        current_text_line = font.render(line, False, (0, 0, 0))
        current_position = (0, idx * font_size + off_set)
        paragraph_surface.blit(current_text_line, current_position)

    # Step 5
    return paragraph_surface, paragraph_size


class Button:
    def __init__(self, text, pos, width=200, height=40, elevation=5):
        # Core attributes
        self.pos = pos
        self.width = width
        self.height = height
        self.text = text
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = self.pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(self.pos, (self.width, self.height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(self.pos, (self.width, self.height))
        self.bottom_color = '#354B5E'

        # text
        self.gui_font = pygame.font.Font(None, 30)
        self.text_surf = self.gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, screen):
        # Resizable
        self.reposition()
        # self.top_rect.move(self.pos[0],self.pos[1])
        # self.bottom_rect.move(self.pos[0],self.pos[1])

        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def reposition(self):
        self.top_rect.x, self.top_rect.y = self.pos
        self.bottom_rect.x, self.bottom_rect.y = self.pos
        self.original_y_pos = self.pos[1]

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = 'lightblue'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    # print('click')
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'


# TODO: créer une classe pour les texts inputs. Penser à faire une méthode pour renvoyer les valeurs des inputs

class Text:
    def __init__(self, text: str, width: int, height: int, color="black"):
        """Classe pour afficher du texte sur une fenêtre"""
        # Core attributes
        self.width = width
        self.height = height
        self.text = text
        self.pos = (self.width, self.height)
        self.color = color

        # Text initialization
        self.base_font = pygame.font.Font(None, 32)
        self.text_surface = self.base_font.render(text, True, color)

    @property
    def pos(self):
        """Accesseur en lecture de pos"""
        return self.width, self.height

    @pos.setter
    def pos(self, value: tuple):
        """Accesseur en écriture de pos"""
        self.__pos = value

    def show(self, screen):
        screen.blit(self.text_surface, self.pos)


class IhmPartie:
    def __init__(self, partie=Partie()):
        pygame.init()

        # Lien avec la partie :
        self.partie = partie
        self.count_joueur = 0

        # Initialize the screen
        self.size = width, height = 1920 // 2, 1080 // 2
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption("Les aventuriers du rail")
        self.clock = pygame.time.Clock()
        self.button_play = Button('Play',
                                  ((self.screen.get_width() - 200) // 2, (self.screen.get_height() - 40) // 2))
        self.button_options = Button('Options',
                                     (self.button_play.pos[0], self.button_play.pos[1] + self.button_play.height + 10))
        self.button_credits = Button('Credits',
                                     (self.button_options.pos[0],
                                      self.button_options.pos[1] + self.button_options.height + 10))
        self.button_back = Button('Back', (20, self.screen.get_height() - 50))
        self.button_start = Button('Start',
                                   (self.button_back.pos[0], self.button_back.pos[1] - 50))

        # Images import
        # basics
        self.plateau = pygame.image.load("img/carte_usa.jpg")
        self.dos_destination = pygame.image.load("img/dos_destination.jpg")
        self.table_points = pygame.image.load("img/table_points.jpg")
        # window icon
        self.game_icon = pygame.image.load("img/cargo-train.png")
        pygame.display.set_icon(self.game_icon)

        # Cartes wagons
        self.wagon_blanc = pygame.image.load("img/wagon_blanc.jpg")
        self.wagon_bleu = pygame.image.load("img/wagon_bleu.jpg")
        self.wagon_jaune = pygame.image.load("img/wagon_jaune.jpg")
        self.wagon_noir = pygame.image.load("img/wagon_noir.jpg")
        self.wagon_orange = pygame.image.load("img/wagon_orange.jpg")
        self.wagon_rose = pygame.image.load("img/wagon_rose.jpg")
        self.wagon_rouge = pygame.image.load("img/wagon_rouge.jpg")
        self.wagon_vert = pygame.image.load("img/wagon_vert.jpg")
        self.locomotive = pygame.image.load("img/locomotive.jpg")
        self.dos_wagon = pygame.image.load("img/dos_wagon.jpg")
        self.dos_wagon = pygame.transform.rotate(self.dos_wagon, 90)

        # Cartes Destination
        self.los_angeles_new_york = pygame.image.load("img/los_angeles_new_york.jpg")
        self.duluth_houston = pygame.image.load("img/duluth_houston.jpg")
        self.sault_ste_marie_nashville = pygame.image.load("img/sault_ste_marie_nashville.jpg")
        self.new_york_atlanta = pygame.image.load("img/new_york_atlanta.jpg")
        self.portland_nashville = pygame.image.load("img/portland_nashville.jpg")
        self.vancouver_montreal = pygame.image.load("img/vancouver_montreal.jpg")
        self.duluth_el_paso = pygame.image.load("img/duluth_el_paso.jpg")
        self.toronto_miami = pygame.image.load("img/toronto_miami.jpg")
        self.portland_phoenix = pygame.image.load("img/portland_phoenix.jpg")
        self.dallas_new_york = pygame.image.load("img/dallas_new_york.jpg")
        self.calgary_salt_lake_city = pygame.image.load("img/calgary_salt_lake_city.jpg")
        self.calgary_phoenix = pygame.image.load("img/calgary_phoenix.jpg")
        self.los_angeles_miami = pygame.image.load("img/los_angeles_miami.jpg")
        self.winnipeg_little_rock = pygame.image.load("img/winnipeg_little_rock.jpg")
        self.san_francisco_atlanta = pygame.image.load("img/san_francisco_atlanta.jpg")
        self.kansas_city_houston = pygame.image.load("img/kansas_city_houston.jpg")
        self.los_angeles_chicago = pygame.image.load("img/los_angeles_chicago.jpg")
        self.denver_pittsburgh = pygame.image.load("img/denver_pittsburgh.jpg")
        self.chicago_santa_fe = pygame.image.load("img/chicago_santa_fe.jpg")
        self.vancouver_santa_fe = pygame.image.load("img/vancouver_santa_fe.jpg")
        self.boston_miami = pygame.image.load("img/boston_miami.jpg")
        self.chicago_new_orleans = pygame.image.load("img/chicago_new_orleans.jpg")
        self.montreal_atlanta = pygame.image.load("img/montreal_atlanta.jpg")
        self.seattle_new_york = pygame.image.load("img/seattle_new_york.jpg")
        self.denver_el_paso = pygame.image.load("img/denver_el_paso.jpg")
        self.helena_los_angeles = pygame.image.load("img/helena_los_angeles.jpg")
        self.winnipeg_houston = pygame.image.load("img/winnipeg_houston.jpg")
        self.montreal_new_orleans = pygame.image.load("img/montreal_new_orleans.jpg")
        self.sault_ste_marie_oklahoma_city = pygame.image.load("img/sault_ste_marie_oklahoma_city.jpg")
        self.seattle_los_angeles = pygame.image.load("img/seattle_los_angeles.jpg")

    def launch_game(self):
        """Lance le jeu et la fenêtre d'accueil du jeu"""
        background, bg_rect = load_png("menu_principal.jpg")
        test_input = TextInput()
        run = True
        while run:
            clicking = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicking = True
                test_input.event_handler(event)
            if self.button_play.pressed:
                self.button_play.pressed = False
                self.launch_partie()
            if self.button_options.pressed:
                self.button_options.pressed = False
                self.launch_options()
            if self.button_credits.pressed:
                self.button_credits.pressed = False
                self.launch_credits()

            # Default setup for the menu screen
            background = pygame.transform.scale(background, self.screen.get_size())
            self.screen.blit(background, (0, 0))

            # Resize buttons if screen resized
            self.button_play.pos = ((self.screen.get_width() - self.button_play.width) // 2,
                                    (self.screen.get_height() - self.button_play.height) // 2)
            self.button_options.pos = (self.button_play.pos[0], self.button_play.pos[1] + self.button_play.height + 10)
            self.button_credits.pos = (
                self.button_options.pos[0], self.button_options.pos[1] + self.button_options.height + 10)

            # Draw buttons on the menu screen
            self.button_play.draw(self.screen)
            self.button_options.draw(self.screen)
            self.button_credits.draw(self.screen)
            input_test = test_input.input(clicking, self.screen)
            if input_test:
                print(input_test)

            # Update screen
            pygame.display.flip()
            self.clock.tick(60)

    def launch_partie(self):
        """Interface pour le début d'une partie"""
        # Core attributes
        screen_partie = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption("Les aventuriers du rail - Nouvelle Partie")

        # Nouvelle partie :
        self.partie = Partie()
        self.count_joueur = 0

        # Pour tester l'IHM:
        self.partie.les_joueurs["TestPlayer1"] = Joueur("TestPlayer1", "random")
        self.partie.les_joueurs["TestPlayer2"] = Joueur("TestPlayer2", "random")
        self.partie.ordre.append("TestPlayer1")
        self.partie.ordre.append("TestPlayer2")

        # Default setup for the menu screen
        background, bg_rect = load_png("ticket_to_ride.jpg")
        background = pygame.transform.scale(background, screen_partie.get_size())
        screen_partie.blit(background, (0, 0))

        # Text
        text_partie = Text("Nouvelle Partie", 20, 20)

        run = True
        while run:
            clicking = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicking = True
            if self.button_back.pressed:
                self.button_back.pressed = False
                self.launch_game()
            if self.button_start.pressed:
                self.button_start.pressed = False
                # self.partie.partie(self)
                # FIXME: vérifier attributions des cartes au début du jeu. Améliorer le lien avec le backend.
                # FIXME: Améliorer les fonctionnalités des buttons => refonte si tps ? (problème de clicker 1x)
                self.partie.preparation_partie()
                print(self.partie.pile_cartes_destination)
                print(self.partie.pile_cartes_wagon)
                for joueur in self.partie.les_joueurs.values():
                    IhmJoueur().launch(joueur)
                    # self.clock.tick(60)

            background = pygame.transform.scale(background, screen_partie.get_size())
            screen_partie.blit(background, (0, 0))
            # Draw buttons on the menu screen
            self.button_back.draw(self.screen)
            self.button_start.draw(self.screen)

            # Text & Text inputs
            # FIXME: remplacer tous les textes ci-dessous par des texts inputs
            self.text_nb_joueurs = Text("Nombre de joueurs pour la partie", (self.screen.get_width() - 100) // 2,
                                        (self.screen.get_height() - 250) // 2)
            self.text_joueur = Text("Nom et couleur du joueur", self.text_nb_joueurs.pos[0],
                                    self.text_nb_joueurs.pos[1] + 50)
            text_partie.show(screen_partie)
            # Affichage des textes
            self.text_nb_joueurs.show(self.screen)
            self.text_joueur.show(self.screen)
            # Update current screen
            pygame.display.update()
            self.clock.tick(60)

    def launch_options(self):
        """Interface pour les options du jeu"""
        # Core attributes
        screen_options = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption("Les aventuriers du rail - Options")

        # Default setup for the menu screen
        background, bg_rect = load_png("background_ticket_to_ride.jpg")
        background = pygame.transform.scale(background, screen_options.get_size())
        screen_options.blit(background, (0, 0))

        # Text
        text_options = Text("Options du jeu", screen_options.get_width() // 2, screen_options.get_height() // 2)

        run = True
        while run:
            clicking = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                if event.type == MOUSEBUTTONDOWN:
                    clicking = True
            if self.button_back.pressed:
                self.button_back.pressed = False
                self.launch_game()

            background = pygame.transform.scale(background, screen_options.get_size())
            screen_options.blit(background, (0, 0))
            # Draw buttons on the menu screen
            self.button_back.draw(self.screen)
            text_options.show(screen_options)
            # Update current screen
            pygame.display.update()
            self.clock.tick(60)

    def launch_credits(self):
        """Interface pour les crédits du jeu"""
        # Core attributes
        screen_credits = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption("Les aventuriers du rail - Credits")

        # Default setup for the menu screen
        background, bg_rect = load_png("background_ticket_to_ride.jpg")
        background = pygame.transform.scale(background, screen_credits.get_size())
        screen_credits.blit(background, (0, 0))

        # Text
        title_credits = Text("Crédits du jeu", screen_credits.get_width() // 2, screen_credits.get_height() // 2)
        plain_text = """paragraphe sur les crédits\nBonjour, je suis un paragraphe\tEt ceux-ci sont les crédits
        \nMathis URIEN & Kenza BELAID"""
        text_credits = Text(plain_text, title_credits.width, title_credits.height + 50)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
            if self.button_back.pressed:
                self.button_back.pressed = False
                self.launch_game()

            background = pygame.transform.scale(background, screen_credits.get_size())
            screen_credits.blit(background, (0, 0))
            # Draw buttons on the menu screen
            self.button_back.draw(self.screen)
            title_credits.show(screen_credits)
            # text_credits.show(screen_credits)
            paragraph_surface, paragraph_size = text_objects(plain_text, pygame.font.Font(None, 32))
            self.screen.blit(paragraph_surface, paragraph_size)

            # Update current screen
            pygame.display.update()
            self.clock.tick(60)


class IhmJoueur(IhmPartie):
    def __init__(self):
        super().__init__()

        # Core attributes
        self.les_wagons = {
            "blanc": self.wagon_blanc,
            "bleu": self.wagon_bleu,
            "jaune": self.wagon_jaune,
            "noir": self.wagon_noir,
            "orange": self.wagon_orange,
            "rose": self.wagon_rose,
            "rouge": self.wagon_rouge,
            "vert": self.wagon_vert,
            "locomotive": self.locomotive
        }
        self.les_destinations = {
            "Los Angeles to New York": self.los_angeles_new_york,
            "Duluth to Houston": self.duluth_houston,
            "Sault Ste Marie to Nashville": self.sault_ste_marie_nashville,
            "New York to Atlanta": self.new_york_atlanta,
            "Portland to Nashville": self.portland_nashville,
            "Vancouver to Montreal": self.vancouver_montreal,
            "Duluth to El Paso": self.duluth_el_paso,
            "Toronto to Miami": self.toronto_miami,
            "Portland to Phoenix": self.portland_phoenix,
            "Dallas to New York": self.dallas_new_york,
            "Calgary to Salt Lake City": self.calgary_salt_lake_city,
            "Calgary to Phoenix": self.calgary_phoenix,
            "Los Angeles to Miami": self.los_angeles_miami,
            "Winnipeg to Little Rock": self.winnipeg_little_rock,
            "San Francisco to Atlanta": self.san_francisco_atlanta,
            "Kansas City to Houston": self.kansas_city_houston,
            "Los Angeles to Chicago": self.los_angeles_chicago,
            "Denver to Pittsburgh": self.denver_pittsburgh,
            "Chicago to Santa Fe": self.chicago_santa_fe,
            "Vancouver to Santa Fe": self.vancouver_santa_fe,
            "Boston to Miami": self.boston_miami,
            "Chicago to New Orleans": self.chicago_new_orleans,
            "Montreal to Atlanta": self.montreal_atlanta,
            "Seattle to New York": self.seattle_new_york,
            "Denver to El Paso": self.denver_el_paso,
            "Helena to Los Angeles": self.helena_los_angeles,
            "Winnipeg to Houston": self.winnipeg_houston,
            "Montreal to New Orleans": self.montreal_new_orleans,
            "Sault Ste Marie to Oklahoma City": self.sault_ste_marie_oklahoma_city,
            "Seattle to Los Angeles": self.seattle_los_angeles
        }
        self.size_plateau = self.plateau.get_size()

        # basic font for user typed
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = ""
        self.interaction_joueur = "Interaction avec le joueur"

        # Buttons
        self.button_fin_tour = Button("Fin du tour", (self.screen.get_width() - 220, 10))
        self.button_test = Button("Test", (self.screen.get_width() - 20, 10))

    def launch(self, joueur):
        mx, my = -1, -1
        run = True
        while run:
            clicking = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                    # Check for backspace
                    if event.key == K_BACKSPACE:
                        # get text input from 0 to -1 i.e. end.
                        self.user_text = self.user_text[:-1]
                    # Unicode standard is used for string
                    # formation
                    else:
                        self.user_text += event.unicode
                    # if event.key == K_RETURN:
                    #     return self.user_text
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print((mx, my))
                    if event.button == 1:
                        clicking = True
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if self.button_fin_tour.pressed:
                self.button_fin_tour.pressed = False
                run = False

            # background
            self.screen.fill("grey")
            self.screen.blit(self.plateau,
                             ((self.screen.get_width() - self.size_plateau[0]) // 2,
                              (self.screen.get_height() - self.size_plateau[1]) // 2))
            self.low_bar = pygame.Rect(0, (self.screen.get_height() + self.plateau.get_height()) // 2 + 5,
                                       self.screen.get_width(),
                                       self.screen.get_height())
            pygame.draw.rect(self.screen, "darkslategray", self.low_bar)

            # textes
            self.text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
            self.questions_surface = self.base_font.render(self.interaction_joueur, True, "black")

            # Affichage texte pour interaction joueur
            self.screen.blit(self.questions_surface,
                             (10, (self.screen.get_height() + self.plateau.get_height()) // 2 + 10))
            self.screen.blit(self.text_surface,
                             (10, (self.screen.get_height() + self.plateau.get_height()) // 2
                              + self.questions_surface.get_height() + 10))

            # Affichage de la pile + pioche en début de file
            for i in range(len(self.partie.pile_cartes_wagon)):
                offset = 0.05 * i
                x = -self.dos_wagon.get_width() // 2 + offset
                y = (
                            self.screen.get_height() - self.plateau.get_height()) // 2 - self.dos_wagon.get_height() - 10 + offset
                self.screen.blit(self.dos_wagon, (x, y))
                if pygame.Rect.collidepoint(self.dos_wagon.get_rect().move(x, y), mx, my) and clicking:
                    # self.partie.prendre_cartes_wagon(joueur,self)
                    print("Carte face cachée")
            for k in range(5):
                # DONE: link this to the current partie
                current_wagon = self.les_wagons[self.partie.pile_cartes_wagon[k]]
                x = current_wagon.get_width() // 4
                y = (self.screen.get_height() - self.plateau.get_height()) // 2 + (current_wagon.get_height() + 5) * k
                self.screen.blit(current_wagon, (x, y))
                if pygame.Rect.collidepoint(current_wagon.get_rect().move(x, y), mx, my) and clicking:
                    nom_carte = self.partie.pile_cartes_wagon.pop(k)
                    self.interaction_joueur = f"Vous avez tiré un wagon {nom_carte}"
                    # print("Carte visible")

            # Affichage texte : Pioche
            # self.pioche_surface = self.base_font.render("Pioche", True, "black")
            # self.screen.blit(self.pioche_surface,
            #                  (50, (self.screen.get_height() - self.plateau.get_height()) // 2
            #                   - self.pioche_surface.get_height()))

            # Affichage des cartes Destination + pioche Destination
            x, y = -1, -1
            for k in range(len(self.partie.pile_cartes_destination)):  # Pioche Destination
                offset = 0.5 * k
                x = self.screen.get_width() - self.dos_destination.get_width() // 2 - offset
                y = (self.screen.get_height() - self.plateau.get_height()) // 2 - 10 + offset
                self.screen.blit(self.dos_destination, (x, y))
            if pygame.Rect.collidepoint(self.dos_destination.get_rect().move(x, y), mx, my) and clicking:
                nom_carte_destination = self.partie.pile_cartes_destination.pop(0)
                joueur.main_destination.append(nom_carte_destination)
                self.interaction_joueur = f"Objectif: relier {nom_carte_destination}"
            for i in range(len(joueur.main_destination)):  # Cartes joueur Destination
                # DONE: link this to player's ones
                if joueur.main_destination:
                    current_destination = self.les_destinations[joueur.main_destination[i]]
                else:
                    current_destination = self.dos_destination
                current_destination = pygame.transform.scale(current_destination, self.dos_destination.get_size())
                self.screen.blit(current_destination, ((self.screen.get_width() + self.plateau.get_width()) // 2 + 20,
                                                       (self.screen.get_height() - self.plateau.get_height()) // 2
                                                       + self.dos_destination.get_height() + 10 +
                                                       (self.dos_destination.get_height() + 5) * i))
            # Affichage texte : Destination
            # self.destination_surface = self.base_font.render("Destination", True, "black")
            # self.screen.blit(self.destination_surface,
            #                  ((self.screen.get_width() - self.destination_surface.get_width()) - 20,
            #                   (self.screen.get_height() - self.plateau.get_height()) // 2 - self.pioche_surface.get_height()))

            # Affichage des cartes de la main du joueur
            for w, wagon in enumerate(joueur.main_wagon.items()):
                # DONE: lier avec la main du joueur
                img_wagon = self.les_wagons[wagon[0]]
                pos = ((self.screen.get_width() - self.screen.get_height() + self.plateau.get_height()) // 2 - 15
                       + img_wagon.get_width() * 5 // 10 * w,
                       (self.screen.get_height() + self.plateau.get_height()) // 2 + 10)
                nb_wagon = Text(str(wagon[1]), pos[0] + 5, pos[1] + img_wagon.get_height())
                nb_wagon.height = pos[1] + img_wagon.get_height() - nb_wagon.text_surface.get_height()
                self.screen.blit(img_wagon, pos)
                nb_wagon.show(self.screen)

            # screen.blit(dos_wagon, ((screen.get_width() + plateau.get_width()) // 2 + 10, 50))

            # Bouton pour la fin de tour
            self.button_fin_tour.draw(self.screen)

            # Affichage du compteur de points
            pygame.draw.circle(self.screen, "lightsteelblue", [self.screen.get_width(), self.screen.get_height()],
                               (self.screen.get_height() - self.plateau.get_height()) // 2 - 5, 0)
            nb_points = joueur.nb_points
            points_surface = self.base_font.render(str(nb_points), True, "black")
            self.screen.blit(points_surface, (self.screen.get_width() - (points_surface.get_width() + 20),
                                              self.screen.get_height() - (points_surface.get_height() + 20)))

            # Affichage du titre/pseudo du joueur
            self.title_rect = pygame.draw.polygon(self.screen, joueur.couleur,
                                                  [[self.screen.get_width() // 2 - 250, 0],
                                                   [self.screen.get_width() // 2 + 250, 0],
                                                   [self.screen.get_width() // 2 + 225, 35],
                                                   [self.screen.get_width() // 2 - 225, 35]])
            if joueur.couleur == "black":
                title_color = "white"
            else:
                title_color = "black"
            title_surface = self.base_font.render(joueur.nom_joueur, True, title_color)
            self.screen.blit(title_surface, (self.screen.get_width() // 2 - title_surface.get_width() // 2, 10))

            # Affichage des autres scores de joueur
            other_players = self.partie.ordre.copy()
            other_players.pop(other_players.index(joueur.nom_joueur))
            for p, player in enumerate(other_players):
                player = self.partie.les_joueurs[player]
                plain_text = f"{player.nom_joueur}: {player.nb_points}"
                text_player = Text(plain_text, self.title_rect.width + 20 * p, self.title_rect.height)
                text_player.show(self.screen)

            # Bouton test pour tester les fonctionnalités
            self.button_test.draw(self.screen)
            if self.button_test.pressed and clicking:
                self.button_test.pressed = not self.button_test.pressed
                joueur.nb_points += 1

            pygame.display.update()
            self.clock.tick(60)


class TextInput():
    def __init__(self, title="Nouvelle entrée de texte", rect_pos=(20, 20)):
        # Core attributes
        self.toggle_return = False
        self.text_margin = 10
        self.active = False

        # Text
        self.base_font = pygame.font.Font(None, 24)
        self.text_input = ""

        # Title
        self.title = title
        self.title_color = "black"
        self.title_surface = self.base_font.render(self.title, True, self.title_color)

        # Rect for text input
        self.rect_input = pygame.Rect(rect_pos,
                                      (tuple(map(sum,
                                                 zip(self.title_surface.get_size(),
                                                     (0, self.base_font.get_linesize()))))))
        self.default_color = "grey"
        self.active_color = "white"
        self.rect_color = self.default_color
        self.default_rect_width = self.title_surface.get_width()

        # Text input
        self.text_color = "black"
        self.text_surf = self.base_font.render(self.text_input, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(
            midleft=tuple(map(sum, zip(self.rect_input.midleft, (self.text_margin, 0)))))

    def show(self, screen):
        pygame.draw.rect(screen, self.rect_color, self.rect_input, border_radius=self.rect_input.height)
        screen.blit(self.text_surf, self.text_rect)
        screen.blit(self.title_surface, (self.rect_input.x, self.rect_input.y - self.title_surface.get_height()))

    def input(self, clicking, screen):
        mx, my = pygame.mouse.get_pos()
        # self.event_handler(event)
        if self.rect_input.collidepoint(mx, my) and clicking:
            self.active = not self.active
        if self.active:
            self.rect_color = self.active_color
        else:
            self.rect_color = self.default_color

        self.rect_input.width = max(self.default_rect_width, self.text_surf.get_width() + self.text_margin * 2)
        self.text_rect.midleft = tuple(map(sum, zip(self.rect_input.midleft, (self.text_margin, 0))))
        # self.text_rect.top=self.rect_input.top+5
        self.text_surf = self.base_font.render(self.text_input, True, self.text_color)
        self.show(screen)

        if self.toggle_return:
            returned_text = self.text_input
            self.text_input = ""
            self.active = False
            self.toggle_return = False
            return returned_text

    def event_handler(self, event):
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE and self.active:
                self.text_input = self.text_input[:-1]
            elif self.active:
                self.text_input += event.unicode
            if event.key == K_RETURN:
                self.toggle_return = True


def text_input():
    # pygame.init() will initialize all
    # imported module
    pygame.init()

    clock = pygame.time.Clock()

    # it will display on screen
    screen = pygame.display.set_mode([600, 500])

    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text = ''

    # create rectangle
    input_rect = pygame.Rect(200, 200, 140, 32)

    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')

    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    active = False

    while True:
        for event in pygame.event.get():

            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode

        # it will set background color of screen
        screen.fill((255, 255, 255))

        if active:
            color = color_active
        else:
            color = color_passive

        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)

        text_surface = base_font.render(user_text, True, (255, 255, 255))

        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)

        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()

        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)


if __name__ == '__main__':
    # print("hello world")
    # launch_game()
    # text_input()
    IHM = IhmJoueur()
    IHM.launch_game()
    # menuScreen = Screen("Les aventuriers du rail")
    # menuScreen.make_current()
    # menuScreen.return_title()
