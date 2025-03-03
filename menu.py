import pygame, sys
from pygame.locals import *

# Setup pygame/window ---------------------------------------- #

"""Khai bao cac constant(hang so)"""
"khởi tạo màn hình menu"
WIDTH = 1100
HEIGHT = 600
"khởi tạo các button trong menu"
"tạo khoảng trống giữa các button"
SPACE = 30
WIDTH_BUTTON = 200
HEIGHT_BUTTON = 50
OPEN_GAME_DINO = "DINO"
OPEN_GAME_SNAKE = "SNAKE"
OPEN_GAME_TETRIS = "TETRIS"

"""Ham ve text"""
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

"""Ham ve button"""
def draw_button(x, y, width, height):
    button = pygame.Rect(x, y, width, height)
    return button

class Menu():
    def __init__(self, parent):
        self.parent = parent

    def run(self):
        mainClock = pygame.time.Clock()
        """Khoi tao pygame"""
        pygame.init()
        pygame.display.set_caption('Game Client')

        """khai bao man hinh hien thi voi chieu dai la width va chieu cao la height"""
        screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        """Khai bao font chu"""
        font_menu = pygame.font.SysFont(None, 50)  # size 50
        font_button = pygame.font.SysFont(None, 30)  # size 30

        click = False
        while True:
            screen.fill((0, 0, 0))
            """ Ve chu Menu game len man hinh (screen)"""
            draw_text(text='Menu game', font=font_menu, color=(255, 255, 255),
                      surface=screen, x=WIDTH / 2 - 100, y=HEIGHT / 2 - 100)

            """Ve 2 nut lua chon"""
            # lay toa do cua chuot
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # tao 2 nut bam
            button_dino = draw_button(x=(WIDTH - WIDTH_BUTTON) / 2,
                                      y=(HEIGHT - HEIGHT_BUTTON - SPACE) / 2,
                                      width=WIDTH_BUTTON,
                                      height=HEIGHT_BUTTON)
            button_snake = draw_button(x=(WIDTH - WIDTH_BUTTON) / 2,
                                       y=(HEIGHT - HEIGHT_BUTTON - SPACE) / 2 + HEIGHT_BUTTON + SPACE,
                                       width=WIDTH_BUTTON,
                                       height=HEIGHT_BUTTON)

            button_tetris = draw_button(x=(WIDTH - WIDTH_BUTTON) / 2,
                                        y=(HEIGHT - HEIGHT_BUTTON - SPACE) / 2 + (HEIGHT_BUTTON + SPACE)*2,
                                        width=WIDTH_BUTTON,
                                        height=HEIGHT_BUTTON)

            # kiem tra xem nut bam co duoc bam
            if button_dino.collidepoint((mouse_x, mouse_y)):
                if click:
                    self.action(OPEN_GAME_DINO)
            if button_snake.collidepoint((mouse_x, mouse_y)):
                if click:
                    self.action(OPEN_GAME_SNAKE)
            if button_tetris.collidepoint((mouse_x, mouse_y)):
                if click:
                    self.action(OPEN_GAME_TETRIS)

            # ve 2 nut bam tren len man hinh (screen)
            pygame.draw.rect(screen, (255, 0, 0), button_dino)
            pygame.draw.rect(screen, (255, 0, 0), button_snake)
            pygame.draw.rect(screen, (255, 0, 0), button_tetris)

            # ve 2 chu len nut bam
            draw_text(text='Dino', font=font_button, color=(255, 255, 255), surface=screen,
                      x=(WIDTH - WIDTH_BUTTON) / 2 + WIDTH_BUTTON/2 - 30,
                      y=(HEIGHT - HEIGHT_BUTTON - SPACE) / 2 + HEIGHT_BUTTON / 3)
            draw_text(text='Snake', font=font_button, color=(255, 255, 255), surface=screen,
                      x=(WIDTH - WIDTH_BUTTON) / 2 + WIDTH_BUTTON/2 - 30,
                      y=(HEIGHT - HEIGHT_BUTTON - SPACE) / 2 + HEIGHT_BUTTON + SPACE + HEIGHT_BUTTON / 3)
            draw_text(text='Tetris', font=font_button, color=(255, 255, 255), surface=screen,
                      x=(WIDTH - WIDTH_BUTTON) / 2 + WIDTH_BUTTON/2 - 30,
                      y=(HEIGHT - HEIGHT_BUTTON - SPACE) / 2 + (HEIGHT_BUTTON + SPACE)*2 + HEIGHT_BUTTON / 3)

            # kiem tra xem nam nut gi
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()
            mainClock.tick(60)

    # thuc hien hanh dong bam nut
    def action(self, _action):
        # neu nut duoc bam la dino
        if _action == OPEN_GAME_DINO:
            pygame.display.set_caption('Game Dinosaur')
            self.parent.play_game_dino()
        # neu nut duoc bam la snake
        if _action == OPEN_GAME_SNAKE:
            pygame.display.set_caption('Game Snake')
            self.parent.play_game_snake()
        if _action == OPEN_GAME_TETRIS:
            pygame.display.set_caption('Game Tetris')
            self.parent.play_game_tetris()