# UIManager
# Responsible for managing and coordination the game’s user interface. Interacts with other UI components for rendering and displaying the game information.
# This is where we will have all the pygame components, along with the other UI classes

# TO DO: Agree on short cut names for imports
import pygame, os,random
from Game_Engine.GameboardManager import Gameboard
import User_Interface.GameboardView as gv
from Game_Engine.Player import Player
import User_Interface.MenuView as mv
from User_Interface.Button import *

pygame.init()
# Constants
# FPS = the refresh rate of the in frames per second
# SCREEN = the surface layer of the pygame window, the main layer
FPS = 60
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cloneopoly")


# Initial Board Rendering
# Collaborates with the GameBoardView to render the Initial Board State.
# Pre-Condition: \@requires self.ui.board.is_rendered == False
# Post-Condition: \@ensures self.ui.board.is_rendered == True
# Method Signature: def render_initial_board(self) -> None:

# Player Info Display
# Informs PlayerView how to display the Player’s status and information.
# Pre-Condition: \@requires self.is_valid_status(player_status) == True
# Post-Condition: \@ensures self.ui.display_status()
# Method Signature: def display_player_status(self) -> None:

# Menu Management
# Helps layer the Menu assets to display the correct formatting
# Pre-Condition: \@requires self.is_layered_menu() == True
# Post-Condition: \@ensures self.ui.display_menu()
# Method Signature: def form_menu(self) -> None:


def main_loop():
    """
    The Main Game Loop, Checks for Inputs and Transitions to other Screens/Game Loops
    """
    run = True
    clock = pygame.time.Clock()
    return_status = title_menu()
    while run:
        if return_status == 0 or return_status == 3:
            run = False
        if return_status == 1:
            return_status = initialize_gameboard()
        if return_status == 2:
            pass
        # We might need this event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


def title_menu():
    """
    Starts the Main Menu Screen from MenuView \n
    Returns a status code with the user's choice
    """
    menu_choice = mv.main_menu(SCREEN, FPS)
    return menu_choice


# TO DO Move Functionality below to GameboardView
def initialize_player(SCREEN, name, image, gameboard_view):
    # create a surface object, image is drawn on it.
    token = pygame.image.load(image).convert_alpha()
    # Scale the image
    token = pygame.transform.scale(token, (40, 40))
    
    player_one = Player(name, token, gameboard_view.property_size)
    # Draw initial position of player on board
    SCREEN.blit(token, (player_one._position_x, player_one._position_y))
    return player_one


def initialize_gameboard():
    # Initialize the board
    run = True
    clock = pygame.time.Clock()
    SCREEN.fill("black")
    gameboard_view = gv.GameboardView(SCREEN)
    player_one = initialize_player(SCREEN, "michel", os.path.join("assets", "images", "car.png"), gameboard_view)
    board_setup = gameboard_view.setup_board()
    gameboard = Gameboard()
    gameboard.add_player(Player("James", os.path.join("assets", "images", "car.png"), gameboard_view.property_size))
    gameboard.add_player(Player("Gello", os.path.join("assets", "images", "car.png"), gameboard_view.property_size))
    pygame.display.update()
    # gameboard.play_game()
    dice_img = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "dice.png")),(50,50))
    
    dice_button = ImageButton(((SCREEN.get_width()/1.75), (SCREEN.get_height()/1.25)), dice_img)


    while run:
        mouse_pos = pygame.mouse.get_pos()
        dice_button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Moves player with each click the amount of spaces indicated
                if dice_button.checkForInput(mouse_pos):
                    dice_1 = random.randint(1, 6)
                    dice_2 = random.randint(1, 6)
                    result = dice_1 + dice_2
                    result_faces = gv.display_result([dice_1,dice_2])
                    print(f"{dice_1} + {dice_2} = {result}")
                    gameboard_view.render_player_move(SCREEN,player_one,result)
                    SCREEN.blit(result_faces[0],((SCREEN.get_width()/1.65), (SCREEN.get_height()/1.30)))
                    SCREEN.blit(result_faces[1],((SCREEN.get_width()/1.53), (SCREEN.get_height()/1.30)))
                    
                    
        pygame.display.update()
        clock.tick(FPS)
    return 0


main_loop()
