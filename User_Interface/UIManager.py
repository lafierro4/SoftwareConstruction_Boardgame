# UIManager
# Responsible for managing and coordination the game’s user interface. Interacts with other UI components for rendering and displaying the game information. 
# This is where we will have all the pygame components, along with the other UI classes

# TO DO: Agree on short cut names for imports
import pygame
from User_Interface.GameboardView import GameboardView
from Game_Engine.Player import Player
import User_Interface.MenuView as mv

pygame.init()
# Constants
# FPS = the refresh rate of the in frames per second
# SCREEN = the surface layer of the pygame window, the main layer
FPS = 60
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
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
    menu_choice = mv.menu(SCREEN,FPS)
    return menu_choice

# TO DO Move Functionality below to GameboardView
def initialize_player(SCREEN, pos_x, name, image):
    # create a surface object, image is drawn on it.
    token = pygame.image.load(image).convert_alpha()
    # Scale the image
    token = pygame.transform.scale(token, (40,40))
    # Draw initial position of player on board
    SCREEN.blit(token, (pos_x, 0))
    player_one = Player(name, token)
    return player_one

def initialize_gameboard():
    # Initialize the board
    pos_x = 0
    player_one = initialize_player(SCREEN,pos_x,"michel","assets/images/car.png")
    run = True
    clock = pygame.time.Clock()
    SCREEN.fill("black")
    gameboard_view = GameboardView(SCREEN)
    board_setup = gameboard_view.setup_board()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Moves player with each click
                if event.button == 1: 
                    pos_x = player_one.move_player(SCREEN,gameboard_view, pos_x)

        pygame.display.update()
        clock.tick(FPS)
    return 0

main_loop()