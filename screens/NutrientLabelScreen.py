import gui_compenonts
import pygame
from food import Food
class NutrientLabel(gui_compenonts.Screen):
    def __init__(self, display, GameStateManager: "gui_compenonts.GameStateManager", food_info: Food, bg_color: pygame.Color = pygame.Color(255,255,255)):
        super().__init__(display, GameStateManager, bg_color)
        self.food_info = food_info
        
        self.main_menu = gui_compenonts.Menu(self.display, relative_size=(.4, .8), bg_color=pygame.Color(125,125,125))
        
    def run(self, pos, click):
        print(NutrientLabel)