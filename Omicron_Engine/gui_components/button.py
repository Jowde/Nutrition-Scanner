from pygame import Surface, Color
from Omicron_Engine.gui_components.label import Label
from pygame.font import Font

class Button(Label):
    def __init__(self, menu: Surface, image: Surface = None, relative_size: tuple[float, float] = None, bg_color: Color = Color(0,0,0), relative_padding: tuple[int, int] = (0,0),
                 text: str = '', text_font: Font = None, text_size: int = 32, text_color: Color = Color(0,0,0), hover_highlight: float = 1.125, on_press = None):
        
        super().__init__(menu=menu, image = image, relative_size=relative_size, bg_color=bg_color, relative_padding=relative_padding, 
                         text=text, text_font=text_font, text_size=text_size, text_color=text_color)
        
        self.hover_highlight = hover_highlight
        self.on_press = on_press
        
    def is_hovered_over(self, pos) -> bool:
            if self.rect.collidepoint(pos):
                self.image.fill(
                        Color(  
                            (self.bg_color.r * self.hover_highlight if self.bg_color.r * self.hover_highlight < 255 else 255,
                            self.bg_color.g * self.hover_highlight if self.bg_color.g * self.hover_highlight < 255 else 255, 
                            self.bg_color.b * self.hover_highlight if self.bg_color.b * self.hover_highlight < 255 else 255)
                            )
                        )
                return True
                
            else:
                self.image.fill(self.bg_color)
                return False
    
    def pressed(self):
        self.on_press()
        