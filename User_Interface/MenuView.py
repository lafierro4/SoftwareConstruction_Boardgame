# MenuView
# Manages the various menu and options within the game, including the main menu, settings, and in-game menu.
# It allows players to navigate and make selections within the game. 

import pygame, os
from User_Interface.Button import Button
pygame.init()

# Display Choice 
# Informs the GameBoardView about the user’s display setting such as size, brightness, or color blindness. 
# Pre-Conditions: \@requires self.is_initialized() 
# Post-Condition: \@ensures self.ui.display_updated_settings() 
# Method Signature: def display_choice(self) -> None: 

title_font = pygame.font.SysFont("consolas", 75)
button_font =  pygame.font.SysFont("consolas", 50)

def main_menu(SCREEN: pygame.Surface,FPS) -> int:
    """
        The Main Menu Screen.
        Gives the User Options at the start up of game.\n
        Returns Code based on user's choice
    """
    # Sets the Background Image and Sound, Sound loops until Screen transision.
    bg_image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "title_bg.png")), (SCREEN.get_size()[0], SCREEN.get_size()[1]))
    bg_image.set_alpha(128)
    SCREEN.blit(bg_image,(0,0))
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join("assets","sounds","title_bg_music.mp3"))
    pygame.mixer.music.play(loops= -1)

    # Screen Game Loop, Renders Buttons and Checks if the user clicks them
    run = True
    clock = pygame.time.Clock()
    while run:
        mouse_pos = pygame.mouse.get_pos()
        menu_text = title_font.render("Cloneopoly", True, "black")
        menu_text_rect = menu_text.get_rect(center = (SCREEN.get_size()[0]/2, SCREEN.get_size()[1]/5))
      
        play_button = Button(image = None, pos=(SCREEN.get_size()[0]/2, SCREEN.get_size()[1]/3), text_input= "Play", font= button_font , base_color="#39FF14", hover_color= "#0a18f3")
        options_button = Button(image= None, pos=(SCREEN.get_size()[0]/2, SCREEN.get_size()[1]/3 + 100), text_input= "Options", font= button_font, base_color= "#39FF14", hover_color= "#0a18f3")
        quit_button = Button(image= None, pos=(SCREEN.get_size()[0]/2, SCREEN.get_size()[1]/3 + 200), text_input= "Quit", font= button_font, base_color= "#39FF14", hover_color= "#0a18f3")
        
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
                    return 2
                if quit_button.checkForInput(mouse_pos):
                    return 3
        pygame.display.update()
        clock.tick(FPS)
    return 0

