# MenuView
# Manages the various menu and options within the game, including the main menu, settings, and in-game menu.
# It allows players to navigate and make selections within the game. 

import pygame, os
from User_Interface.util import Button, ImageButton
pygame.init()


FPS = 60

def main_menu(SCREEN: pygame.Surface) -> tuple[int,int]:
    """
        The Main Menu Screen.
        Gives the User Options at the start up of game.\n
        Returns Code based on user's choice
    """
    # Sets the Background Image and Sound, Sound loops until Screen transision.
    SCREEN.fill("white")
    bg_image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "title_bg.png")), (SCREEN.get_width(), SCREEN.get_height()))
    
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join("assets","sounds","title_bg_music.mp3"))
    pygame.mixer.music.set_volume(0.45)
    pygame.mixer.music.play(loops= -1)

    button_font =  pygame.font.SysFont("consolas", 50)

    # Screen Game Loop, Renders Buttons and Checks if the user clicks them
    run = True
    clock = pygame.time.Clock()
    while run:
        bg_image = pygame.transform.smoothscale(bg_image, (SCREEN.get_width(), SCREEN.get_height()))
        SCREEN.blit(bg_image,(0,0))
        mouse_pos = pygame.mouse.get_pos()

        play_button = Button(pos=(SCREEN.get_width()/2, SCREEN.get_height()/3), text_input= "Play", font= button_font , base_color="#000000", hover_color= "#0a18f3")
        options_button = Button(pos=(SCREEN.get_width()/2, SCREEN.get_height()/3 + 100), text_input= "Options", font= button_font, base_color= "#000000", hover_color= "#0a18f3")
        quit_button = Button(pos=(SCREEN.get_width()/2, SCREEN.get_height()/3 + 200), text_input= "Quit", font= button_font, base_color= "#000000", hover_color= "#0a18f3")
        
        for button in [play_button, options_button, quit_button]:
            button.change_color(mouse_pos)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_clicked(mouse_pos):
                    pygame.mixer.music.stop()
                    #return 1
                    return play_mode_selection(SCREEN)
                if options_button.check_clicked(mouse_pos):
                    options_menu(SCREEN)
                if quit_button.check_clicked(mouse_pos):
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
    

    previous_arrow_image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "previous_arrow.png")),(100,100))
    next_arrow_image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "next_arrow.png")),(100,100))
    return_arrow_image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets","images","return.png")), (50,50))
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
                if previous_button.check_clicked(mouse_pos):
                    current_size_index -= 1
                    if current_size_index < 0:
                        current_size_index = len(window_size_list) - 1
                    new_width, new_height = window_size_list[current_size_index]
                    pygame.display.set_mode((new_width, new_height))
                    pygame.display.get_surface().blit(SCREEN, (0, 0))
                if next_button.check_clicked(mouse_pos):
                    current_size_index += 1
                    if current_size_index >= len(window_size_list):
                        current_size_index = 0
                    new_width, new_height = window_size_list[current_size_index]
                    pygame.display.set_mode((new_width, new_height))
                    pygame.display.get_surface().blit(SCREEN, (0, 0))
                if return_button.check_clicked(mouse_pos):
                    return

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


def play_mode_selection(SCREEN: pygame.Surface) -> tuple[int,int]:
    SCREEN.fill("white")
    bg_image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "mode.png")), (SCREEN.get_width(), SCREEN.get_height()))
    pygame.mixer.music.load(os.path.join("assets","sounds","chooseAGame.mp3"))
    pygame.mixer.music.set_volume(0.45)
    pygame.mixer.music.play(loops= -1)
    button_font = pygame.font.Font(os.path.join("assets", "images", "brokenmachine.ttf"), 50)
    run = True
    clock = pygame.time.Clock()
    while run:
        bg_image = pygame.transform.smoothscale(bg_image, (SCREEN.get_width(), SCREEN.get_height()))
        SCREEN.blit(bg_image,(0,0))
        mouse_pos = pygame.mouse.get_pos()
        play_local_button = Button(pos=(SCREEN.get_width()/2, SCREEN.get_height()/3), text_input="Play Local", font=button_font, base_color="#ff0000", hover_color="#0a18f3")
        play_AI_button = Button(pos=(SCREEN.get_width() / 2, SCREEN.get_height() / 3 + 150), text_input="Play Vs AI", font=button_font, base_color="#ff0000", hover_color="#0a18f3")
        for button in [play_local_button, play_AI_button]:
            button.change_color(mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_local_button.check_clicked(mouse_pos):
                    return players_selection(SCREEN, False)
                    #return 1
                if play_AI_button.check_clicked(mouse_pos):
                    return players_selection(SCREEN, True)
                    #return 2
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

def players_selection(SCREEN: pygame.Surface, is_ai: bool) -> tuple[int,int]:
    SCREEN.fill("white")
    bg_image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "select.png")), (SCREEN.get_width(), SCREEN.get_height()))
    button_font = pygame.font.Font(os.path.join("assets", "images", "brokenmachine.ttf"), 50)
    run = True
    clock = pygame.time.Clock()
    heading_font = pygame.font.Font(os.path.join("assets", "images", "brokenmachine.ttf"), 70)
    if is_ai:
        heading_text = heading_font.render("Choose the number of bots", True, (255, 0, 0))
    else:
        heading_text = heading_font.render("Choose the number of players", True, (255, 0, 0))

    while run:
        bg_image = pygame.transform.smoothscale(bg_image, (SCREEN.get_width(), SCREEN.get_height()))
        SCREEN.blit(bg_image, (0, 0))
        SCREEN.blit(heading_text, (SCREEN.get_width() // 2 - heading_text.get_width() // 2, SCREEN.get_height() // 4))

        mouse_pos = pygame.mouse.get_pos()

        if is_ai:
            bot_1_button = Button(pos=(SCREEN.get_width() // 2, SCREEN.get_height() // 2), text_input="1 Bot", font=button_font, base_color="#ff0000", hover_color="#0a18f3")
            bot_2_button = Button(pos=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 150), text_input="2 Bots", font=button_font, base_color="#ff0000", hover_color="#0a18f3")
            bot_3_button = Button(pos=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 300), text_input="3 Bots", font=button_font, base_color="#ff0000", hover_color="#0a18f3")

            for button in [bot_1_button, bot_2_button, bot_3_button]:
                button.change_color(mouse_pos)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bot_1_button.check_clicked(mouse_pos):
                        return (1, 1) #number of human players, number of bots
                    elif bot_2_button.check_clicked(mouse_pos):
                        return (1, 2)
                    elif bot_3_button.check_clicked(mouse_pos):
                        return (1, 3)
        else:
            player_2_button = Button(pos=(SCREEN.get_width() // 2, SCREEN.get_height() // 2), text_input="2 Players", font=button_font, base_color="#ff0000", hover_color="#0a18f3")
            player_3_button = Button(pos=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 150), text_input="3 Players", font=button_font, base_color="#ff0000", hover_color="#0a18f3")
            player_4_button = Button(pos=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 300), text_input="4 Players", font=button_font, base_color="#ff0000", hover_color="#0a18f3")

            for button in [player_2_button, player_3_button, player_4_button]:
                button.change_color(mouse_pos)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_2_button.check_clicked(mouse_pos):
                        return (2, 0)
                    elif player_3_button.check_clicked(mouse_pos):
                        return (3, 0)
                    elif player_4_button.check_clicked(mouse_pos):
                        return (4, 0)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()
