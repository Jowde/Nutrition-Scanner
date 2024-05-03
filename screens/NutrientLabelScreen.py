import gui_compenonts
import pygame
from food import Food

BACKGROUND_COLOR = pygame.Color(255,255,255)
MENU_COLOR = pygame.Color(125,125,125)

class NutrientLabel(gui_compenonts.Screen):
    def __init__(self, display, GameStateManager: "gui_compenonts.GameStateManager", food_info: Food, bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        self.food_info = food_info
        
        self.main_menu = gui_compenonts.Menu(self.display, relative_size=(.4, .8), bg_color=MENU_COLOR)