import pygame
import os
import random

from pygame.sprite import collide_mask


class GameDino():
    def __init__(self, parent):
        self.parent = parent

    def play(self):
        pygame.init()

        SCREEN_HEIGHT = 600
        SCREEN_WIDTH = 1100

        RUNNING = [pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Dino/DinoRun1.png")),
                   pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Dino/DinoRun2.png"))]
        JUMPING = pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Dino/DinoJump.png"))
        DUCKING = [pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Dino/DinoDuck1.png")),
                   pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Dino/DinoDuck2.png"))]


        SMALL_CACTUS = [pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Cactus/SmallCactus1.png")),
                        pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Cactus/SmallCactus2.png")),
                        pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Cactus/SmallCactus3.png"))]
        LARGE_CACTUS = [pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Cactus/LargeCactus1.png")),
                        pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Cactus/LargeCactus2.png")),
                        pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Cactus/LargeCactus3.png"))]

        BIRD = [pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Bird/Bird1.png")),
                pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Bird/Bird2.png"))]

        CLOUD = pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Other/Cloud.png"))

        ME = [pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Meteor/Meteor_1.png")),
              pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Meteor/Meteor_2.png")),
              pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Meteor/Meteor_R1.png")),
              pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Meteor/Meteor_R2.png")),
              pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Meteor/Boom.png")),
              pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Meteor/Rock.png"))]

        TR = pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Other/Track.png"))

        BG = [pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Other/Background_0.png")),
              pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Other/Background_1.png")),
              pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Other/Background_2.png")),
              pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Other/Background_3.png")),
              pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Other/Background_4.png")),
              pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Other/Background_5.png")),
              pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Other/Background_6.png"))]

        GR = pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Other/Ground.png"))

        SOUND = [os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Music/dino_die.mp3"),
                 os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Music/menu.mp3"),
                 os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Music/run.mp3"),
                 os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Music/tick.wav")]

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        GAME_RUNNING = 0
        GAME_OVER = 1
        INTRO = 2

        all_sprites = pygame.sprite.Group()

        class Player(pygame.sprite.Sprite):
            X_POS = 80
            Y_POS = 310
            Y_POS_DUCK = 340
            JUMP_VEL = 8.5

            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.duck_img = DUCKING
                self.run_img = RUNNING
                self.jump_img = JUMPING

                self.dino_duck = False
                self.dino_run = True
                self.dino_jump = False

                self.lose = False

                self.step_index = 0
                self.jump_vel = self.JUMP_VEL
                self.image = self.run_img[0]
                self.rect = self.image.get_rect()
                self.rect.x = self.X_POS
                self.rect.y = self.Y_POS

                self.mask = pygame.mask.from_surface(self.image)

            def duck(self):
                self.image = self.duck_img[self.step_index // 5]
                self.rect = self.image.get_rect()
                self.rect.x = self.X_POS
                self.rect.y = self.Y_POS_DUCK
                self.step_index += 1

            def run(self):
                self.image = self.run_img[self.step_index // 5]
                self.rect = self.image.get_rect()
                self.rect.x = self.X_POS
                self.rect.y = self.Y_POS
                self.step_index += 1

            def jump(self):
                self.image = self.jump_img
                if self.dino_jump:
                    self.rect.y -= self.jump_vel * 4
                    self.jump_vel -= 0.8
                if self.jump_vel < - self.JUMP_VEL:
                    self.dino_jump = False
                    self.dino_run = True
                    self.jump_vel = self.JUMP_VEL

            def control(self, event):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and not self.dino_jump:
                        self.dino_duck = False
                        self.dino_run = False
                        self.dino_jump = True
                    if event.key == pygame.K_DOWN and not self.dino_jump:
                        self.dino_duck = True
                        self.dino_run = False
                        self.dino_jump = False
                if event.type == pygame.KEYUP and not self.dino_jump:
                    self.dino_duck = False
                    self.dino_run = True
                    self.dino_jump = False

            def update(self):
                if self.dino_duck:
                    self.duck()
                if self.dino_run:
                    self.run()
                if self.dino_jump:
                    self.jump()

                if self.step_index >= 10:
                    self.step_index = 0
                for obstacle in obstacles:
                    if collide_mask(self, obstacle):
                        self.lose = True

        class Cloud(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = CLOUD
                self.rect = self.image.get_rect()
                self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
                self.rect.y = random.randint(50, 100)

            def update(self):
                self.rect.x -= game_speed
                if self.rect.x < -200:
                    self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
                    self.rect.y = random.randint(50, 100)

        class Obstacle(pygame.sprite.Sprite):
            def __init__(self, type, index):
                pygame.sprite.Sprite.__init__(self)
                self.type = type
                self.image = self.type[index]
                self.rect = self.image.get_rect()
                self.rect.x = SCREEN_WIDTH
                self.mask = pygame.mask.from_surface(self.image)

            def update(self):
                self.rect.x -= game_speed
                if self.rect.x < -200:
                    all_sprites.remove(self)
                    obstacles.remove(self)

        class SmallCactus(Obstacle):
            def __init__(self):
                self.id = 0
                self.index = random.randint(0, 2)
                super().__init__(SMALL_CACTUS, self.index)
                self.rect.y = 325

        class LargeCactus(Obstacle):
            def __init__(self):
                self.id = 1
                self.index = random.randint(0, 2)
                super().__init__(LARGE_CACTUS, self.index)
                self.rect.y = 300

        class Bird(Obstacle):
            def __init__(self):
                self.id = 2
                self.index = 0
                super().__init__(BIRD, self.index)
                self.rect.y = 250

            def update(self):
                super().update()
                if self.index >= 9:
                    self.index = 0
                self.image = BIRD[self.index // 5]
                self.index += 1

        class Meteor(Obstacle):
            def __init__(self):
                self.index = 0
                super().__init__(ME, self.index)
                self.on_air = True
                self.rect.x = 0
                self.rect.y = -100

                self.vec_x = 65
                self.vec_y = 25

                self.boom_fade = 255

            def boom(self, i):
                boom_img = ME[4]
                boom_img.convert()
                boom_img.set_alpha(i)
                if i > 0: screen.blit(boom_img, (self.rect.x - 100, self.rect.y - 120))
                pygame.display.update()

            def update(self):
                self.rect.x += self.vec_x
                self.rect.y += self.vec_y

                if self.index >= 9:
                    self.index = 0
                self.image = ME[self.index // 5]
                self.index += 1

                if self.rect.y >= 300:
                    self.boom(self.boom_fade)
                    self.boom_fade -= 10
                    self.vec_x = 0
                    self.vec_y = 0
                    self.image = ME[5]
                    super().update()

        class Meteor_To_The_Face(Meteor):
            def __init__(self):
                super().__init__()
                self.rect.x = 1000
                self.rect.y = -130

                self.vec_x = -26
                self.vec_y = 10

            def update(self):
                self.rect.x += self.vec_x
                self.rect.y += self.vec_y

                if self.index >= 9:
                    self.index = 0
                self.image = ME[self.index // 5 + 2]
                self.index += 1

                if self.rect.y >= 300:
                    self.boom(self.boom_fade)
                    self.boom_fade -= 10
                    self.vec_x = 0
                    self.vec_y = 0
                    self.image = ME[5]
                    super().update()

        class Track(pygame.sprite.Sprite):
            def __init__(self, x):
                pygame.sprite.Sprite.__init__(self)
                self.image = TR
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = 380

            def update(self):
                self.rect.x -= game_speed
                if self.rect.x < - self.image.get_width():
                    self.rect.x = self.image.get_width() - 10

        class Background(pygame.sprite.Sprite):
            def __init__(self, x, index):
                pygame.sprite.Sprite.__init__(self)
                self.index = index
                self.image = BG[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = 0

            def update(self):
                self.rect.x -= 10
                if self.rect.x < - self.image.get_width():
                    self.rect.x = self.image.get_width() - 10
                    self.index += 2
                    if self.index > 6: self.index -= 7
                    self.image = BG[self.index]

        class Ground(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = GR
                self.rect = self.image.get_rect()
                self.rect.x = 0
                self.rect.y = 380

            def update(self):
                pass

        class Text(pygame.sprite.Sprite):
            def __init__(self, text, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.font = pygame.font.Font('freesansbold.ttf', 20)
                self.image = self.font.render(text, True, (0, 0, 0))
                self.rect = self.image.get_rect()
                self.rect.center = (x, y)

            def update_text(self, text):
                self.image = self.font.render(text, True, (0, 0, 0))

        class Score(Text):
            def __init__(self):
                self.score = 0
                self.text = "Score : " + str(self.score)
                Text.__init__(self, self.text, 50, 20)

            def update_score(self):
                play_sound(SOUND[3])
                self.score += 1
                self.update_text("Score : " + str(self.score))

        def play_music(music, play_times):
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(play_times)

        def play_sound(sound):
            get_sound = pygame.mixer.Sound(sound)
            pygame.mixer.Sound.play(get_sound)

        def intro():
            text = Text("PRESS SPACE TO START", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            all_sprites.add(text)
            play_music(SOUND[1], -1)
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pygame.mixer.music.stop()
                            all_sprites.empty()
                            running = False
                        if event.key == pygame.K_ESCAPE:
                            pygame.display.set_caption('Game Client')
                            pygame.quit()
                            self.parent.run_menu()

                screen.fill((255, 255, 255))

                all_sprites.draw(screen)
                all_sprites.update()
                pygame.display.update()
                clock.tick(60)

            return GAME_RUNNING

        def game_over():
            play_music(SOUND[0], 1)
            gameOver = pygame.image.load(os.path.join("C:/Users/LAPTOP24H/Downloads/streamlit/bai1/1733678579112_game_project_d2a76c0425/game_project/Assets/Other/GameOver.png"))
            gameOverRect = gameOver.get_rect()
            gameOverRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)

            score_text = Text("Your score: " + str(sco), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            text = Text("PRESS SPACE TO RESTART!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
            all_sprites.add(text, score_text)

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pygame.mixer.music.stop()
                            all_sprites.empty()
                            running = False
                        if event.key == pygame.K_ESCAPE:
                            pygame.display.set_caption('Game Client')
                            pygame.quit()
                            self.parent.run_menu()
                screen.fill((255, 255, 255))
                screen.blit(gameOver, gameOverRect)

                all_sprites.draw(screen)
                all_sprites.update()
                pygame.display.update()
                clock.tick(60)

            return GAME_RUNNING

        obstacles = pygame.sprite.Group()

        game_speed = 20

        def game():
            background_1 = Background(0, 0)
            background_2 = Background(1100, 1)
            ground = Ground()
            all_sprites.add(background_1, background_2, ground)

            cloud = Cloud()
            all_sprites.add(cloud)

            track_1 = Track(0)
            track_2 = Track(TR.get_width())
            all_sprites.add(track_1, track_2)

            player = Player()
            all_sprites.add(player)

            score = Score()
            all_sprites.add(score)
            global sco
            sco = 0

            play_music(SOUND[2], -1)

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.display.set_caption('Game Client')
                            pygame.quit()
                            self.parent.run_menu()
                        player.control(event)


                screen.fill((172, 170, 170))

                if len(obstacles) == 0:
                    if random.randint(0, 4) == 0:
                        sc = SmallCactus()
                        all_sprites.add(sc)
                        obstacles.add(sc)

                    elif random.randint(0, 4) == 1:
                        lc = LargeCactus()
                        all_sprites.add(lc)
                        obstacles.add(lc)

                    elif random.randint(0, 4) == 2:
                        bird = Bird()
                        all_sprites.add(bird)
                        obstacles.add(bird)

                    elif random.randint(0, 4) == 3:
                        meteor = Meteor()
                        all_sprites.add(meteor)
                        obstacles.add(meteor)

                    elif random.randint(0, 4) == 4:
                        meteor_2 = Meteor_To_The_Face()
                        all_sprites.add(meteor_2)
                        obstacles.add(meteor_2)

                    check_point = True

                for ob in obstacles:
                    if check_point:
                        if player.rect.x >= ob.rect.x + 100:
                            score.update_score()
                            sco = score.score
                            check_point = False

                all_sprites.draw(screen)
                all_sprites.update()
                pygame.display.update()
                clock.tick(60)

                if player.lose:
                    pygame.mixer.music.stop()
                    all_sprites.empty()
                    obstacles.empty()
                    running = False

            return GAME_OVER

        def main():
            scene = INTRO
            while True:
                if scene == INTRO:
                    scene = intro()
                if scene == GAME_RUNNING:
                    scene = game()
                if scene == GAME_OVER:
                    scene = game_over()

        main()

