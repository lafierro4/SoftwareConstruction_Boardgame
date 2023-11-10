# MenuView
# Manages the various menu and options within the game, including the main menu, settings, and in-game menu.
# It allows players to navigate and make selections within the game. 

import pygame, os
from User_Interface.Button import *
pygame.init()

# Display Choice 
# Informs the GameBoardView about the user’s display setting such as size, brightness, or color blindness. 
# Pre-Conditions: \@requires self.is_initialized() 
# Post-Condition: \@ensures self.ui.display_updated_settings() 
# Method Signature: def display_choice(self) -> None: 

FPS = 60

def main_menu(SCREEN: pygame.Surface) -> int:
    """
        The Main Menu Screen.
        Gives the User Options at the start up of game.\n
        Returns Code based on user's choice
    """
    # Sets the Background Image and Sound, Sound loops until Screen transision.
    SCREEN.fill("white")
    bg_image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "title_bg.png")), (SCREEN.get_width(), SCREEN.get_height()))
    #bg_image.set_alpha(128)
    
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join("assets","sounds","title_bg_music.mp3"))
    pygame.mixer.music.set_volume(0.45)
    pygame.mixer.music.play(loops= -1)

    title_font = pygame.font.SysFont("consolas", 75)
    button_font =  pygame.font.SysFont("consolas", 50)

    # Screen Game Loop, Renders Buttons and Checks if the user clicks them
    run = True
    clock = pygame.time.Clock()
    while run:
        bg_image = pygame.transform.smoothscale(bg_image, (SCREEN.get_width(), SCREEN.get_height()))
        SCREEN.blit(bg_image,(0,0))
        mouse_pos = pygame.mouse.get_pos()
        menu_text = title_font.render("Cloneopoly", True, "black")
        menu_text_rect = menu_text.get_rect(center = (SCREEN.get_width()/2, SCREEN.get_height()/5))
      
        play_button = Button(pos=(SCREEN.get_width()/2, SCREEN.get_height()/3), text_input= "Play", font= button_font , base_color="#39FF14", hover_color= "#0a18f3")
        options_button = Button(pos=(SCREEN.get_width()/2, SCREEN.get_height()/3 + 100), text_input= "Options", font= button_font, base_color= "#39FF14", hover_color= "#0a18f3")
        quit_button = Button(pos=(SCREEN.get_width()/2, SCREEN.get_height()/3 + 200), text_input= "Quit", font= button_font, base_color= "#39FF14", hover_color= "#0a18f3")
        
        SCREEN.blit(menu_text,menu_text_rect)
      
        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    pygame.mixer.music.stop()
                    return 1
                if options_button.checkForInput(mouse_pos):
                    options_menu(SCREEN)
                if quit_button.checkForInput(mouse_pos):
                    run = False
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

def options_menu(SCREEN: pygame.Surface):

    SCREEN.fill("white")
    default_size = (1280, 720)
    window_size_list = [(1280,720),(1920,1080)]
    current_size_index = 0
    for index, size in enumerate(window_size_list):
        if pygame.display.get_window_size() == size:
            current_size_index = index
    bg_image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets","images","bg_settings.png")), (SCREEN.get_width(), SCREEN.get_height()) )
    bg_image.set_alpha(128)
    

    next_arrow_image = pygame.image.load(os.path.join("assets", "images", "next_arrow.png"))
    previous_arrow_image = pygame.image.load(os.path.join("assets","images","previous_arrow.png"))
    return_arrow_image = pygame.transform.scale(pygame.image.load(os.path.join("assets","images","return.png")), (50,50))
    text_font = pygame.font.SysFont("consolas", 50)

    run = True
    clock = pygame.time.Clock()

    while run:
        if (bg_image.get_width(), bg_image.get_height()) != (SCREEN.get_width(), SCREEN.get_height()):
            bg_image = pygame.transform.smoothscale(bg_image, (SCREEN.get_width(), SCREEN.get_height()))
        SCREEN.blit(bg_image,(0,0))
        
        mouse_pos = pygame.mouse.get_pos()
        menu_text = text_font.render(str(window_size_list[current_size_index]), True, "#39FF14")
        menu_text_rect = menu_text.get_rect(center = (SCREEN.get_width()/2, SCREEN.get_height()/4))
        SCREEN.blit(menu_text,menu_text_rect)

        previous_button = ImageButton(pos=((SCREEN.get_width()/4), (SCREEN.get_height()/4)), image= previous_arrow_image)
        next_button = ImageButton(pos=(((SCREEN.get_width()/4)*3),(SCREEN.get_height()/4)), image= next_arrow_image)
        return_button = ImageButton(pos=(50,50) , image=return_arrow_image)
        
        for button in [previous_button, next_button, return_button]:
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if previous_button.checkForInput(mouse_pos):
                    current_size_index -= 1
                    if current_size_index < 0:
                        current_size_index = len(window_size_list) - 1
                    new_width, new_height = window_size_list[current_size_index]
                    pygame.display.set_mode((new_width, new_height))
                    pygame.display.get_surface().blit(SCREEN, (0, 0))
                if next_button.checkForInput(mouse_pos):
                    current_size_index += 1
                    if current_size_index >= len(window_size_list):
                        current_size_index = 0
                    new_width, new_height = window_size_list[current_size_index]
                    pygame.display.set_mode((new_width, new_height))
                    pygame.display.get_surface().blit(SCREEN, (0, 0))
                if return_button.checkForInput(mouse_pos):
                    return

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()