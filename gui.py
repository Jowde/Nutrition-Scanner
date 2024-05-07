import gui_components 
import pygame
import gui_components.game_state_manager
import gui_components.screen 
import screens
import screens.AddItemScreen
POTATO_SCREEN_SIZE = (1024, 600)

class GUI:
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        
        self.display = pygame.display.set_mode(POTATO_SCREEN_SIZE)
        
        self.GSM = gui_components.GameStateManager('main_screen')
        self.MainScreen = screens.MainScreen(self.display, self.GSM)
        self.FoodListScreen = screens.FoodListScreen(self.display, self.GSM)
        self.AddItemScreen = screens.AddItemScreen(self.display, self.GSM)
        self.ChooseWeightScreen = screens.ChooseWeightScreen(self.display, self.GSM)
        self.screens = {'main_screen': self.MainScreen, 'foodlist_screen': self.FoodListScreen, 'nutrient_screens': self.FoodListScreen.nutrient_screens, 'add_item_screen': self.AddItemScreen, 'choose_weight_screen': self.ChooseWeightScreen}
        
        self.running = True
        
    def main_loop(self):
        pressed_keys = []
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    pressed_keys.append(event)
            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()[0]
            if self.GSM.current_state != 'nutrient_screens':
                self.screens[self.GSM.current_state].run(pos, click, pressed_keys)
            else:
                self.screens['nutrient_screens'][self.GSM.screens_index].run(pos, click, pressed_keys)
            pressed_keys = []
            pygame.display.update()
        
if __name__ =='__main__':
    gui = GUI()
    gui.main_loop()
        
        
    

    