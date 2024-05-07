import gui_compenonts
from info_handler import InfoHandler
import pygame
from screens.NutrientLabelScreen import NutrientLabel 

BUTTON_COLOR1 = pygame.Color(125,125,200)
BUTTON_COLOR2 = pygame.Color(125,125,125)
MENU_COLOR = pygame.Color(125,125,125)
BACKGROUND_COLOR = pygame.Color(255,255,255)
FONT_SIZE = 22


class FoodListScreen(gui_compenonts.Screen):
    def __init__(self, display, GameStateManager: "gui_compenonts.GameStateManager", bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        
        self.title_menu = gui_compenonts.Menu(self.display, relative_size=(.4, .2), position='topcenter')
        self.title_button = gui_compenonts.Button(self.title_menu, relative_padding=(.3, .3), bg_color=BUTTON_COLOR1, text='Food List', on_press=lambda: True, hover_highlight=1, text_size=FONT_SIZE)
        self.title_menu.init_widgets() 
        
        self.back_menu = gui_compenonts.Menu(self.display, relative_size=(.2, .2), position='topleft')
        self.back_button = gui_compenonts.Button(self.back_menu, relative_padding=(.6,.7), bg_color=BUTTON_COLOR1, on_press=self.switch_to_main, text='Back', text_size=FONT_SIZE)
        self.back_menu.init_widgets()
        
        self.nutrient_screens = []
        
        self.info_handler = InfoHandler('foods.csv')
        self.info_handler.loadfromfile()
        
        self.food_scroll_menus = []
        
        self.food_scroll_index = 0
        
        self.next_menu = gui_compenonts.Menu(self.display, relative_size=(.2, .2), position='bottomright')
        self.next_button = gui_compenonts.Button(self.next_menu, relative_padding=(.6,.7), bg_color=BUTTON_COLOR1, on_press=self.increase_index, text='Next', text_size=FONT_SIZE)
        self.next_menu.init_widgets()
        
        self.previous_menu = gui_compenonts.Menu(self.display, relative_size=(.2, .2), position='bottomleft')
        self.previous_button = gui_compenonts.Button(self.previous_menu, relative_padding=(.6,.7), bg_color=BUTTON_COLOR1, on_press=self.decrease_index, text='Previous', text_size=FONT_SIZE)
        self.previous_menu.init_widgets()

        self.addremove_menu = gui_compenonts.Menu(self.display, relative_size=(.2, .2), position='topright', layout='vertical')
        self.add_item = gui_compenonts.Button(self.addremove_menu, relative_padding=(.6, .7), text='Add Item', bg_color=BUTTON_COLOR1, text_size=FONT_SIZE, on_press=self.switch_to_addItem)
        self.remove_item = gui_compenonts.Button(self.addremove_menu, relative_padding=(.6, .7), text="Remove Item", bg_color=BUTTON_COLOR1, text_size=FONT_SIZE, on_press=self.remove_item)
        self.addremove_menu.init_widgets()

        self.init_menus()

        

    

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
        for food in self.info_handler.food_dict:
            if index == 3:
                self.food_scroll_menus.append(gui_compenonts.Menu(self.display, relative_size=(.7, .7), bg_color=MENU_COLOR, layout='vertical'))
                index = 0
            print(self.info_handler.food_from_dict(food))
            print(food)
            self.nutrient_screens.append(NutrientLabel(self.display, self.GameStateManager, self.info_handler.food_from_dict(food)))
            
            on_press_func = lambda: self.switch_to_nutrient_label(len(self.nutrient_screens) - 1)
            
            gui_compenonts.Button(self.food_scroll_menus[-1], text =f'{food}', relative_padding=(.3, .3), bg_color=pygame.Color(125,125,200), on_press=on_press_func, hover_highlight=1.25, text_size=FONT_SIZE)
            
            index+=1
            
            
        while index <3:
            gui_compenonts.Button(self.food_scroll_menus[-1],relative_padding=(.3, .3), bg_color=BUTTON_COLOR2, on_press=lambda: True, hover_highlight=1, text_size=FONT_SIZE)
            index+=1
            
        for menu in self.food_scroll_menus:
            menu.init_widgets()
    
    def remove_item(self):
        foodName = input("What food item do you want to remove")
        foodItem = self.info_handler.food_from_dict(foodName)
        self.info_handler.remove_item(foodItem)
        
        self.food_scroll_menus.remove(self.food_scroll_menus[0])
        self.food_scroll_menus.remove(self.food_scroll_menus[len(self.food_scroll_menus) -1 ])
        

    def switch_to_addItem(self):
        self.GameStateManager.current_state = 'add_item_screen'

    def switch_to_nutrient_label(self, index):
        self.GameStateManager.index = index
        self.GameStateManager.current_state = 'nutrient_screens'
          
    def switch_to_main(self):
        self.GameStateManager.current_state = 'main_screen'
        
    def run(self, pos: tuple[int,int], click: bool):
        keys = pygame.key.get_pressed()
            
                
        self.display.fill(self.bg_color)
        self.title_menu.draw(pos, click)
        self.back_menu.draw(pos, click)
        self.food_scroll_menus[self.food_scroll_index].draw(pos, click)
        self.addremove_menu.draw(pos, click)


        if self.index_limit_upper:
            self.next_menu.draw(pos, click)
        else:
            self.next_menu.clear()
            
        if self.index_limit_lower:
            self.previous_menu.draw(pos, click)
        else:
            self.previous_menu.clear()