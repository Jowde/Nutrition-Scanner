import Omicron_Engine as OE
import pygame
from pygame import Color
class GameScreen(OE.Screen):
    def __init__(self, display, GameStateManager: "OE.GameStateManager"):
        super().__init__(display, GameStateManager, Color(0,0,0))
        self.game_menu = OE.Menu(
                                display = self.display,
                                position='topcenter',
                                relative_size=(.4, .4),
                                layout="horizontal",
                                bg_color=Color(125,125,125)
                                 )
        
        self.real_start_game_button = OE.Button(self.game_menu,
                                                text = 'Hello World',
                                                bg_color = Color(255, 125, 125),
                                                on_press= lambda : self.switch_state('start_screen') )
        self.another_button = OE.Button(
                                        self.game_menu,
                                        text = 'Goodbye World',
                                        bg_color = Color(255, 125, 125),
                                        on_press= lambda : self.switch_state('start_screen'), 
                                        relative_padding=(.2, .1)
                                        )
        
        self.game_menu.add_widget(self.real_start_game_button)
        self.game_menu.add_widget(self.another_button)
        self.game_menu.init_widgets()
        
        
    
    def run(self, events = None):
        self.display.fill(self.bg_color)
        click = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            
        self.game_menu.draw(pygame.mouse.get_pos(), click)
        