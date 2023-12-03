# Cloneopoly
# Responsible for managing and coordination the game’s user interface. Interacts with other UI components for rendering and displaying the game information.
# This is where we wigameboard.screenll have all the pygame components, along with the other UI classes

# TO DO: Agree on short cut names for imports
import pygame,os
from typing import List
from Game_Engine.Player import Player
from Game_Engine import Property, Square
from User_Interface import MenuView, GameboardView, PlayerInfoView, util
from Computer.Strategy import Strategy

# Initialze Pygame Window and sets the default window size to be 1280 by 720
pygame.init()
FPS = 60
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Cloneopoly")

class Cloneopoly:
    def __init__(self) -> None:
        self.players: List[Player] = []
        self.player_buttons: List[util.Button] = []
        self.number_of_players = MenuView.main_menu(SCREEN)
        self.initialize_game(self.number_of_players)

    def initialize_game(self,number_of_players):
        """
        The Initial Game Loop,
        """
        is_ai = False
        number_of_humans = number_of_players[0] # type: ignore
        number_of_bots = number_of_players[1] # type: ignore
        number_players = number_of_humans + number_of_bots
        if number_of_bots > 0:
            is_ai = True
        player_info = PlayerInfoView.player_select_screen(SCREEN, number_players, is_ai) # type: ignore
        SCREEN.fill("white")
        self.gameboard= GameboardView.GameboardView(SCREEN)
        self.gameboard.setup_board()
        pygame.display.update()
        self.players = self.initialize_players(player_info)
        self.main_game_loop()


    def initialize_players(self,player_info) -> List[Player]:
        player_names, player_tokens = player_info
        space_size = SCREEN.get_width() / 25.6
        tokens = util.token_image_surface(space_size/1.4)
        players: List[Player] = []
        for name, token in zip(player_names,player_tokens):
            player = Player(name,tokens[token],space_size)
            player.set_position(space_size * 11, space_size * 11)
            players.append(player)
            SCREEN.blit(tokens[token], (player._position_x, player._position_y))
        
        pygame.display.flip()
        return players

    def main_game_loop(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join("assets","sounds","mysteryLand.mp3"))
        pygame.mixer.music.set_volume(0.45)
        pygame.mixer.music.play(loops= -1)
        text_font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 35)
        button_font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 20)
        dice_img = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "dice.png")), (50, 50))
        button_background = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets","images","button_background.png")), 
                                                         ((self.gameboard.screen.get_width()/8.5),(self.gameboard.screen.get_height()/7)))
        for index, player in enumerate(self.players):
                button = util.Button(((self.gameboard.screen.get_width() / 17.5) + (index * (self.gameboard.screen.get_width()/8.5)), (self.gameboard.screen.get_height()/1.05)), 
                                                text_input= (f"{player.name}'s Info"), font= button_font, base_color= "#000000",hover_color="#4100ff",image=button_background)
                player.button = button
                self.player_buttons.append(button)
        
        dice_button = util.ImageButton(((self.gameboard.screen.get_width() / 1.75), (self.gameboard.screen.get_height() / 1.20)), dice_img)
        run = True
        roll_dice_timer = None  # Timer to control automatic dice rolling for AI player
        is_ai = False
        clock = pygame.time.Clock()
        current_player_index = 0
        while run:
            is_ai = self.players[current_player_index].name.startswith("AI")
            mouse_pos = pygame.mouse.get_pos()
            dice_button.update(self.gameboard.screen)
            
            for button in self.player_buttons:
                button.change_color(mouse_pos)
                button.update(self.gameboard.screen)
            #displays balance
            for i, player in enumerate(self.players):
                text_balance = text_font.render(f"{player.name}'s Balance {player.balance}", False, util.hex_to_rgb("#000000"))
                text_balance_rect = text_balance.get_rect(center=(self.gameboard.screen.get_width() / 1.35, self.gameboard.screen.get_height() / 16 + i * 30))
                self.gameboard.screen.blit(text_balance, text_balance_rect)

            turn_text = text_font.render(f"{self.players[current_player_index]._name}'s Turn, Roll Those Dice!", True, util.hex_to_rgb("#000000"))
            turn_text_rect = turn_text.get_rect(center=(self.gameboard.screen.get_width() / 1.35, self.gameboard.screen.get_height()/3.5))
            self.gameboard.screen.blit(turn_text, turn_text_rect)
            if is_ai:
                start_time = pygame.time.get_ticks()
                # Adjust the delay time (in milliseconds) as needed
                delay_duration = 3000  
                while pygame.time.get_ticks() - start_time < delay_duration:
                    pygame.display.update()
                    clock.tick(FPS)
                updated_player_space = self.gameboard.dice_is_being_rolled(self.players, current_player_index)
                self.display_action(updated_player_space[0],updated_player_space[1])
                current_player_index = (current_player_index + 1) % len(self.players)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if dice_button.check_clicked(mouse_pos):
                            updated_player_space = self.gameboard.dice_is_being_rolled(self.players, current_player_index)
                            self.display_action(updated_player_space[0],updated_player_space[1])
                            current_player_index = (current_player_index + 1) % len(self.players)
                        for player_index,player_button in enumerate(self.player_buttons):
                            if player_button.check_clicked(mouse_pos):
                                PlayerInfoView.display_player_info(player= self.players[player_index])
            pygame.display.update()
            clock.tick(FPS)
        pygame.quit()
        quit()

    def display_action(self,player:Player, board_index:int):
        current_space = self.gameboard.board[board_index]
        if isinstance(current_space,Property.Property):
            self._display_property_action(current_space,player)
        elif isinstance(current_space,Square.Square):
            self._display_square_action(current_space,player)
        return

    def property_is_being_bought(self, player:Player, property_object: Property.Property, text_rect):
        font = pygame.font.Font(os.path.join("assets", "images", "Minecraft.ttf"), 30)
        if player.balance >= property_object.price:
            property_object.action(player)
            player.add_property(property_object)
            #Move Action phrases to Property action method
            action = [(f"Player {player.name} bought"),
                        (f"{property_object.name} for ${property_object.price}!"),
                        (f"New Balance ${player.balance}")]
            for inx,rect in enumerate(text_rect):
                self.gameboard.screen.fill((255, 255, 255), text_rect[inx])
            action_text = [font.render(line, True, util.hex_to_rgb("#000000")) for line in action]
            action_text_rect = [text.get_rect(center=(self.gameboard.screen.get_width() / 1.35, self.gameboard.screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
            for surface,rect in zip(action_text, action_text_rect):
                self.gameboard.screen.blit(surface,rect)
            return
        else:
            action = [(f"Unable to buy{property_object.name} for ${property_object.price}"),
                        (f"Not Enough Funds, Player Balance ${player.balance}")]
            for inx,rect in enumerate(text_rect):
                self.gameboard.screen.fill((255, 255, 255), text_rect[inx])
            action_text = [font.render(line, True, util.hex_to_rgb("#000000")) for line in action]
            action_text_rect = [text.get_rect(center=(self.gameboard.screen.get_width() / 1.35, self.gameboard.screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
            for surface,rect in zip(action_text, action_text_rect):
                self.gameboard.screen.blit(surface,rect)
            return
    
    def _display_property_action(self, property_object: Property.Property, player: Player):
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
                        text_rect = self.display_text(action_lines)
                        self.property_is_being_bought(player, property_object, text_rect)
                        return
                    else:
                        # AI Player did not buy the property
                        action_lines[0] = f"{player.name} chose not to buy"
                        self.display_text(action_lines)
                        return
                else:
                    text_rect = self.display_text(action_lines)
                    yes_button = util.Button((self.gameboard.screen.get_width() / 1.25 - 150, self.gameboard.screen.get_height() / 2), "YES", font,
                                            text_color, "#00ff00")
                    no_button = util.Button((self.gameboard.screen.get_width() / 1.25, self.gameboard.screen.get_height() / 2), "NO", font,
                                            text_color, "#ff0000")

                    mouse_pos = pygame.mouse.get_pos()
                    for button in [yes_button, no_button]:
                        button.change_color(mouse_pos)
                        button.update(self.gameboard.screen)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if yes_button.check_clicked(mouse_pos):
                                self.property_is_being_bought(player, property_object, text_rect)
                                return
                            elif no_button.check_clicked(mouse_pos):
                                return

            elif property_object.owner is not player:
                transfer_successful = property_object.action(player)
                action_lines = [ f"Player {property_object.owner_name}",f"owns {property_object.name},",
                    f"pay ${property_object.calculate_rent(player)}",
                    ]
                if not transfer_successful:
                    self.handle_bankrupt(player)
                    action_lines.append(f"Not enough funds...{player.name} is bankrupt!")
                else:
                    action_lines.append(f"{player.name}'s new Balance ${player.balance}")
                self.display_text(action_lines)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                return
            else:
                action_lines = [f"You own {property_object.name}"]
                self.display_text(action_lines)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                return

            pygame.display.update()
            clock.tick(FPS)

        pygame.quit()
        quit()

    def handle_bankrupt(self,player:Player):
        if player.assets is not None:
            for asset in player.assets:
                asset.reset()
        self.players.remove(player)
        if player.button is not None:
            if player.button in self.player_buttons:
                self.player_buttons.remove(player.button)


    def _display_square_action(self, square_object: Square.Square, player: Player):
        clock = pygame.time.Clock()
        match(square_object.space_type):
            case "corner":
                if square_object.name == "Go":
                    action_lines = [f"Landed on {square_object.name}, collect $200"]
                else:
                    action_lines = [f"Landed on Free Parking"]
            case "jail":
                action_lines = [f"Landed on Jail, Just Visiting"]
            case "go_to_jail":
                action_lines = [f"GO TO JAIL!"]
            case "tax":
                action_lines = [f"Oh no! Landed on {square_object.name}!", f"Pay 10% of Balance = {int(player.balance * 0.1)}", 
                    f"New Balance = {player.balance - int(player.balance * 0.1)}",
                ] 
            case _:
                action_lines = f"Error Square Type\nNot Found"

        square_object.action(player)
        self.display_text(action_lines)
        pygame.display.update()
        clock.tick(FPS)

    def display_text(self, action_lines):
        font = pygame.font.Font(os.path.join("assets", "images", "Minecraft.ttf"), 30)
        text_color = util.hex_to_rgb("#000000")
        action_text = [font.render(line, True, text_color) for line in action_lines]
        action_text_rect = [
            text.get_rect(center=(self.gameboard.screen.get_width() / 1.35, self.gameboard.screen.get_height() / (3 - i * 0.25)))
            for i, text in enumerate(action_text)
        ]
        for surface, rect in zip(action_text, action_text_rect):
            self.gameboard.screen.blit(surface, rect)
        pygame.display.update()
        return action_text_rect