import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.components.soundtrack import Music
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS,LARGE_CANO, BIRD, CLOUD, BIRD_RED, BIRD_GREEN, BIRD_BLUE, DEATH_SOUND

class ObstacleManager():
    def __init__(self):
        self.obstacle = []
        self.cloud = []
        self.Bird_choice = [BIRD, BIRD_RED, BIRD_GREEN, BIRD_BLUE]


    def update(self, game):
        self.num = random.randint(0,2)

        if len (self.cloud) == 0:
            self.cloud.append(Cloud(CLOUD)) 

        if len (self.obstacle) == 0:
            if self.num == 0:
                self.obstacle.append(Cactus(SMALL_CACTUS, 325))
            if self.num == 1:
                self.obstacle.append(Cactus(LARGE_CANO, 270))
            if self.num == 2:
                self.obstacle.append(Bird(random.choice(self.Bird_choice)))

        for obstacle in self.obstacle:
            obstacle.update(game.game_speed, self.obstacle)
            if game.player.dino_rect.colliderect(obstacle.rect):
                Music.play_sound(self, DEATH_SOUND, 0.1)
                pygame.mixer.music.stop()
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break
        
        for cloud in self.cloud:
            cloud.update(game.game_speed, self.cloud)

            
    def draw(self, screen):
        for obstacle in self.obstacle:
            obstacle.draw(screen)

        for cloud in self.cloud:
            cloud.draw(screen)

    def reset_obstacles(self):
        self.obstacle.clear()
        self.cloud.clear()