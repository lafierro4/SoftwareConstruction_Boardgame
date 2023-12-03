# GameboardView
# In charge of rendering the game board, properties, and other visual
# elements related to the game board. Handles user interactions with the game board, such as property selections and purchases.
import pygame, os, random

FPS = 60
WIDTH, HEIGHT = 1280, 720
from Game_Engine.Square import Square
from Game_Engine.Property import Property
from User_Interface import util
from Game_Engine.Player import Player
from Computer.Strategy import Strategy

class GameboardView:
    def __init__(self,screen:pygame.Surface):
        self.screen = screen
        self.space_size = screen.get_width() / 25.6
        self._board = util.board_spaces()
        self.board_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.border_width = 2

    def setup_board(self):
        self.board_surface.fill((255, 255, 255))
        index = 0
        for row in range(1, 14):
            for col in range(1, 14):
                x = (col - 1) * self.space_size
                y = (row - 1) * self.space_size
                # space how to implement this
                space = self._board[2]
                if (row == 1 or row == 12):
                    if(col == 1 or col == 12):   
                        self.draw_rectangle(x, y, True, False, space.color)
                        if col != 1:
                            index += 1
                    elif col == 2 or col == 13:
                        continue
                    else:
                        self.draw_rectangle(x, y, False, False, space.color)
                        index += 1
                elif (2 < row < 12) and (col == 1 or col == 12):
                    self.draw_rectangle(x, y, False, True, space.color)
                    index += 1
                else:
                    continue
               # print(index, x, row, y, col)
        self.screen.blit(self.board_surface, (0, 0))

    def draw_rectangle(self, x, y, is_corner, is_lateral, color):
        if is_corner:
            pygame.draw.rect(
                self.board_surface,
                util.hex_to_rgb("#cce6cf"),
                (x, y, int(self.space_size * 2), int(self.space_size * 2)),
            )
            pygame.draw.rect(
                self.board_surface,
                util.hex_to_rgb("#171717"),
                (x, y, int(self.space_size * 2), int(self.space_size * 2)),
                width=self.border_width,
            )
        elif is_lateral:
            pygame.draw.rect(
                self.board_surface,
                util.hex_to_rgb(color),
                (x, y, int(self.space_size * 2), int(self.space_size)),
            )
            pygame.draw.rect(
                self.board_surface,
                util.hex_to_rgb("#171717"),
                (x, y, int(self.space_size * 2), int(self.space_size)),
                width=self.border_width,
            )
        else:
            pygame.draw.rect(
                self.board_surface,
                util.hex_to_rgb(color),
                (x, y, int(self.space_size), int(self.space_size * 2)),
            )
            pygame.draw.rect(
                self.board_surface,
                util.hex_to_rgb("#171717"),
                (x, y, int(self.space_size), int(self.space_size * 2)), 
                width = self.border_width
            )

    def render_player_move(self, players:list[Player], current_player: Player, steps: int):
        for step in range(steps):
            self.screen.blit(self.board_surface, (0, 0))

            for player in players:
                total_pos = (player.position - steps + step + 1) % 40 if player is current_player else player.position
                offset_pos = (player.position - steps + step + 1) % 10 if player is current_player else player.position % 10
                if total_pos < 10:
                    self.screen.blit(player.token, (self.space_size * (11 - offset_pos), self.space_size * 11))
                elif total_pos < 20:
                    self.screen.blit(player.token, (self.space_size, self.space_size * (11 - offset_pos)))
                elif total_pos < 30:
                    self.screen.blit(player.token, (self.space_size * (offset_pos + 1), self.space_size))
                else:
                    self.screen.blit(player.token, (self.space_size * 11, self.space_size * (offset_pos + 1)))
            
            pygame.display.update()
            pygame.time.delay(250)
            
    def dice_is_being_rolled(self, players, dice_surfaces, current_player_index):
        random.seed()
        dice_rolls =(random.randint(1, 6), random.randint(1, 6))
        #dice_rolls = (2,4)
        steps = sum(dice_rolls)
        if players[current_player_index].in_jail():
            if all(roll == dice_rolls[0] for roll in dice_rolls):
                players[current_player_index].set_jail_status(False)
                players[current_player_index].move(steps)
                self.render_player_move(players, players[current_player_index], steps)
        else:
            players[current_player_index].move(steps)
            self.render_player_move(players, players[current_player_index], steps)
        for index, roll in enumerate(dice_rolls):
            self.screen.blit(dice_surfaces[roll - 1], (self.screen.get_width() / (1.65 - index * 0.12), self.screen.get_height() / 1.25))
        self.display_action(players[current_player_index], players[current_player_index].position)


    def display_action(self,player:Player, square_index):
        current_space = self._board[square_index]
        if isinstance(current_space,Property):
            _display_property_action(self.screen,current_space,player)
        elif isinstance(current_space,Square):
            _display_square_action(self.screen,current_space,player)
        return
    
def property_is_being_bought(player: Player, property_object: Property, text_rect, screen, font):
    if player.balance >= property_object.price:
        property_object.action(player)
        player.add_property(property_object)
        #Move Action phrases to Property action method
        action = [(f"Player {player.name} bought"),
                    (f"{property_object.name} for ${property_object.price}!"),
                    (f"New Balance ${player.balance}")]
        for inx,rect in enumerate(text_rect):
            screen.fill((255, 255, 255), text_rect[inx])
        action_text = [font.render(line, True, util.hex_to_rgb("#000000")) for line in action]
        action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
        for surface,rect in zip(action_text, action_text_rect):
            screen.blit(surface,rect)
        return
    else:
        action = [(f"Unable to buy{property_object.name} for ${property_object.price}"),
                    (f"Not Enough Funds, Player Balance ${player.balance}")]
        for inx,rect in enumerate(text_rect):
            screen.fill((255, 255, 255), text_rect[inx])
        action_text = [font.render(line, True, util.hex_to_rgb("#000000")) for line in action]
        action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
        for surface,rect in zip(action_text, action_text_rect):
            screen.blit(surface,rect)
        return
# Long Method, idk how we can split it

def _display_property_action(screen: pygame.Surface, property_object: Property, player: Player):
    font = pygame.font.Font(os.path.join("assets", "images", "Minecraft.ttf"), 30)
    clock = pygame.time.Clock()
    run = True
    is_ai = player.name.startswith("AI")
    text_color = util.hex_to_rgb("#000000")

    while run:
        if not property_object.is_owned():
            action_lines = [f"Would you like to buy", f"{property_object.name}", f"for ${property_object.price}"]
            if is_ai:
                if Strategy.should_buy_property(property_object, player):
                    text_rect = display_text(action_lines)
                    property_is_being_bought(player, property_object, text_rect, screen, font)
                    return
                else:
                    # AI Player did not buy the property
                    action_lines[0] = f"{player.name} chose not to buy"
                    display_text(action_lines)
                    return
            else:
                text_rect = display_text(action_lines)
                yes_button = util.Button((screen.get_width() / 1.25 - 150, screen.get_height() / 2), "YES", font,
                                         text_color, "#00ff00")
                no_button = util.Button((screen.get_width() / 1.25, screen.get_height() / 2), "NO", font,
                                        text_color, "#ff0000")

                mouse_pos = pygame.mouse.get_pos()
                for button in [yes_button, no_button]:
                    button.change_color(mouse_pos)
                    button.update(screen)

                clicked = False  # Variable to track whether a Button was clicked
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if yes_button.check_clicked(mouse_pos):
                            property_is_being_bought(player, property_object, text_rect, screen, font)
                            clicked = True
                        elif no_button.check_clicked(mouse_pos):
                            clicked = True

                if clicked:
                    return
        elif property_object.owner is not player:
            property_object.action(player)
            action_lines = [ f"Player {property_object.owner_name}",f"owns {property_object.name},",
                f"pay ${property_object.calculate_rent(player)}", f"{player.name}'s new Balance ${player.balance}",
            ]
            display_text(action_lines)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            return
        else:
            action_lines = [f"You own {property_object.name}"]
            display_text(action_lines)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            return

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


def _display_square_action(screen: pygame.Surface, square_object: Square, player: Player):
    clock = pygame.time.Clock()
    run = True

    while run:
        if square_object.square_type == "corner":
            if square_object.name == "Go":
                action_lines = [f"Landed on {square_object.name}, collect $200"]
            else:
                action_lines = [f"Landed on Free Parking"]
            display_text(action_lines)
            square_object.action(player)
            return
        elif square_object.square_type == "jail":
            action_lines = [f"Landed on Jail, Just Visiting"]
            display_text(action_lines)
            square_object.action(player)
            return
        elif square_object.square_type == "go_to_jail":
            action_lines = [f"GO TO JAIL!"]
            display_text(action_lines)
            square_object.action(player)
            return
        elif square_object.square_type == "tax":
            action_lines = [f"Oh no! Landed on {square_object.name}!", f"Pay 10% of Balance = {int(player.balance * 0.1)}", 
                f"New Balance = {player.balance - int(player.balance * 0.1)}",
            ] 
            square_object.action(player)
            display_text(action_lines)
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

def display_text(action_lines):
        font = pygame.font.Font(os.path.join("assets", "images", "Minecraft.ttf"), 30)
        text_color = util.hex_to_rgb("#000000")
        action_text = [font.render(line, True, text_color) for line in action_lines]
        action_text_rect = [
            text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25)))
            for i, text in enumerate(action_text)
        ]
        for surface, rect in zip(action_text, action_text_rect):
            screen.blit(surface, rect)
        pygame.display.update()
        return action_text_rect