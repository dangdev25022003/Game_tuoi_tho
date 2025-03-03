from menu import Menu
from game_dino import GameDino
from game_snake import GameSnake
from Tetris import GameTetris

class GameClient():
    def __init__(self):
        self.menu = Menu(self)
        self.game_dino = GameDino(self)
        self.game_snake = GameSnake(self)
        self.game_tetris = GameTetris(self)

    def run(self):
        self.run_menu()

    def run_menu(self):
        self.menu.run()

    def play_game_dino(self):
        self.game_dino.play()

    def play_game_snake(self):
        self.game_snake.play()

    def play_game_tetris(self):
        self.game_tetris.play()

if __name__=="__main__":
    game = GameClient()
    game.run()