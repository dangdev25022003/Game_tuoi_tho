import pygame as pg
import random as rd
from dataclasses import dataclass

class GameTetris():
    def __init__(self, parent):
        self.parent = parent

    def play(self):
        pg.init()
        width, columns, rows = 300, 15, 30
        distance = width // columns
        height = distance * rows
        grid = [0] * columns * rows

        speed, score, level, temp = 1000, 0, 1, 0

        picture = []  #
        for n in range(8):
            picture.append(pg.transform.scale(pg.image.load(f''
                                                            f'./bai1/1733678579112_game_project_d2a76c0425/game_project/Tetris/T_{n}.jpg'), (distance, distance)))
            
        disp = pg.display.set_mode([width, height])
        pg.display.set_caption('Tetris Game')

        tetromino_down = pg.USEREVENT + 1

        pg.time.set_timer(tetromino_down, speed)

        pg.key.set_repeat(1, 100)

        tetrominos = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # O
                        [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],  # I
                        [0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0],  # J
                        [0, 0, 4, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # L
                        [0, 5, 5, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # S
                        [6, 6, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Z
                        [0, 0, 0, 0, 7, 7, 7, 0, 0, 7, 0, 0, 0, 0, 0, 0]]  # T



        @dataclass
        class tetromino():
            tetro: list
            row: int = 0
            column: int = 5

            def show(self):
                for n, color in enumerate(self.tetro):
                    if color > 0:
                        x = (self.column + n % 4) * distance
                        y = (self.row + n // 4) * distance
                        disp.blit(picture[color], (x, y))

            def check(self, r, c):
                for n, color in enumerate(self.tetro):
                    if color > 0:
                        rs = r + n // 4
                        cs = c + n % 4
                        if rs >= rows or cs < 0 or cs >= columns or grid[rs * columns + cs] > 0:
                            return False
                return True

            def update(self, r, c):
                if self.check(self.row + r, self.column + c):
                    self.row += r
                    self.column += c
                    return True
                return False

            def rotate(self):
                savetetro = self.tetro.copy()

                for n, color in enumerate(savetetro):
                    self.tetro[(2 - (n % 4)) * 4 + (n // 4)] = color
                if not self.check(self.row, self.column):
                    self.tetro = savetetro.copy()


        def ObjectOnGridline():
            for n, color in enumerate(character.tetro):
                if color > 0:
                    grid[(character.row + n // 4) * columns + (character.column + n % 4)] = color


        def DeleteFullRows():
            fullrows = 0
            for row in range(rows):
                for column in range(columns):
                    if grid[row * columns + column] == 0:
                        break
                else:
                    del grid[row * columns:row * columns + columns]
                    grid[0:0] = [0] * columns
                    fullrows += 1
            return fullrows ** 2 * 100


        character = tetromino(rd.choice(tetrominos))
        status = True
        while status:

            pg.time.delay(100)
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.display.set_caption('Game Client')
                        status = False
                        pg.quit()
                        self.parent.run_menu()
                if event.type == pg.QUIT:
                    status = False
                if event.type == tetromino_down:
                    if not character.update(1, 0):
                        ObjectOnGridline()
                        score += DeleteFullRows()
                        if score > 0 and score // 500 >= level and temp != score:
                            speed = int(speed * 0.8)
                            pg.time.set_timer(tetromino_down, speed)
                            level = score // 500 + 1
                            temp = score
                        character = tetromino(rd.choice(tetrominos))
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        character.update(0, -1)
                    if event.key == pg.K_RIGHT:
                        character.update(0, 1)
                    if event.key == pg.K_DOWN:
                        character.update(1, 0)
                    if event.key == pg.K_SPACE:
                        character.rotate()

            disp.fill((0,0,0))
            character.show()

            textsurface = pg.font.SysFont('UTF-8', 60).render(f'{score:,}', False, (255, 255, 255))
            disp.blit(textsurface, (width // 2 - textsurface.get_width() // 2, 5))
            textsurface = pg.font.SysFont('UTF-8', 40).render(f'Level: {level}', False, (255, 255, 255))
            disp.blit(textsurface, (width // 2 - textsurface.get_width() // 2, 55))

            for n, color in enumerate(grid):
                if color > 0:
                    x = n % columns * distance
                    y = n // columns * distance
                    disp.blit(picture[color], (x, y))

            pg.display.update()

        pg.quit()