import gui_components
import pygame
from food import Food
from info_handler import InfoHandler

BACKGROUND_COLOR = pygame.Color(255,255,255)
MENU_COLOR = pygame.Color(125,125,125)
BUTTON_COLOR = pygame.Color(125,125,200)
FONT_SIZE = 22

class NutrientLabel(gui_components.Screen):
    def __init__(self, display, GameStateManager: "gui_components.GameStateManager", food_info: Food, infohandler: InfoHandler, bg_color: pygame.Color = BACKGROUND_COLOR):
        super().__init__(display, GameStateManager, bg_color)
        self.food_info = food_info
        self.info_handler = infohandler
        
        self.main_menu = gui_components.Menu(self.display, relative_size=(.4, .8), bg_color=MENU_COLOR, layout='horizontal')
        self.leftSideMenu = gui_components.Menu(self.main_menu, relative_size=(.5,.8), bg_color=MENU_COLOR, layout='vertical', position='centerleft')
        self.rightSideMenu = gui_components.Menu(self.main_menu, relative_size=(.5, .8), bg_color=MENU_COLOR, layout='vertical', position='centerright')
        
        self.titleMenu = gui_components.Menu(self.display, relative_size=(.5, .075), position='topcenter')
        self.titleLabel = gui_components.Label(self.titleMenu, relative_padding=(0,0), text=f'{food_info.food_name}')
        
        
        self.servingSizeBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Serving Size",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.caloriesBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Calories",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fatBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Fat",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.saturated_fatBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Saturated Fats",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.unsaturated_fatBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Unsaturated Fats", bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.carbsBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Carbohydrates", bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fiberBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Fiber",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.sugarsBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Sugars",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.added_sugarBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text=f'Added Sugars', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.proteinBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Protein",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)

        self.servingSizeBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.serving_size}g', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.caloriesBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.calories}', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fatBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.fat}g',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.saturated_fatBtnVal =gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.saturated_fat}g', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.unsaturated_fatBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.unsaturated_fat}g',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.carbsBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.carbs}g',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fiberBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.fiber}g',   bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.sugarsBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.sugars}g',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.added_sugarBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.added_sugars}g',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.proteinBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{food_info.protein}g', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        
        
        self.back_menu = gui_components.Menu(self.display, relative_size=(.1, .1), position='topleft')
        self.back_button = gui_components.Button(self.back_menu, relative_padding=(.2,.3), bg_color=BUTTON_COLOR, on_press=self.switch_to_food_list, text='Back')
        self.back_menu.init_widgets()
        
        self.edit_menu = gui_components.Menu(self.display, relative_size=(.1, .1), position='topright')
        self.edit_button = gui_components.Button(self.edit_menu, relative_padding=(.2,.3), bg_color=BUTTON_COLOR, on_press=self.enable_edit_mode, text='Edit')
        self.edit_menu.init_widgets()
        #might be able to call these functions when a widget is added Need to look into - Jude (note to self)
        self.leftSideMenu.init_widgets()
        self.rightSideMenu.init_widgets()
        
        self.main_menu.init_widgets()
        self.titleMenu.init_widgets()
    
    def reinit(self, food_info: Food):
        self.food_info = food_info
        
        self.main_menu = gui_components.Menu(self.display, relative_size=(.4, .8), bg_color=MENU_COLOR, layout='horizontal')
        self.leftSideMenu = gui_components.Menu(self.main_menu, relative_size=(.5,.8), bg_color=MENU_COLOR, layout='vertical', position='centerleft')
        self.rightSideMenu = gui_components.Menu(self.main_menu, relative_size=(.5, .8), bg_color=MENU_COLOR, layout='vertical', position='centerright')
        
        self.titleMenu = gui_components.Menu(self.display, relative_size=(.5, .075), position='topcenter')
        self.titleLabel = gui_components.Label(self.titleMenu, relative_padding=(0,0), text=f'{self.food_info.food_name}')
        
        
        self.servingSizeBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Serving Size",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.caloriesBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Calories",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fatBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Fat",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.saturated_fatBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Saturated Fats",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.unsaturated_fatBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Unsaturated Fats", bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.carbsBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Carbohydrates", bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fiberBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Fiber",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.sugarsBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Sugars",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.added_sugarBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text=f'Added Sugars', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.proteinBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Protein",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)

        self.servingSizeBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.serving_size}g', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.caloriesBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.calories}', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fatBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.fat}g',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.saturated_fatBtnVal =gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.saturated_fat}g', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.unsaturated_fatBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.unsaturated_fat}g',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.carbsBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.carbs}g',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fiberBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.fiber}g',   bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.sugarsBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.sugars}g',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.added_sugarBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.added_sugars}g',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.proteinBtnVal = gui_components.Label(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.protein}g', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        
        self.back_menu = gui_components.Menu(self.display, relative_size=(.1, .1), position='topleft')
        self.back_button = gui_components.Button(self.back_menu, relative_padding=(.2,.3), bg_color=BUTTON_COLOR, on_press=self.switch_to_food_list, text='Back')
        self.back_menu.init_widgets()
        
        self.edit_menu = gui_components.Menu(self.display, relative_size=(.1, .1), position='topright')
        self.edit_button = gui_components.Button(self.edit_menu, relative_padding=(.2,.3), bg_color=BUTTON_COLOR, on_press=self.enable_edit_mode, text='Edit')
        self.edit_menu.init_widgets()
        #might be able to call these functions when a widget is added Need to look into - Jude (note to self)
        self.leftSideMenu.init_widgets()
        self.rightSideMenu.init_widgets()
        
        self.main_menu.init_widgets()
        self.titleMenu.init_widgets()

    def enable_edit_mode(self):
        self.main_menu = gui_components.Menu(self.display, relative_size=(.4, .8), bg_color=MENU_COLOR, layout='horizontal')
        self.leftSideMenu = gui_components.Menu(self.main_menu, relative_size=(.5,.8), bg_color=MENU_COLOR, layout='vertical', position='centerleft')
        self.rightSideMenu = gui_components.Menu(self.main_menu, relative_size=(.5, .8), bg_color=MENU_COLOR, layout='vertical', position='centerright')
        
        self.titleMenu = gui_components.Menu(self.display, relative_size=(.5, .075), position='topcenter')
        self.titleLabel = gui_components.Label(self.titleMenu, relative_padding=(0,0), text=f'{self.food_info.food_name}')
        
        self.servingSizeBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Serving Size",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.caloriesBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Calories",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fatBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Fat",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.saturated_fatBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Saturated Fats",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.unsaturated_fatBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Unsaturated Fats", bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.carbsBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Carbohydrates", bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fiberBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Fiber",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.sugarsBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Sugars",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.added_sugarBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text=f'Added Sugars', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.proteinBtn = gui_components.Label(self.leftSideMenu, relative_padding=(.1, .1), text="Protein",  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)

        self.servingSizeBtnVal = gui_components.TextInput(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.serving_size}', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.caloriesBtnVal = gui_components.TextInput(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.calories}', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fatBtnVal = gui_components.TextInput(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.fat}',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.saturated_fatBtnVal =gui_components.TextInput(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.saturated_fat}', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.unsaturated_fatBtnVal = gui_components.TextInput(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.unsaturated_fat}',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.carbsBtnVal = gui_components.TextInput(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.carbs}',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.fiberBtnVal = gui_components.TextInput(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.fiber}',   bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.sugarsBtnVal = gui_components.TextInput(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.sugars}',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.added_sugarBtnVal = gui_components.TextInput(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.added_sugars}',  bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        self.proteinBtnVal = gui_components.TextInput(self.rightSideMenu, relative_padding=(.1, .1), text=f'{self.food_info.protein}', bg_color=BUTTON_COLOR, text_size=FONT_SIZE)
        
        self.back_menu = gui_components.Menu(self.display, relative_size=(.1, .1), position='topleft')
        self.back_button = gui_components.Button(self.back_menu, relative_padding=(.2,.3), bg_color=BUTTON_COLOR, on_press=self.switch_to_food_list, text='Back')
        self.back_menu.init_widgets()
        
        self.edit_menu = gui_components.Menu(self.display, relative_size=(.1, .1), position='topright')
        self.edit_button = gui_components.Button(self.edit_menu, relative_padding=(.2,.3), bg_color=BUTTON_COLOR, on_press=self.make_new_food, text='Confirm')
        self.edit_menu.init_widgets()
        #might be able to call these functions when a widget is added Need to look into - Jude (note to self)
        self.leftSideMenu.init_widgets()
        self.rightSideMenu.init_widgets()
        
        self.main_menu.init_widgets()
        self.titleMenu.init_widgets()
        
    def make_new_food(self):
    
            new_food_info = Food(food_name=self.food_info.food_name,
                                 serving_size=self.servingSizeBtnVal.text,
                                 calories=self.caloriesBtnVal.text, 
                                 fat=self.fatBtnVal.text, 
                                 saturated_fat=self.saturated_fatBtnVal.text, 
                                 unsaturated_fat=self.unsaturated_fatBtnVal.text,
                                 carbs=self.carbsBtnVal.text, 
                                 fiber=self.fiberBtnVal.text, 
                                 sugars=self.sugarsBtnVal.text, 
                                 added_sugars=self.added_sugarBtnVal.text,
                                 protein = self.proteinBtnVal.text)
            self.reinit(new_food_info)
            self.info_handler.add_item(new_food_info)
            self.info_handler.savetofile()
            self.info_handler.loadfromfile()
    
        
        
    def run(self, pos:tuple[int,int], click: bool, pressed_keys: list):
        
        self.display.fill(self.bg_color)
        self.main_menu.draw(pos, click, pressed_keys)
        
        # make menus that are in menus automatically draw- Jude (note to self) 
        self.leftSideMenu.draw(pos,click, pressed_keys)
        self.rightSideMenu.draw(pos, click, pressed_keys)
        
        self.back_menu.draw(pos, click, pressed_keys)
        self.edit_menu.draw(pos, click, pressed_keys)
        self.titleMenu.draw(pos, click, pressed_keys)
        
        
    def switch_to_food_list(self):
        self.GameStateManager.current_state = 'foodlist_screen'
