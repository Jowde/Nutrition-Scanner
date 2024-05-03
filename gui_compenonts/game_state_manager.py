class GameStateManager:
    def __init__(self, inital_state: str):
        self.current_state = inital_state
        
    @property
    def current_state(self) -> str:
        return self._current_state
    
    @current_state.setter
    def current_state(self, state: str):
        self._current_state = state