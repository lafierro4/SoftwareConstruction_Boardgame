# UIManager
# Responsible for managing and coordination the game’s user interface. Interacts with other UI components for rendering and displaying the game information.
# This is where we will have all the pygame components, along with the other UI classes

# TO DO: Agree on short cut names for imports
import pygame
from Game_Engine.Player import Player
from User_Interface import MenuView, GameboardView, PlayerInfoView, util

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


def start_game(number_players):
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
            player_info = PlayerInfoView.player_select_screen(SCREEN, number_players)
            initialize_gameboard(player_info)
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
    menu_choice = MenuView.main_menu(SCREEN)
    return menu_choice



def initialize_players(player_info) -> list[Player]:
    players = []
    player_names, player_tokens = player_info
    space_size = SCREEN.get_width() / 25.6
    tokens = util.token_image_surface(space_size/1.4)

    for name, token in zip(player_names,player_tokens):
        player = Player(name,tokens[token],space_size)
        player.set_position(space_size * 11, space_size * 11)
        players.append(player)
        SCREEN.blit(tokens[token], (player._position_x, player._position_y))

    pygame.display.flip()
    return players


def initialize_gameboard(player_info):
    # Initialize the board
    SCREEN.fill("white")
    gameboard_view = GameboardView.GameboardView(SCREEN)
    gameboard_view.setup_board()
    pygame.display.update()
    players = initialize_players(player_info)
    gameboard_view.main_loop_screen(players)
    

