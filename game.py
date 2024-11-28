import pygame
import os
from pygame.locals import *
from piece import Piece
from chess import Chess

class Game:
    def __init__(self):
        WIDTH = 640
        HEIGHT = 750
        
        self.menu_showed = False
        self.running = True
        self.resources = "resources"

        pygame.display.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])

        window_title = "PyChess"
        pygame.display.set_caption(window_title)

        icon_src = os.path.join(self.resources, "icon.png")
        icon = pygame.image.load(icon_src)
        pygame.display.set_icon(icon)

        pygame.display.flip()

        self.clock = pygame.time.Clock()

    def start_game(self):
        self.board_offset_x = 0
        self.board_offset_y = 50
        self.board_dimensions = (self.board_offset_x,self.board_offset_y)