"""
Projet informatique
@author: Mathis URIEN, Kenza BELAID
"""

# Imports:
import pygame, sys
from pygame.locals import *


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


class Button:
    def __init__(self, x, y, sx, sy, bcolour, fbcolour, font, fontsize, fcolour, text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.bcolour = bcolour
        self.fbcolour = fbcolour
        self.fcolour = fcolour
        self.fontsize = fontsize
        self.text = text
        self.current = False
        self.buttonf = pygame.font.SysFont(font, fontsize)

    def show_button(self, display):
        if self.current:
            pygame.draw.rect(display, self.fbcolour, (self.x, self.y, self.sx, self.sy))
        else:
            pygame.draw.rect(display, self.bcolour, (self.x, self.y, self.sx, self.sy))
        textsurface = self.buttonf.render(self.text, False, self.fcolour)
        display.blit(textsurface, (self.x + self.sx / 2 - (self.fontsize / 2) * (len(self.text) / 2) - 5,
                                   (self.y + self.sy / 2 - (self.fontsize / 2) - 4)))

    def focus_check(self, mousepos, mouseclick):
        if self.x <= mousepos[0] <= self.x + self.sx and self.y <= mousepos[1] <= self.y + self.sy:
            self.current = True
            return mouseclick[0]
        else:
            self.current = False
            return False


def launch_game():
    pygame.init()
    pygame.font.init()
    menuScreen = Screen("Les aventuriers du rail")
    screen2 = Screen("Screen 2")

    win = menuScreen.make_current()
    done = False
    testButton = Button(0, 0, 150, 50, "black", "blue", "arial", 20, "white", "Menu")
    returnButton = Button(0, 0, 150, 50, "orange", "green", "arial", 20, "black", "Back")

    toggle = False

    while not done:
        menuScreen.screen_update()
        screen2.screen_update()
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        # menuScreen Page code
        if menuScreen.check_update():
            screen2button = testButton.focus_check(mouse_pos, mouse_click)
            testButton.show_button(menuScreen.return_title())
            if screen2button:
                win = screen2.make_current()
                menuScreen.end_current()

        # Screen 2 Page code
        elif screen2.check_update():
            # Back Button
            returnm = returnButton.focus_check(mouse_pos, mouse_click)
            returnButton.show_button(screen2.return_title())
            if returnm:
                win = menuScreen.make_current()
                screen2.end_current()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.update()
    pygame.quit()


def game():
    size = width, height = 1920 // 2, 1080 // 2
    screen = pygame.display.set_mode(size)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        screen.fill("blue")
        pygame.display.flip()
        # screen.blit(plateau, ((width - size_plateau[0]) // 2, (height - size_plateau[1]) // 2))


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

class IhmJoueur:
    def __init__(self):
        pygame.init()

        # Initialize the screen
        self.size = width, height = 1920 // 2, 1080 // 2
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption("Les aventuriers du rail")

        # Images import
        self.plateau = pygame.image.load("img/carte_usa.jpg")
        self.wagon_blanc = pygame.image.load("img/wagon_blanc.jpg")
        self.wagon_bleu = pygame.image.load("img/wagon_bleu.jpg")
        self.wagon_jaune = pygame.image.load("img/wagon_jaune.jpg")
        self.wagon_noir = pygame.image.load("img/wagon_noir.jpg")
        self.wagon_orange = pygame.image.load("img/wagon_orange.jpg")
        self.wagon_rose = pygame.image.load("img/wagon_rose.jpg")
        self.wagon_rouge = pygame.image.load("img/wagon_rouge.jpg")
        self.wagon_vert = pygame.image.load("img/wagon_vert.jpg")
        self.locomotive = pygame.image.load("img/locomotive.jpg")
        self.dos_destination = pygame.image.load("img/dos_destination.jpg")
        self.table_points = pygame.image.load("img/table_points.jpg")
        self.dos_wagon = pygame.image.load("img/dos_wagon.jpg")
        self.dos_wagon = pygame.transform.rotate(self.dos_wagon, 90)
        self.les_wagons = [self.wagon_blanc, self.wagon_bleu, self.wagon_jaune, self.wagon_noir, self.wagon_orange,
                           self.wagon_rose, self.wagon_rouge,
                           self.wagon_vert, self.locomotive]
        self.size_plateau = self.plateau.get_size()

        # basic font for user typed
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = ""

    # def affichage_pioche(self,pioche):

    def launch(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
                        # get text input from 0 to -1 i.e. end.
                        self.user_text = self.user_text[:-1]
                    # Unicode standard is used for string
                    # formation
                    else:
                        self.user_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print((mx, my))
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            # background
            self.screen.fill("grey")
            self.screen.blit(self.plateau,
                             ((self.screen.get_width() - self.size_plateau[0]) // 2,
                              (self.screen.get_height() - self.size_plateau[1]) // 2))
            self.low_bar = pygame.Rect(0, (self.screen.get_height() + self.plateau.get_height()) // 2 + 5,
                                       self.screen.get_width(),
                                       self.screen.get_height())
            pygame.draw.rect(self.screen, "blue", self.low_bar)

            # textes
            self.text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
            self.questions_surface = self.base_font.render("Interaction avec le joueur", True, "black")

            # Affichage texte pour interaction joueur
            self.screen.blit(self.questions_surface,
                             (10, (self.screen.get_height() + self.plateau.get_height()) // 2 + 10))
            self.screen.blit(self.text_surface,
                             (10, (self.screen.get_height() + self.plateau.get_height()) // 2
                              + self.questions_surface.get_height() + 10))

            # Affichage de la pile
            for k in range(5):
                self.screen.blit(self.wagon_bleu,
                                 (50, (self.screen.get_height() - self.plateau.get_height()) // 2
                                  + self.wagon_bleu.get_height() * k + k * 5))

            # Affichage texte : Pioche
            self.pioche_surface = self.base_font.render("Pioche", True, "black")
            self.screen.blit(self.pioche_surface,
                             (50, (self.screen.get_height() - self.plateau.get_height()) // 2
                              - self.pioche_surface.get_height()))

            # Affichage des cartes Destination
            for i in range(3):
                self.screen.blit(self.dos_destination, ((self.screen.get_width() + self.plateau.get_width()) // 2 + 20,
                                                        (self.screen.get_height() - self.plateau.get_height()) // 2 + (
                                                                self.dos_destination.get_height() + 5) * i))
            # Affichage texte : Pioche
            self.destination_surface = self.base_font.render("Destination", True, "black")
            self.screen.blit(self.destination_surface,
                             (50, (
                                     self.screen.get_height() - self.plateau.get_height()) // 2 - self.pioche_surface.get_height()))

            # Affichage des cartes de la main du joueur
            for w, wagon in enumerate(self.les_wagons):
                self.screen.blit(wagon,
                                 (self.questions_surface.get_width() + 20 + (wagon.get_width() + 5) * w,
                                  (self.screen.get_height() + self.plateau.get_height()) // 2 + 10))

            # screen.blit(dos_wagon, ((screen.get_width() + plateau.get_width()) // 2 + 10, 50))

            # Affichage du compteur de points
            pygame.draw.circle(self.screen, "red", [self.screen.get_width(), self.screen.get_height()],
                               (self.screen.get_height() - self.plateau.get_height()) // 2 - 5, 0)
            nb_points = 5
            points_surface = self.base_font.render(str(nb_points), True, "black")
            self.screen.blit(points_surface, (self.screen.get_width() - (points_surface.get_width() + 20),
                                              self.screen.get_height() - (points_surface.get_height() + 20)))

            # Affichage du titre/pseudo du joueur (?)
            pygame.draw.polygon(self.screen, "green",
                                [[self.screen.get_width() // 2 - 250, 0], [self.screen.get_width() // 2 + 250, 0],
                                 [self.screen.get_width() // 2 + 225, 35], [self.screen.get_width() // 2 - 225, 35]])
            title_surface = self.base_font.render("Les aventuriers du rail", True, "black")
            self.screen.blit(title_surface, (self.screen.get_width() // 2 - title_surface.get_width() // 2, 10))

            pygame.display.update()


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
    IHM=IhmJoueur
    IhmJoueur.launch(IHM)
