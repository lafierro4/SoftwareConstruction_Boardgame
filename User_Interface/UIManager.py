# UIManager
# Responsible for managing and coordination the game’s user interface. Interacts with other UI components for rendering and displaying the game information. 
# This is where we will have all the pygame components, along with the other UI classes
import pygame
from  User_Interface.GameboardView import GameboardView
WIDTH, HEIGHT = 1280, 720
from Game_Engine.Player import Player

pygame.init()
FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
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

def initialize_player(WIN, pos_x, name, image):
    # create a surface object, image is drawn on it.
    token = pygame.image.load(image).convert_alpha()
    # Scale the image
    token = pygame.transform.scale(token, (40,40))
    # Draw initial position of player on board
    WIN.blit(token, (pos_x, 0))
    player_one = Player(name, token)
    return player_one

def run():
    """
        The Main Game Loop
    """
    run = True
    clock = pygame.time.Clock()
    gameboard_view = GameboardView(WIN)
    gameboard_view.setup_board()
    
    pos_x = 0
    player_one = initialize_player(WIN,pos_x,"michel","assets/car.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # Moves player with each click
                if event.button == 1: 
                    pos_x = player_one.move_player(WIN,gameboard_view, pos_x)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

run()