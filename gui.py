import pygame, pygame_menu
import pygame_menu.locals
import pygame_menu.widgets

pygame.init()
display = pygame.display.set_mode((720,720))

menu = pygame_menu.Menu('Hello World', 720,720)
food_menu = pygame_menu.Menu('Foods', 720, 720)

def func(name):
    print('Hello world from', name)  # Name will be 'foo'

menu.add.button('Exec', func, 'foo',                   # Execute a function
                align=pygame_menu.locals.ALIGN_CENTER)

menu.add.button(title = 'food list', action = food_menu)

menu.add.button('Exit', pygame_menu.events.EXIT,       # Link to exit action
                align=pygame_menu.locals.ALIGN_RIGHT)



scroll_bar = pygame_menu.widgets.ScrollBar(400, (1,2), orientation= pygame_menu.locals.ORIENTATION_VERTICAL)



while True:


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(display)
        
    
        
    scroll_bar.update(events)
    scroll_bar.draw(display)

    pygame.display.update()