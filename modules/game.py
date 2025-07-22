import pygame
from pygame import Surface

from modules.map_generation import generate_map
from modules.sprites.tile import Tile

from configuration.settings import *


class Game:
    def __init__(self):
        self.tiles_group = pygame.sprite.Group()
        self.walls_group = pygame.sprite.Group()
        self.player = None

    def render(self):
        self.virtual_screen.fill(BG_COLOR)

        self.tiles_group.draw(self.virtual_screen)

        scaled_surface = pygame.transform.scale(self.virtual_screen, self.screen.get_size())
        self.screen.blit(scaled_surface, (0, 0))
        pygame.display.flip()

    def setup(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        generate_map(self.tiles_group, self.walls_group)
        self.running = True
        self.screen = pygame.display.set_mode(WIN_SIZE, pygame.RESIZABLE)
        self.virtual_screen = Surface(WIN_SIZE)
        self.clock = pygame.time.Clock()
        self.fps = FPS

    def game_cycle(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.render()
            self.clock.tick(self.fps)

    def run(self):
        self.setup()
        self.game_cycle()