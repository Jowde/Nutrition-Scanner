from pygame import Vector2, Surface, transform, font, Color, Rect
from pygame.font import Font
from gui_components.button import Button

class Label(Button):
    def __init__(self, menu: Surface, image: Surface = None, relative_size: tuple[float, float] = None, bg_color: Color = Color(255,255,255), relative_padding: tuple[int, int] = (0,0),
                 text: str = '', text_font: Font = None, text_size: int = 32, text_color: Color = Color(0,0,0), hover_highlight: float = 1, border_width: int = 0, border_color:Color = Color(0,0,0)):
        
        super().__init__ (menu=menu, image=image, relative_size=relative_size, bg_color=bg_color, relative_padding=relative_padding, 
                          text=text, text_font=text_font, text_size=text_size, text_color=text_color, hover_highlight=hover_highlight, 
                          on_press=lambda: True, border_color=border_color, border_width=border_width)
        
        

       
        
        
        
        