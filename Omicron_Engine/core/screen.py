from abc import ABC, abstractmethod
from Omicron_Engine.core.game_state_manager import GameStateManager
from pygame import Color
from pygame.sprite import Group
class Screen(ABC):
    def __init__(self, display, GameStateManager: "GameStateManager", bg_color: Color = Color(255,255,255)):
        self.display = display
        self.GameStateManager = GameStateManager
        self.bg_color = bg_color
        
    @abstractmethod
    def run(self, events = None):
        raise NotImplementedError
    
    def switch_state(self, gamestate: str):
        self.GameStateManager.current_state = gamestate
        
    
        
        