from dimensional_analysis import DimensionalAnalysis
import pygame
from screens.NutrientLabelScreen import NutrientLabel
from info_handler import InfoHandler
import gui_components.screen

BUTTON_COLOR1 = pygame.Color(125,125,200)
BUTTON_COLOR2 = pygame.Color(125,125,125)
MENU_COLOR = pygame.Color(125,125,125)
BACKGROUND_COLOR = pygame.Color(255,255,255)
FONT_SIZE = 22

class ChooseWeightScreen(gui_components.Screen):
    def __init__(self, display, GameStateManager: "gui_components.GameStateManager", bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)

        self.info_handler = InfoHandler('foods.csv')
        self.weight = 55
        self.foodName = 'apple'

        self.foodItem = self.info_handler.food_from_dict(self.foodName)
        self.newFood = DimensionalAnalysis(self.weight, self.foodItem).newFood
        
        self.weighted_portion = NutrientLabel(self.display, self.GameStateManager, self.newFood, self.info_handler)
        


    def run(self, pos: tuple[int,int], click: bool, pressed_keys: list):
        self.display.fill(self.bg_color)