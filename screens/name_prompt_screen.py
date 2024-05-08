import gui_components
import pygame

BACKGROUND_COLOR = pygame.Color(255,255,255)
MENU_COLOR = pygame.Color(125,125,125)
BUTTON_COLOR1 = pygame.Color(125,125,200)
FONT_SIZE = 22
class NamePromptScreen(gui_components.Screen):
    def __init__(self, display, GameStateManager: "gui_components.GameStateManager", bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        
        self.name_prompt_menu = gui_components.Menu(self.display, relative_size=(.6, .7), bg_color=MENU_COLOR, layout='vertical')
        self.name_label = gui_components.Label(self.name_prompt_menu, relative_padding=(.4, .5), text='Please type name of food item', bg_color=BUTTON_COLOR1, text_size=FONT_SIZE)
        self.name_prompt = gui_components.TextInput(self.name_prompt_menu, relative_padding=(.4, .5), text='', bg_color=BUTTON_COLOR1, text_size=FONT_SIZE)
        
        self.name_prompt_menu.init_widgets()
    
    def switch_to_food_list(self):
        self.GameStateManager.current_state = 'foodlist_screen'

    def run(self, pos:tuple[int,int], click: bool, pressed_keys: list):
        self.display.fill(self.bg_color)
        self.name_prompt_menu.draw(pos, click, pressed_keys)
