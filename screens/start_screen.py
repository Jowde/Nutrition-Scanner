import Omicron_Engine as OE
import pygame
from pygame import Vector2, Color

class StartScreen(OE.Screen):
    def __init__(self, display, GameStateManager: "OE.GameStateManager"):
        super().__init__(display, GameStateManager, Color(255,255,255))

        self.display.fill(self.bg_color)
        
        self.main_menu = OE.Menu(
                                    self.display, relative_size=(.75, .5), 
                                    layout='vertical',
                                    bg_color= Color(123,125,125) 
                                 )
         
        self.start_button = OE.Button(
                                        menu = self.main_menu, 
                                        bg_color = Color((125,125,255)), 
                                        text = 'Start Game',
                                        on_press= lambda : self.switch_state('game_screen')
                                    )
        
        
        self.test_label = OE.Label(
                                        menu = self.main_menu, 
                                        bg_color = Color((125,255,255)),
                                        text = 'Label test',
                                        relative_padding=(.2,.2)
                                        
                                    )
                       
        self.main_menu.add_widget(self.start_button)
        self.main_menu.add_widget(self.test_label)
        
        self.main_menu.init_widgets()
        
        
        
    def run(self, events = None):
        self.display.fill(self.bg_color)
        
        click = False
        for event in events:
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        pos = pygame.mouse.get_pos() 
        
      
        self.main_menu.draw(pos, click)
        
        
    
    