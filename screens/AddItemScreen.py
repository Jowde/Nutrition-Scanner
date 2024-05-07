import gui_components
import pygame
from food import Food
import gui_components.menu
import photo_scanner

BACKGROUND_COLOR = pygame.Color(255,255,255)
MENU_COLOR = pygame.Color(125,125,125)
BUTTON_COLOR = pygame.Color(125,125,200)
FONT_SIZE = 22

class AddItemScreen(gui_compenonts.Screen):
    def __init__(self, display, GameStateManager: "gui_compenonts.GameStateManager", bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)

        self.main_menu = gui_compenonts.Menu(self.display, relative_size=(.4, .4), layout='vertical')
        self.photoscan = PhotoScanner()

        #Create back button

        #Create buttons ( Add via Label Add manually )
        #Add via label - takes function that starts camera fuction

        self.addButton = gui_compenonts.Button(self.main_menu, relative_padding=(.6, .7), text="Photo Scanner", on_press=self.startWindow, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)

        self.main_menu.init_widgets()

        #Add manually - takes you to screen where you can manually add items
    def startWindow(self):
        foodName = input("Food name here: ")
        self.photoscan.setStartWindow()
        self.photoscan.startPhotoWindow(foodName)
    
    def run(self, pos:tuple[int,int], click: bool):
        self.main_menu.draw(pos, click)

    
class AddItemScreen(gui_components.Screen):
    def __init__(self, display, GameStateManager: "gui_components.GameStateManager", bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)

        self.main_menu = gui_components.Menu(self.display, relative_size=(.8, .8), bg_color=BACKGROUND_COLOR, layout='vertical')

        #Create buttons ( Add via Label Add manually )
        #Add via label - takes function that starts camera fuction
        self.addButton = gui_components.Button(self.main_menu, relative_padding=(.4, .4), text="Use Photo Scanner", on_press=photo_scanner.startPhotoWindow())

        #Add manually - takes you to screen where you can manually add items
    def run(self, pos:tuple[int,int], click: bool, pressed_keys: list):
        self.main_menu.draw(pos, click, pressed_keys)

