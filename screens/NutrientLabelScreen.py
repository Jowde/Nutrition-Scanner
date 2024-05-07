import gui_components
import pygame
from food import Food

BACKGROUND_COLOR = pygame.Color(255,255,255)
MENU_COLOR = pygame.Color(125,125,125)
BUTTON_COLOR = pygame.Color(125,125,200)
FONT_SIZE = 22

class NutrientLabel(gui_components.Screen):
    def __init__(self, display, GameStateManager: "gui_components.GameStateManager", food_info: Food, bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        self.food_info = food_info
        
        self.main_menu = gui_components.Menu(self.display, relative_size=(.8, .8), bg_color=MENU_COLOR, layout='horizontal')
        self.leftSideMenu = gui_components.Menu(self.main_menu, relative_size=(.3,.8), bg_color=MENU_COLOR, layout='vertical', position='centerleft')
        self.middleMenu = gui_components.Menu(self.main_menu, relative_size=(.3, .8), bg_color=MENU_COLOR, layout='vertical', position='center')
        self.rightSideMenu = gui_components.Menu(self.main_menu, relative_size=(.3, .8), bg_color=MENU_COLOR, layout='vertical', position='centerright')
        
        self.titleMenu = gui_components.Menu(self.display, relative_size=(.5, .075), position='topcenter')
        self.titleLabel = gui_components.Label(self.titleMenu, relative_padding=(0,0), text=f'{food_info.food_name}')
        
        
        self.servingSizeBtn = gui_components.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Serving Size", hover_highlight=1, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.caloriesBtn = gui_components.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Calories", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fatBtn = gui_components.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Fat", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.saturated_fatBtn = gui_components.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Saturated Fats", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.unsaturated_fatBtn = gui_components.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Unsaturated Fats", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.carbsBtn = gui_components.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Carbohydrates", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fiberBtn = gui_components.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Fiber", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.sugarsBtn = gui_components.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Sugars", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.added_sugarBtn = gui_components.Button(self.leftSideMenu, relative_padding=(.1, .1), text=f'Added Sugars', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.proteinBtn = gui_components.Button(self.leftSideMenu, relative_padding=(.1, .1), text="Protein", hover_highlight=1, on_press= lambda : True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)

        self.servingSizeBtnVal = gui_components.Button(self.middleMenu, relative_padding=(.1, .1), text=f'{food_info.serving_size}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.caloriesBtnVal = gui_components.Button(self.middleMenu, relative_padding=(.1, .1), text=f'{food_info.calories}', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fatBtnVal = gui_components.Button(self.middleMenu, relative_padding=(.1, .1), text=f'{food_info.fat}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.saturated_fatBtnVal =gui_components.Button(self.middleMenu, relative_padding=(.1, .1), text=f'{food_info.saturated_fat}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.unsaturated_fatBtnVal = gui_components.Button(self.middleMenu, relative_padding=(.1, .1), text=f'{food_info.unsaturated_fat}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.carbsBtnVal = gui_components.Button(self.middleMenu, relative_padding=(.1, .1), text=f'{food_info.carbs}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fiberBtnVal = gui_components.Button(self.middleMenu, relative_padding=(.1, .1), text=f'{food_info.fiber}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.sugarsBtnVal = gui_components.Button(self.middleMenu, relative_padding=(.1, .1), text=f'{food_info.sugars}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.added_sugarBtnVal = gui_components.Button(self.middleMenu, relative_padding=(.1, .1), text=f'{food_info.added_sugars}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.proteinBtnVal = gui_components.Button(self.middleMenu, relative_padding=(.1, .1), text=f'{food_info.protein}g', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        
        self.servingSizeEditBtn = gui_components.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'edit', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.caloriesEditBtn = gui_components.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'edit', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fatEditBtn = gui_components.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'edit', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.saturated_fatEditBtn =gui_components.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'edit', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.unsaturated_fatEditBtn = gui_components.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'edit', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.carbsEditBtn = gui_components.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'edit', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fiberEditBtn = gui_components.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'edit', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.sugarsEditBtn = gui_components.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'edit', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.added_sugarEditBtn = gui_components.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'edit', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.proteinEditBtn = gui_components.Button(self.rightSideMenu, relative_padding=(.1, .1), text=f'edit', hover_highlight=1, on_press=lambda: True, bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        
        self.back_menu = gui_components.Menu(self.display, relative_size=(.1, .1), position='topleft')
        self.back_button = gui_components.Button(self.back_menu, relative_padding=(.2,.3), bg_color=BUTTON_COLOR, on_press=self.switch_to_food_list, text='Back')
        self.back_menu.init_widgets()
        
        #might be able to call these functions when a widget is added Need to look into - Jude (note to self)
        self.leftSideMenu.init_widgets()
        self.middleMenu.init_widgets()
        self.rightSideMenu.init_widgets()
        
        self.main_menu.init_widgets()
        self.titleMenu.init_widgets()
        
    def run(self, pos, click):
        
        self.display.fill(self.bg_color)
        self.main_menu.draw(pos, click)
        
        # make menus that are in menus automatically draw- Jude (note to self) 
        self.leftSideMenu.draw(pos,click)
        self.middleMenu.draw(pos,click)
        self.rightSideMenu.draw(pos, click)
        
        self.back_menu.draw(pos, click)
        self.titleMenu.draw(pos, click)
        
    def switch_to_food_list(self):
        self.GameStateManager.current_state = 'foodlist_screen'
