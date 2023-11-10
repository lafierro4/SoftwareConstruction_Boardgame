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


def start_game():
    """
    The Initial Game Loop,
    """
    run = True
    clock = pygame.time.Clock()
    return_status = title_menu()
    while run:
        if return_status == 0 or return_status == 3:
            run = False
        if return_status == 1:
            return_status = initialize_gameboard()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


def title_menu():
    """
    Starts the Main Menu Screen from MenuView \n
    Returns a status code with the user's choice
    """
    menu_choice = mv.main_menu(SCREEN)
    return menu_choice




def initialize_gameboard():
    # Initialize the board
    SCREEN.fill("white")
    gameboard_view = gv.GameboardView(SCREEN)
    gameboard_view.setup_board()
    pygame.display.update()
    gameboard_view.main_loop_screen(1)
    

    


start_game()
