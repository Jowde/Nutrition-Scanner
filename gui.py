import gui_components 
import pygame
import gui_components.game_state_manager
import gui_components.screen 
import screens
import screens.AddItemScreen
POTATO_SCREEN_SIZE = (1024, 600)
FPS = 60
class GUI:
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        
        self.display = pygame.display.set_mode(POTATO_SCREEN_SIZE)
        
        
        self.clock = pygame.time.Clock()
        self.GSM = gui_components.GameStateManager('main_screen')
        self.MainScreen = screens.MainScreen(self.display, self.GSM)
        self.FoodListScreen = screens.FoodListScreen(self.display, self.GSM)
        self.AddItemScreen = screens.AddItemScreen(self.display, self.GSM)
        self.ChooseWeightScreen = screens.ChooseWeightScreen(self.display, self.GSM)
        self.name_prompt_screen = screens.NamePromptScreen(self.display, self.GSM, self.FoodListScreen)
        
        self.screens = {'main_screen': self.MainScreen, 
                        'foodlist_screen': self.FoodListScreen, 
                        'nutrient_screens': self.FoodListScreen.nutrient_screens, 
                        'add_item_screen': self.AddItemScreen, 
                        'choose_weight_screen': self.ChooseWeightScreen,
                        'name_prompt_screen': self.name_prompt_screen}
        
        self.max_click_cooldown = 45
        self.click_cooldown = 0
        self.running = True
        
    @property
    def click_cooldown(self):
        return self._click_cooldown
    @click_cooldown.setter
    def click_cooldown(self, value):
        if value >= 0:
            self._click_cooldown = value
        else:
            self._click_cooldown = 0
        
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
            
            if self.click_cooldown<=0:
                click = pygame.mouse.get_pressed()[0]
            else:
                click = False
                
            if self.GSM.current_state != 'nutrient_screens':
                self.screens[self.GSM.current_state].run(pos, click, pressed_keys)
            else:
                self.screens['nutrient_screens'] = self.FoodListScreen.nutrient_screens
                self.screens['nutrient_screens'][self.GSM.screens_index].run(pos, click, pressed_keys)
                    
                        
            pressed_keys = []
            
            if click:
                self.click_cooldown = self.max_click_cooldown
            self.click_cooldown -=1
            
            self.clock.tick(FPS)
            pygame.display.update()
        
if __name__ =='__main__':
    gui = GUI()
    gui.main_loop()
        