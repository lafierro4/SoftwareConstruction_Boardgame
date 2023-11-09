# GameboardView
# In charge of rendering the game board, properties, and other visual
# elements related to the game board. Handles user interactions with the game board, such as property selections and purchases.
import pygame, os, random

WIDTH, HEIGHT = 1280, 720
from Game_Engine.GameboardManager import Gameboard, Player
from User_Interface.Button import Button, ImageButton


def hex_to_rgb(hex_code) -> tuple[int, int, int]:
    hex_code = hex_code.lstrip("#")
    return tuple(int(hex_code[i : i + 2], 16) for i in (0, 2, 4))


class GameboardView:
    def __init__(self):
        self.gameboard = Gameboard()
        self.property_size = 50
        self.squares = self.gameboard._board
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        self.border_width = 2

    def setup_board(self,screen:pygame.Surface):
        self.board_surface.fill((255, 255, 255))
        for row in range(1, 14):
            for col in range(1, 14):
                x = (col - 1) * self.property_size
                y = (row - 1) * self.property_size
                if row == 1:
                    self.draw_row(col, x, y)
                if row == 12:
                    self.draw_row(col, x, y)
                if row == 2 or row == 13:
                    continue
                if row > 2 and row < 12:
                    if col == 1 or col == 12:
                        self.draw_rectangle(x, y, False, True)
                
        screen.blit(self.board_surface, (0, 0))
    
    def draw_row(self, col, x, y):
        if col == 1:
            self.draw_rectangle(x, y, True, False)
        elif col == 2 or col == 13:
            return
        elif col == 12:
            self.draw_rectangle(x, y, True, False)
        else:
            self.draw_rectangle(x, y, False, False)

    def draw_rectangle(self, x, y, is_corner, is_lateral):
        if is_corner:
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#cce6cf"),
                (x, y, self.property_size * 2, self.property_size * 2),
            )
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#171717"),
                (x, y, self.property_size * 2, self.property_size * 2),
                width=self.border_width,
            )
        elif is_lateral:
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#cce6cf"),
                (x, y, self.property_size * 2, self.property_size),
            )
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#171717"),
                (x, y, self.property_size * 2, self.property_size),
                width=self.border_width,
            )
        else:
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#cce6cf"),
                (x, y, self.property_size, self.property_size * 2),
            )
            pygame.draw.rect(
                        self.board_surface,
                        hex_to_rgb("#171717"),
                        (x, y, self.property_size, self.property_size * 2), width = self.border_width
                    )
            
    def render_player_move(self, screen: pygame.Surface, player: Player, distance:int):
        for step in range(distance):
            # erase board  
            screen.blit(self.board_surface, (0, 0))  
            # gets player rectangle
            token_rect = player.token.get_rect() 
            # conditions for movement direction
            if player._position_y == self.property_size * 11:
                if player._position_x == self.property_size: 
                    token_rect.move_ip(player._position_x,player._position_y - self.property_size)
                else:
                    token_rect.move_ip(player._position_x - self.property_size, player._position_y) 
            elif player._position_y == self.property_size:
                if player._position_x == self.property_size * 11:
                    token_rect.move_ip(player._position_x,player._position_y + self.property_size)
                else:
                    token_rect.move_ip(player._position_x + self.property_size,player._position_y)
            else:
                if player._position_x == self.property_size:
                    token_rect.move_ip(player._position_x, player._position_y - self.property_size)
                else:
                    token_rect.move_ip(player._position_x,player._position_y + self.property_size)
            # Update player's position
            player._position_x = token_rect.x
            player._position_y = token_rect.y
            # Redraw player
            screen.blit(player.token, token_rect)
            # Introduce a delay to control the animation speed (adjust the milliseconds as needed)
            #pygame.time.delay(100)  # 500 milliseconds (0.5 seconds) 

    def main_loop_screen(self, SCREEN: pygame.Surface, FPS, number_players: int):
        player_one = initialize_player(SCREEN, "michel", os.path.join("assets", "images", "car.png"), self)

        dice_img = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "dice.png")),(50,50))
        dice_button = ImageButton(((SCREEN.get_width() / 1.75), (SCREEN.get_height() / 1.25)), dice_img)
        display_action(SCREEN, player_one, None)

        dice_surfaces = list(map(lambda index: pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", f"dice_{index}.png")), (50, 50)), range(1,7)))

        run = True
        clock = pygame.time.Clock()
        while run:
            mouse_pos = pygame.mouse.get_pos()

            dice_button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Moves player with each click the amount of spaces indicated
                    if event.button == 1 and dice_button.checkForInput(mouse_pos):
                        dice_rolls = self.gameboard.roll_dice()
                        player_position = player_one.move(sum(dice_rolls))
                        
                        self.render_player_move(SCREEN,player_one,dice_rolls[0] + dice_rolls[1])
                        for index, roll in enumerate(dice_rolls):
                            SCREEN.blit(dice_surfaces[roll - 1], (SCREEN.get_width() / (1.65 - index * 0.12), SCREEN.get_height() / 1.30))
                        display_action(SCREEN, player_one, player_position)
                      
            pygame.display.update()
            clock.tick(FPS)
        
        return 0



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

def display_action(screen: pygame.Surface, player, square_index):
    button_font = pygame.font.SysFont("Minecraft", 25)
    yes_button  = Button((150,400),"YES", button_font, "black", "#0f0")
    yes_button.update(screen)

# Update Game Board
# Renders the current game state in real time by communicating with the Game Board Manager.
# Pre-Condition: \@requires self.is_valid_game_state == True
# Post-Condition: \@ensures self.update_board()
# Method Signature: def update_game_board(self, board: GameboardManager, player_action)

# Render Player Position
# Renders Player’s position and movement whenever a change in game state occurs.
# Pre-Condition: \@requires player is not None and player.position >= 0 and player.position <= 40
# Post-Condition: \@ensures self.player_rendered()
# Method Signature: def render_player_position(self, player: Player) -> None:

# Render Dice Roll
# Render the Dice Roll Animation when the Player rolls any dice.
# Pre-Condition: \@requires roll >= 1 and roll <= 6
# Post-Condition: \@ensures self.dice_rendered()
# Method Signature: def render_dice_roll(self, roll: int) -> None:
