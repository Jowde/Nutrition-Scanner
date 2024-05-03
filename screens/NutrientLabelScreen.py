import gui_compenonts
import pygame
from food import Food

BACKGROUND_COLOR = pygame.Color(255,255,255)
MENU_COLOR = pygame.Color(125,125,125)
BUTTON_COLOR = pygame.Color(125,125,200)

class NutrientLabel(gui_compenonts.Screen):
    def __init__(self, display, GameStateManager: "gui_compenonts.GameStateManager", food_info: Food, bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        self.food_info = food_info
        
        self.main_menu = gui_compenonts.Menu(self.display, relative_size=(.8, .8), bg_color=MENU_COLOR, layout='horizontal')
        self.leftSideMenu = gui_compenonts.Menu(self.main_menu, relative_size=(.3,.8), bg_color=MENU_COLOR, layout='vertical', position='centerleft')
        self.rightSideMenu = gui_compenonts.Menu(self.main_menu, relative_size=(.3, .8), bg_color=MENU_COLOR, layout='vertical', position='centerright')

        self.servingSizeBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Serving Size", hover_highlight=1, bg_color=BUTTON_COLOR)
        self.caloriesBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Calories", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR)
        self.fatBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Fat", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR)
        self.saturated_fatBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Saturated Fats", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR)
        self.unsaturated_fatBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Unsaturated Fats", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR)
        self.carbsBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Carbohydrates", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR)
        self.fiberBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Fiber", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR)
        self.sugarsBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Sugars", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR)
        self.added_sugarBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.1, .1), text=f'Added Sugars', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR)
        self.proteinBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Protein", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR)

        self.servingSizeBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.serving_size}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR)
        self.caloriesBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.calories}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR)
        self.fatBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.fat}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR)
        self.saturated_fatBtnVal =gui_compenonts.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.saturated_fat}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR)
        self.unsaturated_fatBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.unsaturated_fat}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR)
        self.carbsBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.carbs}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR)
        self.fiberBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.fiber}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR)
        self.sugarsBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.sugars}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR)
        self.added_sugarBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.added_sugars}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR)
        self.proteinBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.protein}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR)
        
        
        self.back_menu = gui_compenonts.Menu(self.display, relative_size=(.1, .1), position='topleft')
        self.back_button = gui_compenonts.Button(self.back_menu, relative_padding=(.2,.3), bg_color=BUTTON_COLOR, on_press=self.switch_to_food_list, text='Back')
        self.back_menu.init_widgets()
        
        self.leftSideMenu.init_widgets()
        self.rightSideMenu.init_widgets()
        self.main_menu.init_widgets()
        
    def run(self, pos, click):
        self.display.fill(self.bg_color)
        self.main_menu.draw(pos, click)
        self.leftSideMenu.draw(pos,click)
        self.rightSideMenu.draw(pos,click)
        self.back_menu.draw(pos, click)
        
    def switch_to_food_list(self):
        self.GameStateManager.current_state = 'foodlist_screen'
