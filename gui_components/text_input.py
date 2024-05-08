from pygame import Surface, Color
from gui_components.button import Button
from pygame.font import Font
import pygame 

class TextInput(Button):
    def __init__(self, menu: Surface, image: Surface = None, relative_size: tuple[float, float] = None, bg_color: Color = Color(255,255,255), relative_padding: tuple[int, int] = (0,0), 
                 text: str = '', text_font: Font = None, text_size: int = 32, text_color: Color = Color(0,0,0), 
                 hover_highlight: float = 1.125, border_width: int = 0, border_color: Color = Color(0,0,0), min_index: int =0, max_index:int = 0):

        func = lambda: True
        super().__init__(menu=menu, image = image, relative_size=relative_size, bg_color=bg_color, relative_padding=relative_padding, 
                         text=text, text_font=text_font, text_size=text_size, text_color= text_color, hover_highlight=hover_highlight, 
                         on_press = func, border_width=border_width, border_color=border_color)
        
        self.selected = False
        self.min_index = min_index
        self.max_index = max_index
        
        self.max_counter = 120
        self.counter = self.max_counter
        
        self.display_line_colors = [pygame.Color(0,0,0), pygame.Color(125,125,125)]
        self.display_line_index = 0
        self.current_index = self.min_index
    
    @property
    def current_index(self):
        return self._current_index
    
    @current_index.setter
    def current_index(self, value):
        if value >= self.min_index and value <= len(self.text):
            self._current_index = value
            
    @property
    def display_line_index(self):
        return self._display_line_index
    
    @display_line_index.setter
    def display_line_index(self, value):
        if value >= len(self.display_line_colors):
            self._display_line_index = 0
        else:
            self._display_line_index = value
        
    def change_selected_to_true(self):
        self.selected = True
        
    def change_selected_to_false(self):
        self.selected = False
    
    def input_handler(self, key_presseds: list):
        if self.selected:
            for event in key_presseds:
                if event.key == pygame.K_0:
                    self.text = self.text[:self.current_index] + '0'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_1:
                    self.text = self.text[:self.current_index] + '1'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_2:
                    self.text = self.text[:self.current_index] + '2'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_3:
                    self.text = self.text[:self.current_index] + '3'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_4:
                    self.text = self.text[:self.current_index] + '4'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_5:
                    self.text = self.text[:self.current_index] + '5'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_6:
                    self.text = self.text[:self.current_index] + '6'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_7:
                    self.text = self.text[:self.current_index] + '7'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_8:
                    self.text = self.text[:self.current_index] + '8'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_9:
                    self.text = self.text[:self.current_index] + '9'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_q:
                    self.text = self.text[:self.current_index] + 'q'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_w:
                    self.text = self.text[:self.current_index] + 'w'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_e:
                    self.text = self.text[:self.current_index] + 'e'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_r:
                    self.text = self.text[:self.current_index] + 'r'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_t:
                    self.text = self.text[:self.current_index] + 't'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_y:
                    self.text = self.text[:self.current_index] + 'y'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_u:
                    self.text = self.text[:self.current_index] + 'u'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_i:
                    self.text = self.text[:self.current_index] + 'i'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_o:
                    self.text = self.text[:self.current_index] + 'o'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_p:
                    self.text = self.text[:self.current_index] + 'p'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_a:
                    self.text = self.text[:self.current_index] + 'a'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_s:
                    self.text = self.text[:self.current_index] + 's'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_d:
                    self.text = self.text[:self.current_index] + 'd'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_f:
                    self.text = self.text[:self.current_index] + 'f'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_g:
                    self.text = self.text[:self.current_index] + 'g'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_h:
                    self.text = self.text[:self.current_index] + 'h'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_j:
                    self.text = self.text[:self.current_index] + 'j'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_k:
                    self.text = self.text[:self.current_index] + 'k'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_l:
                    self.text = self.text[:self.current_index] + 'l'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_z:
                    self.text = self.text[:self.current_index] + 'z'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_x:
                    self.text = self.text[:self.current_index] + 'x'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_c:
                    self.text = self.text[:self.current_index] + 'c'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_v:
                    self.text = self.text[:self.current_index] + 'v'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_b:
                    self.text = self.text[:self.current_index] + 'b'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_n:
                    self.text = self.text[:self.current_index] + 'n'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_m:
                    self.text = self.text[:self.current_index] + 'm'+  self.text[self.current_index:]
                    self.current_index +=1
                elif event.key == pygame.K_BACKSPACE:
                    if len(self.text) > 0 and self.current_index - 1 >= 0:
                            self.text = self.text[:self.current_index - 1] + self.text[self.current_index:]
                            self.current_index -=1
                elif event.key == pygame.K_RIGHT:
                    self.current_index +=1
                elif event.key == pygame.K_LEFT:
                    self.current_index -=1

    def update(self):
        if self.counter > 0:
            self.counter-=1
        else:
            self.counter = self.max_counter
            self.display_line_index +=1
        self.text_surface = self.text_font.render(self.text, True, self.text_color)
        rect = self.text_surface.get_rect(center = (self.image.get_width()/2, self.image.get_height()/2))
        self.image.blit(self.text_surface, rect)
        
        if self.selected:
            try:
                pygame.draw.line(self.image, 
                                self.display_line_colors[self.display_line_index], 
                                (self.current_index/(len(self.text)) * self.text_surface.get_width() + (rect.left), rect.top),
                                (self.current_index/(len(self.text)) * self.text_surface.get_width() + (rect.left), rect.bottom), 
                                width=1)
            except:
                    pygame.draw.line(self.image, 
                                self.display_line_colors[self.display_line_index], 
                                (0 * self.text_surface.get_width() + (rect.left), rect.top),
                                (0 * self.text_surface.get_width() + (rect.left), rect.bottom), 
                                width=1)
            
        if self.border_width > 0:
            rect = self.image.get_rect(right = self.image.get_width(), bottom = self.image.get_height())
            pygame.draw.rect(self.image, self.border_color, rect, self.border_width)
            
        
                
                   
            
            
            
