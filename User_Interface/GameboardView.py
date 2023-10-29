# GameboardView
# In charge of rendering the game board, properties, and other visual 
# elements related to the game board. Handles user interactions with the game board, such as property selections and purchases. 
import pygame
WIDTH, HEIGHT = 1280, 720
from Game_Engine.GameboardManager import Gameboard


def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")
    return tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))


class GameboardView():
    def __init__(self,win,):
        self.WIN = win
        self.gameboard = Gameboard()
        self.property_size = 40
        self.properties = self.gameboard.properties

    def setup_board(self):
        for row in range(8):  
            for col in range(8):  
                x = col * self.property_size
                y = row * self.property_size

                if row == 0 or row == 7 or col == 0 or col == 7:
                    # Draw properties on the sides
                    property_index = (row * 10 + col) % len(self.properties)
                    pygame.draw.rect(self.WIN, hex_to_rgb(self.properties[property_index].color), (x, y, self.property_size, self.property_size))
                else:
                    # Leave the middle empty
                    pygame.draw.rect(self.WIN, (255, 255, 255), (x, y, self.property_size, self.property_size)) 
        pygame.display.update()
        


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