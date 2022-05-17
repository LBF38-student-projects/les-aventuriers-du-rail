"""
Projet informatique
@author: Mathis URIEN, Kenza BELAID
"""

# Imports:
import pygame, sys
from pygame.locals import *
from Partie import *


class Screen():
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


class Button():
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


def test():
    pygame.init()
    size = width, height = 1920 // 2, 1080 // 2
    screen = pygame.display.set_mode(size)
    plateau = pygame.image.load("img\carte_usa.jpg")
    # print(plateau.get_width(), plateau.get_height())
    wagon = pygame.image.load("img\wagon_test.png")
    pygame.display.set_caption("Les aventuriers du rail")
    size_plateau = plateau.get_size()
    # pygame.display.toggle_fullscreen()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_g:
                    game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print((mx, my))
        screen.fill("grey")
        screen.blit(plateau, ((width - size_plateau[0]) // 2, (height - size_plateau[1]) // 2))
        # pygame.display.flip()
        screen.blit(wagon, (369, 191))
        pygame.display.flip()
        # rect=pygame.Rect(1,1,1,1)
        # pygame.draw.rect(screen,"blue",rect)
        # pygame.display.flip()


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
    # launch_game()
    text_input()