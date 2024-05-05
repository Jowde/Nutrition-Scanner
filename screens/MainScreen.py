import gui_compenonts
import pygame

BACKGROUND_COLOR = pygame.Color(255,255,255)
MENU_COLOR = pygame.Color(125,125,125)
BUTTON_COLOR = pygame.Color(125,125,200)
FONT_SIZE = 22

class MainScreen(gui_compenonts.Screen):
    def __init__(self, display, GameStateManager: "gui_compenonts.GameStateManager", bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        
        self.main_menu = gui_compenonts.Menu(self.display, (.7, .7), bg_color=MENU_COLOR, layout='vertical')
        
        self.food_list_button = gui_compenonts.Button(self.main_menu, relative_padding=(.2, .2), text='Food List', bg_color=BUTTON_COLOR, on_press=self.switch_to_food_list, text_size=FONT_SIZE)
        self.setting_button = gui_compenonts.Button(self.main_menu, text = 'Setting', bg_color=BUTTON_COLOR, relative_padding=(.2, .2), text_size=FONT_SIZE)
        
        self.main_menu.init_widgets()
    
    def switch_to_food_list(self):
        self.GameStateManager.current_state = 'foodlist_screen'

    def run(self, pos: tuple[int,int], click: bool):
        self.display.fill(self.bg_color)
        self.main_menu.draw(pos, click)