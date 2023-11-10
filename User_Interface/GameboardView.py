# GameboardView
# In charge of rendering the game board, properties, and other visual
# elements related to the game board. Handles user interactions with the game board, such as property selections and purchases.
import pygame, os, textwrap, math

FPS = 60
WIDTH, HEIGHT = 1280, 720
from Game_Engine.GameboardManager import Gameboard, Player, Property, Square
from User_Interface.Button import Button, ImageButton
from User_Interface.MenuView import options_menu


def hex_to_rgb(hex_code) -> tuple[int, int, int]:
    hex_code = hex_code.lstrip("#")
    r, g, b = int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16)
    return r, g, b


class GameboardView:
    def __init__(self,screen:pygame.Surface):
        self.gameboard = Gameboard()
        self.screen = screen
        self.property_size = screen.get_width() / 25.6
        self.squares = self.gameboard._board
        self.board_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.border_width = 2

    def setup_board(self):
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
                
        self.screen.blit(self.board_surface, (0, 0))
    
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
                (x, y, int(self.property_size * 2), int(self.property_size * 2)),
            )
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#171717"),
                (x, y, int(self.property_size * 2), int(self.property_size * 2)),
                width=self.border_width,
            )
        elif is_lateral:
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#cce6cf"),
                (x, y, int(self.property_size * 2), int(self.property_size)),
            )
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#171717"),
                (x, y, int(self.property_size * 2), int(self.property_size)),
                width=self.border_width,
            )
        else:
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#cce6cf"),
                (x, y, int(self.property_size), int(self.property_size * 2)),
            )
            pygame.draw.rect(
                        self.board_surface,
                        hex_to_rgb("#171717"),
                        (x, y, int(self.property_size), int(self.property_size * 2)), width = self.border_width
                    )

    def render_player_move(self,players, player: Player, distance: int):
        for step in range(distance):
            # Calculate the next position based on the step
            if player._position_y == self.property_size * 11:
                if player._position_x == self.property_size:
                    next_x, next_y = player._position_x, player._position_y - self.property_size
                else:
                    next_x, next_y = player._position_x - self.property_size, player._position_y
            elif player._position_y == self.property_size:
                if player._position_x == self.property_size * 11:
                    next_x, next_y = player._position_x, player._position_y + self.property_size
                else:
                    next_x, next_y = player._position_x + self.property_size, player._position_y
            else:
                if player._position_x == self.property_size:
                    next_x, next_y = player._position_x, player._position_y - self.property_size
                else:
                    next_x, next_y = player._position_x, player._position_y + self.property_size

            # Move the player to the next position
            player._position_x, player._position_y = next_x, next_y

            # Redraw the entire board
            self.draw_board(players)

            # Blit the player's token at the new position
            self.screen.blit(player.token, (player._position_x, player._position_y))

            # Update the display
            pygame.display.update()

            # Delay for a short period
            pygame.time.delay(250)

    def draw_board(self,players):
        # Redraw the entire board (you may need to adapt this based on your implementation)
        self.screen.blit(self.board_surface, (0, 0))
        # Add code to redraw any other elements on the board

        # Add code to redraw all player tokens at their current positions
        for player in players:
            self.screen.blit(player.token, (player._position_x, player._position_y))



    def initialize_players(self, number_players) -> list[Player]:
        players = []

        tokens = (pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "car.png")).convert_alpha(),(35,35)),
                    pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "penguin.png")).convert_alpha(),(35,35)) )

        player_one = Player("Michel", tokens[0], self.property_size,0)
        player_two = Player("Luis", tokens[1], self.property_size,1)

        # Set initial positions on the board
        player_one.set_position(self.property_size * 11, self.property_size * 11)
        player_two.set_position(self.property_size * 11, self.property_size * 11)

        players.append(player_one)
        players.append(player_two)

        # Draw initial positions of players on the board
        self.screen.blit(tokens[0], (player_one._position_x, player_one._position_y))
        self.screen.blit(tokens[1], (player_two._position_x, player_two._position_y))

        pygame.display.flip()
        return players

    def main_loop_screen(self,number_players: int):
        players = self.initialize_players(number_players)
        dice_img = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "dice.png")), (50, 50))
        dice_button = ImageButton(((self.screen.get_width() / 1.75), (self.screen.get_height() / 1.20)), dice_img)
        dice_surfaces = [pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", f"dice_{index}.png")), (50, 50)) for index in range(1, 7)]
        font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 35)
        run = True
        clock = pygame.time.Clock()
        current_player_index = 0

        while run:
            mouse_pos = pygame.mouse.get_pos()

            dice_button.update(self.screen)

            display_surface = pygame.Surface(size=(self.screen.get_width() / 2.25, self.screen.get_height() / 1.75))
            display_surface_rect = display_surface.get_rect(center=(self.screen.get_width() / 1.35, self.screen.get_height() / 2))

            turn_text = font.render(f"{players[current_player_index]._name}'s Turn, Roll Those Dice!", True, hex_to_rgb("#000000"))
            turn_text_rect = turn_text.get_rect(center=(self.screen.get_width() / 1.35, self.screen.get_height()/3.5))
            self.screen.blit(turn_text, turn_text_rect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and dice_button.checkForInput(mouse_pos):
                        self.screen.fill((255, 255, 255), display_surface_rect)
                        dice_rolls = self.gameboard.roll_dice()
                        player_position = players[current_player_index].move(sum(dice_rolls))
                        self.render_player_move(players,players[current_player_index] ,dice_rolls[0] + dice_rolls[1])
                        for index, roll in enumerate(dice_rolls):
                            self.screen.blit(dice_surfaces[roll - 1], (self.screen.get_width() / (1.65 - index * 0.12), self.screen.get_height() / 1.25))
                        self.display_action(players[current_player_index], player_position)
                        current_player_index = (current_player_index + 1) % len(players)  

            pygame.display.update()
            clock.tick(FPS)
        
        pygame.quit()
        quit()


    def display_action(self,player:Player, square_index):
        current_space = self.gameboard._board[square_index]
        if isinstance(current_space,Property):
            _display_property_action(self.screen,current_space,player)
        elif isinstance(current_space,Square):
            _display_square_action(self.screen,current_space,player)

        return
    
   


def _display_property_action(screen:pygame.Surface,property_object:Property,player:Player):
    font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 30)
    clock = pygame.time.Clock()
    run = True
    while run:
        if not property_object.is_owned():
            action = [(f"Would you like to buy"),
                       (f"{property_object.name}"),
                        (f"for ${property_object.price}?")]
            action_text = [font.render(action[0], False, hex_to_rgb("#000000")), 
                           font.render(action[1], False, hex_to_rgb("#000000")),
                           font.render(action[2], False, hex_to_rgb("#000000")),]
            action_text_rect = [action_text[0].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.75)),
                                action_text[1].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.50)),
                                action_text[2].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.25))]
            for surface,rect in zip(action_text, action_text_rect):
                screen.blit(surface,rect)
                
            yes_button  = Button((screen.get_width()/1.25-150,screen.get_height()/2),"YES", font, "#000000", "#00ff00")
            no_button = Button((screen.get_width()/1.25,screen.get_height()/2), "NO", font, "#000000", "#ff0000")
            mouse_pos = pygame.mouse.get_pos()
            
            for button in [yes_button, no_button]:
                button.changeColor(mouse_pos)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button.checkForInput(mouse_pos):
                        if player.balance >= property_object.price:
                            property_object.action(player)
                            player.add_property(property_object)
                            action = [(f"Player {player.name} bought"),
                                        (f"{property_object.name} for ${property_object.price}!"),
                                        (f"New Balance ${player.balance}")]
                            for inx,rect in enumerate(action_text_rect):
                                screen.fill((255, 255, 255), action_text_rect[inx])
                            action_text = [font.render(action[0], True, hex_to_rgb("#000000")), 
                                            font.render(action[1], True, hex_to_rgb("#000000")),
                                            font.render(action[2], True, hex_to_rgb("#000000")),]
                            action_text_rect = [action_text[0].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.75)),
                                                action_text[1].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.50)),
                                                action_text[2].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.25))]
                            for surface,rect in zip(action_text, action_text_rect):
                                screen.blit(surface,rect)
                            return
                        else:
                            action = [(f"Unable to buy{property_object.name} for ${property_object.price}"),
                                      (f"Not Enough Funds, Player Balance ${player.balance}")]
                            for inx,rect in enumerate(action_text_rect):
                                screen.fill((255, 255, 255), action_text_rect[inx])
                            action_text = [font.render(action[0], True, hex_to_rgb("#000000")), font.render(action[1], True, hex_to_rgb("#000000"))]
                            action_text_rect = [action_text[0].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.75)),
                                                action_text[1].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.50))]
                            for surface,rect in zip(action_text, action_text_rect):
                                screen.blit(surface,rect)
                            return
                    elif no_button.checkForInput(mouse_pos):
                        print("no")
                        return
        elif property_object.owner is not player:
            property_object.action(player)
            action = [(f"Player {property_object.owner_name}"),
                       (f"owns {property_object.name},"),
                      (f"pay ${property_object.calculate_rent(player)}"),
                      (f"{player.name}'s new Balance ${player.balance}")]
            action_text = [font.render(action[0], True, hex_to_rgb("#000000")), 
                           font.render(action[1], True, hex_to_rgb("#000000")), 
                           font.render(action[2], True, hex_to_rgb("#000000")),
                           font.render(action[3], True, hex_to_rgb("#000000")), ]
            action_text_rect = [action_text[0].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.75)),
                                action_text[1].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.50)),
                                action_text[2].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.25)),
                                action_text[3].get_rect(center=(screen.get_width() / 1.35, screen.get_height()/2.00)),]
            for surface,rect in zip(action_text, action_text_rect):
                screen.blit(surface,rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            return
        else:
            action = (f"You own {property_object.name}")
            action_text = font.render(action, True,hex_to_rgb("#000000"))
            action_text_rect = action_text.get_rect(center = (screen.get_width()/1.35, screen.get_height()/2))
            screen.blit(action_text,action_text_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            return
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

def _display_square_action(screen:pygame.Surface,square_object:Square, player:Player):
    font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 30)
    clock = pygame.time.Clock()
    run = True
    while run:
        if square_object.square_type == "corner":
            if square_object.name == "Go":
                action = (f"Landed on {square_object.name}, collect $200")
            else:
                action = (f"Landed on Free Parking")
            action_text = font.render(action, True,hex_to_rgb("#000000"))
            action_text_rect = action_text.get_rect(center = (screen.get_width()/1.35, screen.get_height()/2))
            screen.blit(action_text,action_text_rect)
            square_object.action(player)
            return
        elif square_object.square_type == "jail":
            action = (f"Landed on Jail, Just Visiting")
            action_text = font.render(action, True,hex_to_rgb("#000000"))
            action_text_rect = action_text.get_rect(center = (screen.get_width()/1.35, screen.get_height()/2))
            screen.blit(action_text,action_text_rect)
            square_object.action(player)
            return
        elif square_object.square_type == "go_to_jail":
            action = (f"GO TO JAIL!")
            action_text = font.render(action, True,hex_to_rgb("#000000"))
            action_text_rect = action_text.get_rect(center = (screen.get_width()/1.35, screen.get_height()/2))
            screen.blit(action_text,action_text_rect)
            square_object.action(player)
            return
        elif square_object.square_type == "tax":
            action = [ (f"Oh no! Landed on {square_object.name}!"), 
                        (f"Pay 10% of Balance = {int(player.balance * 0.1)}") , 
                        (f"New Balance = {player.balance - int(player.balance * 0.1)}") ]
            square_object.action(player)
            action_text = [font.render(action[0], True,hex_to_rgb("#000000")), 
                           font.render(action[1], True, hex_to_rgb("#000000")),
                           font.render(action[2],True, hex_to_rgb("#000000")) ]
            action_text_rect = [action_text[0].get_rect(center = (screen.get_width()/1.35, screen.get_height()/2.75)),
                                action_text[1].get_rect(center = (screen.get_width()/1.35, screen.get_height()/2.50)),
                                action_text[2].get_rect(center = (screen.get_width()/1.35, screen.get_height()/2.25)) ]
            for surface,rect in zip(action_text, action_text_rect):
                screen.blit(surface,rect)
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()    

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
