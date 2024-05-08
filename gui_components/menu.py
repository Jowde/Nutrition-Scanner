from pygame import Vector2, Surface, transform, Color
from pygame.sprite import Sprite, Group
from gui_components.label import Label
from gui_components.button import Button
from gui_components.text_input import TextInput
class Menu(Sprite):
    def __init__(self, display: Surface, relative_size: tuple[float,float] = (1,1), position: str = 'center', 
                 bg_color: Color = Color(255,255,255), bg_image: Surface = None, layout: str = 'horizontal'):
        self.display = display
        self.relative_size = Vector2(relative_size)
        self.position = position.lower()
        self.bg_color = bg_color
        self.bg_image = bg_image
        self.layout = layout.lower()
        self.widget_group = Group()
        
        self.size = Vector2(
                            self.relative_size.x*self.display.get_width(), 
                            self.relative_size.y*self.display.get_height()
                            )
        self.init_bg()
    
    def init_bg(self):
        calculated_size = (self.display.get_width()*self.relative_size.x, self.display.get_height()*self.relative_size.y)
        if self.bg_image:
            self.image = transform.scale(self.bg_image, calculated_size)
        else:
            self.image = Surface(calculated_size)
            self.image.fill(self.bg_color)
        
        self.rect = self.image.get_rect()
        
        self.init_position()
        
    def init_position(self):
        
        if self.position == 'topleft':
            self.rect.top = 0
            self.rect.left = 0
            
        elif self.position == 'topcenter':
            self.rect.top = 0
            self.rect.centerx = self.display.get_width()//2
        
        elif self.position == 'topright':
            self.rect.right = self.display.get_width()
            self.rect.top = 0
        
        elif self.position == 'centerleft':
            self.rect.left = 0
            self.rect.centery = self.display.get_height()//2
            
        elif self.position == 'center':
            self.rect.center = (self.display.get_width()//2, 
                                self.display.get_height()//2)
            
        elif self.position == 'centerright':
            self.rect.right = self.display.get_width()
            self.rect.centery = self.display.get_height()//2
            
        elif self.position == 'bottomleft':
            self.rect.left = 0
            self.rect.bottom = self.display.get_height()
        
        elif self.position == 'bottomcenter':
            self.rect.centerx = self.display.get_width()//2
            self.rect.bottom = self.display.get_height()
            
        elif self.position == 'bottomright':
            self.rect.right = self.display.get_width()
            self.rect.bottom = self.display.get_height()
        else:
            print(f'invalid position for {self}')
    
    def add_widget(self, widget):
        self.widget_group.add(widget)
    
    def init_widgets(self):
        for index, widget in enumerate(self.widget_group):
            if isinstance(widget, Menu):
                widget.init_widgets()
            else:
                widget.init_image(index, len(self.widget_group), self.layout)
            
    def clear(self):
        self.image.fill(self.bg_color)
        
    def draw(self, pos: tuple[int, int], click: bool, pressed_keys: list):
        for widget in self.widget_group:
            if isinstance(widget, TextInput):
                if widget.is_hovered_over(pos) and click:
                    widget.selected = True
                    
                elif not widget.is_hovered_over(pos) and click:
                    widget.selected = False
    
                if widget.selected:
                    widget.highlight()
                widget.input_handler(pressed_keys)
                
            if widget.is_hovered_over(pos) and click:
                widget.pressed()
                click = False
                
            widget.update()
            self.image.blit(widget.image, widget.position)
        self.display.blit(source = self.image, dest=self.rect)
        
    
    def blit(self, source, dest):
        self.image.blit(source=source, dest=dest)
        
    def get_width(self):
        return self.size.x
    
    def get_height(self):
        return self.size.y