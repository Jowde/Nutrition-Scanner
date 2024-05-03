from pygame import Surface, Color
from gui_compenonts.button import Button
from pygame.font import Font
import pygame 

class TextInput(Button):
    def __init__(self, menu: Surface, image: Surface = None, relative_size: tuple[float, float] = None, bg_color: Color = Color(0,0,0), relative_padding: tuple[int, int] = (0,0),
                 text: str = '', text_font: Font = None, text_size: int = 32, text_color: Color = Color(0,0,0), hover_highlight: float = 1.125, on_press = None):
        self.selected = False
        super().__init__(menu=menu, image = image, relative_size=relative_size, bg_color=bg_color, relative_padding=relative_padding, 
                         text=text, text_font=text_font, text_size=text_size, text_color= text_color, hover_highlight=hover_highlight, on_press = self.change_selected)
    
    def change_selected_to_true(self):
        self.selected = True
        
    def change_selected_to_false(self):
        self.selected = False
    
    def input_handler(self):
        if self.selected:
            keys = pygame.key.get_pressed()
            for key in keys:
                if key == pygame.K_DELETE:
                    if len(self.text) > 0:
                        self.text = self.text[:-1]
                elif key == pygame.K_q:
                    self.text += 'q'
                    
            
            
            
