import gui_components
import pygame
from screens.FoodListScreen import FoodListScreen
from screens.photo_screen import PhotoScreen
 

BACKGROUND_COLOR = pygame.Color(255,255,255)
MENU_COLOR = pygame.Color(125,125,125)
BUTTON_COLOR = pygame.Color(125,125,200)
FONT_SIZE = 22
class EditScreen(gui_components.Screen):
    def __init__(self, display, GameStateManager: "gui_components.GameStateManager", food_list_screen: FoodListScreen, PhotoScreen: PhotoScreen, bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        
        self.main_menu = gui_components.Menu(self.display, (.7, .7), bg_color=MENU_COLOR, layout='vertical')
        
        self.man_button = gui_components.Button(self.main_menu, relative_padding=(.2, .2), text='Manual Macro Input', bg_color=BUTTON_COLOR, on_press=self.switch_to_nutrient_screen, text_size=FONT_SIZE)
        self.auto_button = gui_components.Button(self.main_menu, text = 'Automatic Macro Input', bg_color=BUTTON_COLOR, relative_padding=(.2, .2), text_size=FONT_SIZE, on_press=self.switch_to_auto_screen)
        
        self.main_menu.init_widgets()

        self.food_info = None
        self.foodlistscreen = food_list_screen
        
        self.PhotoScreen = PhotoScreen
        
    def switch_to_nutrient_screen(self):
        self.GameStateManager.screens_index = self.foodlistscreen.find_index_of_food(self.food_info.food_name)
        self.GameStateManager.current_state = 'nutrient_screens'

    def switch_to_auto_screen(self):
        self.GameStateManager.screens_index = self.foodlistscreen.find_index_of_food(self.food_info.food_name)
        self.PhotoScreen.init_photo_scanner()
        self.GameStateManager.current_state = 'auto_screen'
        
    def run(self, pos:tuple[int,int], click: bool, pressed_keys: list):
        self.display.fill(self.bg_color)
        self.main_menu.draw(pos, click, pressed_keys)
