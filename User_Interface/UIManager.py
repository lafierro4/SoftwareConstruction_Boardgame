# UIManager
# Responsible for managing and coordination the game’s user interface. Interacts with other UI components for rendering and displaying the game information.
# This is where we will have all the pygame components, along with the other UI classes

# TO DO: Agree on short cut names for imports
import pygame
from Game_Engine.Player import Player
from User_Interface import MenuView, GameboardView, PlayerInfoView, util

# Initialze Pygame Window and sets the default window size to be 1280 by 720
pygame.init()
FPS = 60
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Cloneopoly")

#This whole class is a middleman, its not even a class really, 

def start_game(number_players):
    """
    The Initial Game Loop,
    """
    run = True
    clock = pygame.time.Clock()
    menu_results = title_menu()
    is_ai = False
    number_of_humans = menu_results[0] # type: ignore
    number_of_bots = menu_results[1] # type: ignore
    number_players = number_of_humans + number_of_bots
    if number_of_bots > 0:
        is_ai = True
    while run:
        player_info = PlayerInfoView.player_select_screen(SCREEN, number_players, is_ai) # type: ignore
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
