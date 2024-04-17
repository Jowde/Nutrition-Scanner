import pygame
from pygame.sprite import Sprite
from pygame import Vector2
from abc import ABC, abstractmethod


class Tile(Sprite, ABC):
    def __init__(self, size: tuple[int, int], position: tuple[int, int], color: str = None, image: "pygame.image" = None):
        Sprite.__init__(self)
        self.size = Vector2(size[0], size[1])
        self.position = Vector2(position[0], position[1])
        
        if color == None:
            self.image = image.convert()
        elif image == None:
            self.image = pygame.Surface(self.size.x, self.size.y)
          
        self.rect = self.image.get_rect()
    
    @abstractmethod
    def update(self):
        raise NotImplementedError