from pygame import Vector2, Surface, transform, font, Color, Rect
from pygame.sprite import Sprite
from pygame.font import Font
class Label(Sprite):
    def __init__(self, menu: Surface, image: Surface = None, relative_size: tuple[float, float] = None, bg_color: Color = Color(0,0,0), relative_padding: tuple[float, float] = (0,0),
                 text: str = '', text_font: Font = None, text_size: int = 32, text_color: Color = Color(0,0,0)):
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
        
        self.rect = Rect(
                            (self.position.x + self.menu.rect.left, self.position.y + self.menu.rect.top),
                            (self.size.x, self.size.y)
                        )
        
        self.init_text()
            
    def init_text(self):
        if not self.text_font:
            self.text_font = font.SysFont('ComicSans', self.text_size)
            
        
    def update(self):
        text_surface = self.text_font.render(self.text, True, self.text_color)
        self.image.blit(text_surface, text_surface.get_rect(center = (self.image.get_width()/2, 
                                                                      self.image.get_height()/2)))
   
       
        
        
        
        