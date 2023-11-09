# GameboardView
# In charge of rendering the game board, properties, and other visual
# elements related to the game board. Handles user interactions with the game board, such as property selections and purchases.
import pygame, os, random

FPS = 60
WIDTH, HEIGHT = 1280, 720
from Game_Engine.GameboardManager import Gameboard, Player, Property
from User_Interface.Button import Button, ImageButton


def hex_to_rgb(hex_code) -> tuple[int, int, int]:
    hex_code = hex_code.lstrip("#")
    r, g, b = int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16)
    return r, g, b


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

    def main_loop_screen(self, SCREEN: pygame.Surface, number_players: int):
        player_one = initialize_player(SCREEN, "michel", os.path.join("assets", "images", "car.png"), self)
        dice_img = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "dice.png")),(50,50))
        dice_button = ImageButton(((SCREEN.get_width() / 1.75), (SCREEN.get_height() / 1.25)), dice_img)

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
                        self.display_action(SCREEN, player_one, player_position)
                      
            pygame.display.update()
            clock.tick(FPS)
        
        return 0


    def display_action(self, screen: pygame.Surface, player:Player, square_index):
        font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 30)
        current_square = self.gameboard._board[square_index]
        run = True
        clock = pygame.time.Clock()
        quit_pygame = False
        #  modify to display the square text,
        # action = font.render(str(current_square), True, (0,0,0))
        # screen.blit(action,(165,250)
        print(str(current_square))
        if isinstance(current_square,Property):
            while run:
                if not current_square.is_owned():
                    action = (f"Would you like to buy {current_square.name} for ${current_square.price}?")
                    action_text = font.render(action, True,hex_to_rgb("#000000"))
                    action_text_rect = action_text.get_rect(center = (screen.get_width()/1.35, screen.get_height()/2))
                    screen.blit(action_text,action_text_rect)
                    yes_button  = Button((screen.get_width()/1.3-150,screen.get_height()/1.5),"YES", font, "#000000", "#00ff00")
                    no_button = Button((screen.get_width()/1.3,screen.get_height()/1.5), "NO", font, "#000000", "#ff0000")
                    mouse_pos = pygame.mouse.get_pos()

                    for button in [yes_button, no_button]:
                        button.changeColor(mouse_pos)
                        button.update(screen)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if yes_button.checkForInput(mouse_pos):
                                if player.balance >= current_square.price:
                                    print(f"{current_square.owner_name}, {player.balance}, {player._assets}")
                                    current_square.action(player)
                                    player.add_property(current_square)
                                    print(f"{current_square.owner_name}, {player.balance}, {player._assets}")
                                    return
                                else:
                                    print("no money")
                            if no_button.checkForInput(mouse_pos):
                                print("no")
                                return
                elif current_square.owner is not player:
                    action = (f"Player {current_square.owner_name} owns {current_square.name}, pay ${current_square._rent_values}")
                    action_text = font.render(action, True,hex_to_rgb("#000000"))
                    action_text_rect = action_text.get_rect(center = (screen.get_width()/1.35, screen.get_height()/2))
                    screen.blit(action_text,action_text_rect)
                else:
                    action = (f"You own {current_square.name}")
                    action_text = font.render(action, True,hex_to_rgb("#000000"))
                    action_text_rect = action_text.get_rect(center = (screen.get_width()/1.35, screen.get_height()/2))
                    screen.blit(action_text,action_text_rect)
                pygame.display.update()
                clock.tick(FPS)

        if quit_pygame == True:
            pygame.quit()
            quit()
        return



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


def render_wrapped_text(text, font, max_width):
    words = text.split(' ')
    wrapped_lines = []
    current_line = words[0]

    for word in words[1:]:
        test_line = current_line + ' ' + word
        test_width, _ = font.size(test_line)
            
        if test_width <= max_width:
                current_line = test_line
        else:
            wrapped_lines.append(current_line)
            current_line = word

    wrapped_lines.append(current_line)
    return wrapped_lines   

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
