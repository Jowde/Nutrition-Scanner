import gui_components
from info_handler import InfoHandler
import pygame
from screens.NutrientLabelScreen import NutrientLabel 

BUTTON_COLOR1 = pygame.Color(125,125,200)
BUTTON_COLOR2 = pygame.Color(125,125,125)
MENU_COLOR = pygame.Color(125,125,125)
BACKGROUND_COLOR = pygame.Color(255,255,255)
FONT_SIZE = 22


class FoodListScreen(gui_components.Screen):
    def __init__(self, display, GameStateManager: "gui_components.GameStateManager", bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        
        self.title_menu = gui_components.Menu(self.display, relative_size=(.4, .2), position='topcenter')
        self.title_button = gui_components.Button(self.title_menu, relative_padding=(.3, .3), bg_color=BUTTON_COLOR1, text='Food List', on_press=lambda: True, hover_highlight=1, text_size=FONT_SIZE)
        self.title_menu.init_widgets() 
        
        self.back_menu = gui_components.Menu(self.display, relative_size=(.2, .2), position='topleft')
        self.back_button = gui_components.Button(self.back_menu, relative_padding=(.6,.7), bg_color=BUTTON_COLOR1, on_press=self.switch_to_main, text='Back', text_size=FONT_SIZE)
        self.back_menu.init_widgets()
        
        self.nutrient_screens = []
        
        self.adding_item = False
        self.removing_item = False
        
        self.info_handler = InfoHandler('foods.csv')
        self.info_handler.loadfromfile()
        
        self.food_scroll_menus = []
        
        self.food_scroll_index = 0
        self.max_index = 0
        self.next_menu = gui_components.Menu(self.display, relative_size=(.2, .2), position='bottomright')
        self.next_button = gui_components.Button(self.next_menu, relative_padding=(.6,.7), bg_color=BUTTON_COLOR1, on_press=self.increase_index, text='Next', text_size=FONT_SIZE)
        self.next_menu.init_widgets()
        
        self.previous_menu = gui_components.Menu(self.display, relative_size=(.2, .2), position='bottomleft')
        self.previous_button = gui_components.Button(self.previous_menu, relative_padding=(.6,.7), bg_color=BUTTON_COLOR1, on_press=self.decrease_index, text='Previous', text_size=FONT_SIZE)
        self.previous_menu.init_widgets()

        func = lambda : self.navigate_to_foodlist()

        self.addremove_menu = gui_components.Menu(self.display, relative_size=(.2, .2), position='topright', layout='vertical')
        self.add_item = gui_components.Button(self.addremove_menu, relative_padding=(.6, .7), text='Add Item', bg_color=BUTTON_COLOR1, text_size=FONT_SIZE, on_press=self.add_item)
        self.remove_item = gui_components.Button(self.addremove_menu, relative_padding=(.6, .7), text="Remove Item", bg_color=BUTTON_COLOR1, text_size=FONT_SIZE, on_press=self.remove_item)
        self.addremove_menu.init_widgets()
        
        self.init_menus()

    def navigate_to_foodlist(self):
        self.GameStateManager.current_state = 'name_prompt_screen'
    
    def increase_index(self):
        if self.food_scroll_index < len(self.food_scroll_menus) - 1:
            self.food_scroll_index+=1
            
    def decrease_index(self):
        if self.food_scroll_index > 0:
            self.food_scroll_index-=1
            
    def index_limit_upper(self):
        return self.food_scroll_index < len(self.food_scroll_menus) - 1
    
    def index_limit_lower(self):
        return self.food_scroll_index > 0
            
    def init_menus(self):
        
        index = 3
        self.info_handler.savetofile()
        self.info_handler.loadfromfile()
        self.nutrient_screens = []
        self.food_scroll_menus = []
        
        for food in self.info_handler.food_dict:
            if index == 3:
                self.food_scroll_menus.append(gui_components.Menu(self.display, relative_size=(.7, .7), bg_color=MENU_COLOR, layout='vertical'))
                index = 0
    
            self.nutrient_screens.append(NutrientLabel(self.display, self.GameStateManager, self.info_handler.food_from_dict(food), self.info_handler))
            

            on_press_func = lambda x=self.find_index_of_food(food): self.switch_to_nutrient_label(x)
            
            gui_components.Button(self.food_scroll_menus[-1], text=f'{food}', relative_padding=(.3, .3), bg_color=pygame.Color(125,125,200), on_press=on_press_func, hover_highlight=1.25, text_size=FONT_SIZE)
            
            index+=1

        while index <3:
            gui_components.Button(self.food_scroll_menus[-1],relative_padding=(.3, .3), bg_color=BUTTON_COLOR2, on_press=lambda: True, hover_highlight=1, text_size=FONT_SIZE)
            index+=1
            
        for menu in self.food_scroll_menus:
            menu.init_widgets()
            
        self.max_index = len(self.food_scroll_menus) - 1
        
    def find_index_of_food(self, food):
        for index, screen in enumerate(self.nutrient_screens): 
            if screen.food_info.food_name == food:
                return index
            
        print('uh oh')
        return -1
    
    def remove_item(self):
        self.removing_item = True
        self.GameStateManager.current_state = 'name_prompt_screen'
        
    def add_item(self):
        self.adding_item = True
        self.GameStateManager.current_state = 'name_prompt_screen'
    

    def switch_to_nutrient_label(self, index):
        self.GameStateManager.screens_index = index
        self.GameStateManager.current_state = 'nutrient_screens'
          
    def switch_to_main(self):
        self.GameStateManager.current_state = 'main_screen'

    def food_from_index(self, index):
        return self.nutrient_screens[index].food_info.food_name
        
    def run(self, pos:tuple[int,int], click: bool, pressed_keys: list):
        self.display.fill(self.bg_color)
        self.title_menu.draw(pos, click, pressed_keys)
        self.back_menu.draw(pos, click, pressed_keys)
        self.addremove_menu.draw(pos, click, pressed_keys)
        
        if self.food_scroll_index < self.max_index:
            self.next_menu.draw(pos, click, pressed_keys)
        if self.food_scroll_index != 0:
            self.previous_menu.draw(pos, click, pressed_keys)
        
        self.food_scroll_menus[self.food_scroll_index].draw(pos, click, pressed_keys)
        
        
        
        