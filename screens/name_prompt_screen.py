import gui_components
import pygame
from screens import FoodListScreen
BACKGROUND_COLOR = pygame.Color(255,255,255)
MENU_COLOR = pygame.Color(125,125,125)
BUTTON_COLOR1 = pygame.Color(125,125,200)
FONT_SIZE = 22
class NamePromptScreen(gui_components.Screen):
    def __init__(self, display, GameStateManager: "gui_components.GameStateManager", foodlistscreen:FoodListScreen, bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        
        self.foodlistscreen = foodlistscreen
        self.name_prompt_menu = gui_components.Menu(self.display, relative_size=(.6, .7), bg_color=MENU_COLOR, layout='vertical')
        self.name_label = gui_components.Label(self.name_prompt_menu, relative_padding=(.4, .5), text='Please type name of food item', bg_color=BUTTON_COLOR1, text_size=FONT_SIZE)
        self.name_prompt = gui_components.TextInput(self.name_prompt_menu, relative_padding=(.4, .5), text='', bg_color=BUTTON_COLOR1, text_size=FONT_SIZE)
        
        self.name_prompt_menu.init_widgets()
        
        self.back_menu = gui_components.Menu(self.display, relative_size=(.2, .2), position='topleft')
        self.back_button = gui_components.Button(self.back_menu, relative_padding=(.6,.7), bg_color=BUTTON_COLOR1, on_press=self.switch_to_food_list, text='Back', text_size=FONT_SIZE)
        self.back_menu.init_widgets()
        
        self.confirm_menu = gui_components.Menu(self.display, relative_size=(.2, .2), position='bottomright')
        self.confirm_button = gui_components.Button(self.confirm_menu, relative_padding=(.6,.7), bg_color=BUTTON_COLOR1, on_press=self.switch_to_correct_screen, text='Confirm', text_size=FONT_SIZE)
        self.confirm_menu.init_widgets()
        
        self.titleMenu = gui_components.Menu(self.display, relative_size=(.5, .075), position='bottomcenter')
        self.titleLabel = gui_components.Label(self.titleMenu, relative_padding=(0,0), text=f'')
        
        self.titleMenu.init_widgets()
    
    def switch_to_food_list(self):
        self.GameStateManager.current_state = 'foodlist_screen'

    def switch_to_correct_screen(self):
        if self.foodlistscreen.adding_item:
            pass
        elif self.foodlistscreen.removing_item:
            try:
                foodItem = self.foodlistscreen.info_handler.food_from_dict(self.name_prompt.text)
                self.foodlistscreen.info_handler.remove_item(foodItem)
                self.foodlistscreen.food_scroll_index = 0
                self.foodlistscreen.init_menus()
                self.foodlistscreen.removing_item = False
                self.switch_to_food_list()
            except:
                self.titleLabel.text = 'invalid food name'
                self.titleMenu.init_widgets()
        else:
            print('name prompt was not given routing info' )
            
    def run(self, pos:tuple[int,int], click: bool, pressed_keys: list):
        
        self.display.fill(self.bg_color)
        self.name_prompt_menu.draw(pos, click, pressed_keys)
        self.back_menu.draw(pos, click, pressed_keys)
        self.confirm_menu.draw(pos, click, pressed_keys)
        self.titleMenu.draw(pos, click, pressed_keys)
        
