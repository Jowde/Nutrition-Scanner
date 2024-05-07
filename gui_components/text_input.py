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
        
        self.current_index = self.min_index
    
    @property
    def current_index(self):
        return self._current_index
    @current_index.setter
    def current_index(self, value):
        if value >= self.min_index and value <= len(self.text):
            self._current_index = value
        
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
                elif event.key == pygame.K_BACKSPACE:
                    if len(self.text) > 0 and self.current_index - 1 >= 0:
                            self.text = self.text[:self.current_index - 1] + self.text[self.current_index:]
                            self.current_index -=1
                elif event.key == pygame.K_RIGHT:
                    self.current_index +=1
                elif event.key == pygame.K_LEFT:
                    self.current_index -=1
                print(self.current_index)
                
                   
            
            
            
