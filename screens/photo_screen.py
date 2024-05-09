import gui_components
import pygame
from photo_scanner import PhotoScanner
from screens.FoodListScreen import FoodListScreen
import os 
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
        print(self.FoodListScreen.food_from_index(self.GameStateManager.screens_index))
        self.photo_scanner = PhotoScanner(self.food_name)
        self.counter = 150
        self.photo_scanner.setStartWindow()

        
    def end_photo_scanner(self):
        self.photo_scanner.endWindow()
        
        for i in range(0, self.photo_scanner.img_counter):
            os.remove(os.path.join("images", f"opencv_frame_{i}.png"))
        
        new_food = self.photo_scanner.food_item.create_food_item()
        
        self.FoodListScreen.info_handler.add_item(new_food)
        self.FoodListScreen.nutrient_screens[self.GameStateManager.screens_index].reinit(new_food)

        self.GameStateManager.current_state = 'nutrient_screens'
        
    def run(self, pos:tuple[int,int], click: bool, pressed_keys: list):
        self.display.fill(self.bg_color)
        frame = self.photo_scanner.startPhotoWindow()
        frame = pygame.image.frombuffer(frame.tostring(), frame.shape[1::-1], "BGR")
        self.display.blit(frame, dest = (self.display.get_width()//2 - frame.get_width()//2, self.display.get_height()//2 - frame.get_height()//2) )
        
        if self.counter <= 0:
            self.end_photo_scanner()
        self.counter -=1
        