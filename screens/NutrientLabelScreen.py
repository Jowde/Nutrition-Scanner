import gui_compenonts
import pygame
from food import Food

BACKGROUND_COLOR = pygame.Color(255,255,255)
MENU_COLOR = pygame.Color(125,125,125)

class NutrientLabel(gui_compenonts.Screen):
    def __init__(self, display, GameStateManager: "gui_compenonts.GameStateManager", food_info: Food, bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        self.food_info = food_info
        
        self.main_menu = gui_compenonts.Menu(self.display, relative_size=(.8, .8), bg_color=MENU_COLOR, layout='horizontal')
        self.leftSideMenu = gui_compenonts.Menu(self.main_menu, relative_size=(.6,.8), bg_color=MENU_COLOR, layout='vertical')
        self.rightSideMenu = gui_compenonts.Menu(self.main_menu, relative_size=(.8, .8), bg_color=MENU_COLOR, layout='vertical')

        self.servingSizeBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.2, .2), text="Serving Size", hover_highlight=1)
        self.caloriesBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.2, .2), text="Calories", hover_highlight=1, on_press= lambda : True)
        self.fatBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.2, .2), text="Fat", hover_highlight=1, on_press= lambda : True)
        self.saturated_fatBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.2, .2), text="Saturated Fats", hover_highlight=1, on_press= lambda : True)
        self.unsaturated_fatBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.2, .2), text="Unsaturated Fats", hover_highlight=1, on_press= lambda : True)
        self.carbsBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.2, .2), text="Carbohydrates", hover_highlight=1, on_press= lambda : True)
        self.fiberBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.2, .2), text="Fiber", hover_highlight=1, on_press= lambda : True)
        self.sugarsBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.2, .2), text="Sugars", hover_highlight=1, on_press= lambda : True)
        self.proteinBtn = gui_compenonts.Button(self.leftSideMenu, relative_padding=(.2, .2), text="Protein", hover_highlight=1, on_press= lambda : True)

        self.servingSizeBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.2, .2), text=f'{food_info.serving_size}g', hover_highlight=1, on_press=lambda: True)
        self.caloriesBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.2, .2), text=f'{food_info.calories}g', hover_highlight=1, on_press=lambda: True)
        self.fatBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.2, .2), text=f'{food_info.fat}g', hover_highlight=1, on_press=lambda: True)
        self.saturated_fatBtnVal =gui_compenonts.Button(self.rightSideMenu, relative_padding=(.2, .2), text=f'{food_info.saturated_fat}g', hover_highlight=1, on_press=lambda: True)
        self.unsaturated_fatBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.2, .2), text=f'{food_info.unsaturated_fat}g', hover_highlight=1, on_press=lambda: True)
        self.carbsBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.2, .2), text=f'{food_info.carbs}g', hover_highlight=1, on_press=lambda: True)
        self.fiberBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.2, .2), text=f'{food_info.fiber}g', hover_highlight=1, on_press=lambda: True)
        self.sugarsBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.2, .2), text=f'{food_info.sugars}g', hover_highlight=1, on_press=lambda: True)
        self.proteinBtnVal = gui_compenonts.Button(self.rightSideMenu, relative_padding=(.2, .2), text=f'{food_info.protein}g', hover_highlight=1, on_press=lambda: True)

        self.main_menu.init_widgets()
        
    def run(self, pos, click):
        self.display.fill(self.bg_color)
        self.main_menu.draw(pos, click)
