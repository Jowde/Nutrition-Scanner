import gui_compenonts 
import pygame
from info_handler import InfoHandler
import gui_compenonts.game_state_manager
import gui_compenonts.screen 

POTATO_SCREEN_SIZE = (1024, 600)

class MainScreen(gui_compenonts.Screen):
    def __init__(self, display, GameStateManager: "gui_compenonts.GameStateManager", bg_color: pygame.Color = pygame.Color(255,255,255)):
        super().__init__(display, GameStateManager, bg_color)
        
        self.main_menu = gui_compenonts.Menu(self.display, (.7, .7), bg_color=pygame.Color(125,125,125), layout='vertical')
        
        self.food_list_button = gui_compenonts.Button(self.main_menu, relative_padding=(.2, .2), text='Food List', bg_color=pygame.Color(125,125,200), on_press=self.switch_to_food_list)
        self.setting_button = gui_compenonts.Button(self.main_menu, text = 'Setting', bg_color=pygame.Color(125,125,200), relative_padding=(.2, .2))
        
        self.main_menu.init_widgets()
    
    def switch_to_food_list(self):
        self.GameStateManager.current_state = 'foodlist_screen'

    def run(self, pos: tuple[int,int], click: bool):
        self.display.fill(self.bg_color)
        self.main_menu.draw(pos, click)
        
class FoodListScreen(gui_compenonts.Screen):
    def __init__(self, display, GameStateManager: "gui_compenonts.GameStateManager", bg_color: pygame.Color = pygame.Color(255,255,255)):
        super().__init__(display, GameStateManager, bg_color)
        
        self.title_menu = gui_compenonts.Menu(self.display, relative_size=(.4, .2), position='topcenter')
        self.title_button = gui_compenonts.Button(self.title_menu, relative_padding=(.3, .3), bg_color=pygame.Color(125,125,200), text='Food List', on_press=lambda: True, hover_highlight=1)
        self.title_menu.init_widgets() 
        
        self.back_menu = gui_compenonts.Menu(self.display, relative_size=(.2, .2), position='topleft')
        self.back_button = gui_compenonts.Button(self.back_menu, relative_padding=(.6,.7), bg_color=pygame.Color(125,125,200), on_press=self.switch_to_main, text='Back')
        self.back_menu.init_widgets()
        
        
        self.info_handler = InfoHandler('foods.csv')
        self.info_handler.loadfromfile()
        
        self.food_scroll_menus = []
        self.init_menus()
        self.food_scroll_index = 0
        
        self.next_menu = gui_compenonts.Menu(self.display, relative_size=(.2, .2), position='bottomright')
        self.next_button = gui_compenonts.Button(self.next_menu, relative_padding=(.6,.7), bg_color=pygame.Color(125,125,200), on_press=self.increase_index, text='Next')
        self.next_menu.init_widgets()
        
        self.previous_menu = gui_compenonts.Menu(self.display, relative_size=(.2, .2), position='bottomleft')
        self.previous_button = gui_compenonts.Button(self.previous_menu, relative_padding=(.6,.7), bg_color=pygame.Color(125,125,200), on_press=self.decrease_index, text='Previous')
        self.previous_menu.init_widgets()
    
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
        for food in self.info_handler.food_dict:
            if index == 3:
                self.food_scroll_menus.append(gui_compenonts.Menu(self.display, relative_size=(.7, .7), bg_color=pygame.Color(125,125,125), layout='vertical'))
                index = 0
            gui_compenonts.Button(self.food_scroll_menus[-1], text =f'{food}',relative_padding=(.3, .3), bg_color=pygame.Color(125,125,200), on_press=lambda: True, hover_highlight=1)
            index+=1
        while index <3:
            gui_compenonts.Button(self.food_scroll_menus[-1],relative_padding=(.3, .3), bg_color=pygame.Color(125,125,125), on_press=lambda: True, hover_highlight=1)
            index+=1
        for menu in self.food_scroll_menus:
            menu.init_widgets()

                
    def switch_to_main(self):
        self.GameStateManager.current_state = 'main_screen'
        
    def run(self, pos: tuple[int,int], click: bool):
        keys = pygame.key.get_pressed()
            
                
        self.display.fill(self.bg_color)
        self.title_menu.draw(pos, click)
        self.back_menu.draw(pos, click)
        self.food_scroll_menus[self.food_scroll_index].draw(pos, click)
        
        if self.index_limit_upper:
            self.next_menu.draw(pos, click)
        else:
            self.next_menu.clear()
            
        if self.index_limit_lower:
            self.previous_menu.draw(pos, click)
        else:
            self.previous_menu.clear()
        
class GUI:
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        
        self.display = pygame.display.set_mode(POTATO_SCREEN_SIZE)
        
        self.GSM = gui_compenonts.GameStateManager('main_screen')
        self.MainScreen = MainScreen(self.display, self.GSM)
        self.FoodListScreen = FoodListScreen(self.display, self.GSM)
        self.screens = {'main_screen': self.MainScreen, 'foodlist_screen': self.FoodListScreen}
        
        
        self.running = True
        
        
    def main_loop(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()[0]
            self.screens[self.GSM.current_state].run(pos, click)
            
            pygame.display.update()
        

if __name__ =='__main__':
    gui = GUI()
    gui.main_loop()
        
        
        
    

    