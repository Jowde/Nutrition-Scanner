import gui_components
import pygame
from photo_scanner import PhotoScanner
from screens.FoodListScreen import FoodListScreen

BACKGROUND_COLOR = pygame.Color(255,255,255)
MENU_COLOR = pygame.Color(125,125,125)
BUTTON_COLOR = pygame.Color(125,125,200)
FONT_SIZE = 22
class PhotoScreen(gui_components.Screen):
    def __init__(self, display, GameStateManager: "gui_components.GameStateManager", FoodListScreen: FoodListScreen, bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        self.food_name = None
        self.FoodListScreen = FoodListScreen
    
    def init_photo_scanner(self):
        self.food_name = self.FoodListScreen.food_from_index(self.GameStateManager.screens_index)
        self.photo_scanner = PhotoScanner(self.food_name)
        self.photo_scanner.setStartWindow()
        
    def end_photo_scanner(self):
        self.photo_scanner.endWindow()
        
    def run(self, pos:tuple[int,int], click: bool, pressed_keys: list):
        self.display.fill(self.bg_color)
        frame = self.photo_scanner.startPhotoWindow()
        print('hello')
        frame = pygame.image.load(frame)
        self.display.blit(frame)
        