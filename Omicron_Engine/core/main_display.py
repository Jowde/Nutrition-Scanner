import pygame
import sys
from Omicron_Engine.core.game_state_manager import GameStateManager
import os
import importlib.util
from pygame import Vector2

class MainDisplay:
    '''
    The main display for the pygame project
    '''
    def __init__(self, current_screen: str, display_size: tuple[int, int] = (720, 720), FPS: int = 60, display_title:str = '', quick_boot: bool = False):
        self.running = True
        self.GameStateManager = GameStateManager(current_screen)
        
        if quick_boot:
            pygame.display.init()
            pygame.font.init()
        else:
            pygame.init()
        
        self.size = Vector2(display_size)
        self.main_display = pygame.display.set_mode(self.size)
        self.FPS = FPS
        
        self.states = {}
        self.define_screens()

        pygame.display.set_caption(display_title)
        self.clock = pygame.time.Clock()
        
        
    
    def define_screens(self):
        screens_folder = os.path.join('screens')
        for file in os.listdir(screens_folder):
            if file[-10:] == '_screen.py':
                class_name = file[:-10].capitalize() + 'Screen'
                spec = importlib.util.spec_from_file_location(class_name, os.path.join('screens', file))
                screen_module =  importlib.util.module_from_spec(spec)
                spec.loader.exec_module(screen_module)
                screen_class = getattr(screen_module, class_name)
                self.states[file[0:-3]] = screen_class(self.main_display, self.GameStateManager)
                
    def main_loop(self):
        while self.running:
            current_screen = self.states[self.GameStateManager.current_state]
            events = pygame.event.get()
            current_screen.run(events)
            
            for event in events: #This is jank I'll need to fix later (searches through events twice)
                if event.type == pygame.QUIT:
                    self.running = False
                    
            pygame.display.update()
            self.clock.tick(self.FPS)
            
        pygame.quit()
        sys.exit()


        
    
