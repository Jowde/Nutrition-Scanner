from pygame import Surface, Color, Vector2, font, transform, Rect, draw
from pygame.font import Font
from pygame.sprite import Sprite

class Button(Sprite):
    def __init__(self, menu: Surface, image: Surface = None, relative_size: tuple[float, float] = None, bg_color: Color = Color(255,255,255), relative_padding: tuple[int, int] = (0,0), 
                 text: str = '', text_font: Font = None, text_size: int = 32, text_color: Color = Color(0,0,0), 
                 hover_highlight: float = 1.125, on_press = None, border_width: int = 0, border_color: Color = Color(0,0,0)):
        
        self.menu = menu
        self.bg_image = image
        self.relative_size = relative_size
        self.bg_color = bg_color
        self.position = Vector2((0,0))
        self.size = Vector2((0,0))
        self.relative_padding = Vector2(relative_padding)
    
        self.text = text
        self.text_font = text_font
        self.text_size = text_size
        self.text_color = text_color
        
        Sprite.__init__(self, self.menu.widget_group)
        
        self.hover_highlight = hover_highlight
        self.on_press = on_press
        
        self.border_width = border_width
        self.border_color = border_color
        
        
    def is_hovered_over(self, pos) -> bool:
            if self.rect.collidepoint(pos):
                self.highlight()
                return True
                
            else:
                self.image.fill(self.bg_color)
                return False
            
    def highlight(self):
        self.image.fill(
                        Color(  
                            (self.bg_color.r * self.hover_highlight if self.bg_color.r * self.hover_highlight < 255 else 255,
                            self.bg_color.g * self.hover_highlight if self.bg_color.g * self.hover_highlight < 255 else 255, 
                            self.bg_color.b * self.hover_highlight if self.bg_color.b * self.hover_highlight < 255 else 255)
                            )
                        )
    
    def pressed(self):
        self.on_press()
    
    def init_image(self, widget_index: int, total_widgets: int, layout: str):
        '''
        Initatizes image atrribute for the sprite using the info from menu 
        '''
        
        if layout == 'horizontal':
            widget_size = Vector2(int((1/(total_widgets)) * self.menu.size.x), int(self.menu.size.y))
            self.size.update(int((1/(total_widgets)) * self.menu.size.x * (1-self.relative_padding.x) ), int(self.menu.size.y * (1-self.relative_padding.y)))
            
            pad_adjustment_x = (widget_size.x - self.size.x)//2
            pad_adjustment_y = (widget_size.y - self.size.y)//2
            
            self.position.update(widget_index*widget_size.x + pad_adjustment_x, pad_adjustment_y)
            
        elif layout == 'vertical':
            widget_size = Vector2((int(self.menu.size.x), int((1/(total_widgets)) * self.menu.size.y)))
            self.size.update((int(self.menu.size.x * (1-self.relative_padding.x)), int((1/(total_widgets)) * self.menu.size.y * (1-self.relative_padding.y))))
            
            pad_adjustment_x = (widget_size.x - self.size.x)//2
            pad_adjustment_y = (widget_size.y - self.size.y)//2
            
            self.position.update(pad_adjustment_x, widget_index * widget_size.y + pad_adjustment_y)
            
        if self.bg_image:
            self.image = transform.scale(self.bg_image, self.size.xy)

        else:
            self.image = Surface(self.size.xy)
            self.image.fill(self.bg_color)
        
        try:
            self.rect = Rect(
                                (self.position.x + self.menu.rect.left + self.menu.display.rect.left, self.position.y + self.menu.rect.top + self.menu.display.rect.top),
                                (self.size.x, self.size.y)
                            )
        except:
            self.rect = Rect(
                            (self.position.x + self.menu.rect.left, self.position.y + self.menu.rect.top),
                            (self.size.x, self.size.y)
                        )
        
        self.init_text()
            
    def init_text(self):
        if not self.text_font:
            self.text_font = font.SysFont('ComicSans', self.text_size)
            
        
    def update(self):
        self.text_surface = self.text_font.render(self.text, True, self.text_color)
        
        self.image.blit(self.text_surface, self.text_surface.get_rect(center = (self.image.get_width()/2, self.image.get_height()/2)))
        
        if self.border_width > 0:
            rect = self.image.get_rect(right = self.image.get_width(), bottom = self.image.get_height())
            draw.rect(self.image, self.border_color, rect, self.border_width)
        
        