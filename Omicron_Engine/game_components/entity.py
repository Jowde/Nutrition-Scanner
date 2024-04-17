import pygame
from tile import Tile
from pygame import Vector2
from abc import ABC, abstractmethod

class Entity(Tile):
    def __init__(self, size: tuple[int, int], position: tuple[float, float], velocity: tuple[float, float] = (0,0), accel: tuple[float, float] =(0,0), color: str = None, image: "pygame.image" = None):
        if color == None:
            super().__init__(size, position, image=image)
        elif image == None:
            super().__init__(size, position, color=color)
        self.velocity = Vector2(velocity[0],velocity[1])
        self.accel = Vector2(accel[0], accel[1]) 
    
    @abstractmethod
    def update(self):
        raise NotImplementedError