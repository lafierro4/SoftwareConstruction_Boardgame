# Cloneopoly
# Responsible for managing and coordination the game’s user interface. Interacts with other UI components for rendering and displaying the game information.
# This is where we will have all the pygame components, along with the other UI classes

# TO DO: Agree on short cut names for imports
import pygame,os
from Game_Engine.Player import Player
from User_Interface import MenuView, GameboardView, PlayerInfoView, util

# Initialze Pygame Window and sets the default window size to be 1280 by 720
pygame.init()
FPS = 60
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Cloneopoly")

class Cloneopoly:
    def __init__(self) -> None:
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
        players = self.initialize_players(player_info)
        self.main_game_loop(players)


    def initialize_players(self,player_info) -> list[Player]:
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


    def main_game_loop(self,players):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join("assets","sounds","mysteryLand.mp3"))
        pygame.mixer.music.set_volume(0.45)
        pygame.mixer.music.play(loops= -1)
        text_font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 35)
        button_font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 20)
        dice_img = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "dice.png")), (50, 50))
        button_background = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets","images","button_background.png")), 
                                                         ((self.gameboard.screen.get_width()/8.5),(self.gameboard.screen.get_height()/7)))
        player_info_buttons = []
        for index, player in enumerate(players):
            player_info_buttons.append(util.Button(((self.gameboard.screen.get_width() / 17.5) + (index * (self.gameboard.screen.get_width()/8.5)), (self.gameboard.screen.get_height()/1.05)), 
                                              text_input= (f"{player.name}'s Info"), font= button_font, base_color= "#000000",hover_color="#4100ff",image=button_background))
        dice_button = util.ImageButton(((self.gameboard.screen.get_width() / 1.75), (self.gameboard.screen.get_height() / 1.20)), dice_img)
        dice_surfaces = [pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", f"dice_{index}.png")), (50, 50)) for index in range(1, 7)]
        run = True
        roll_dice_timer = None  # Timer to control automatic dice rolling for AI player
        is_ai = False
        clock = pygame.time.Clock()
        current_player_index = 0
        while run:
            is_ai = players[current_player_index].name.startswith("AI")
            mouse_pos = pygame.mouse.get_pos()
            dice_button.update(self.gameboard.screen)
            for button in player_info_buttons:
                button.change_color(mouse_pos)
                button.update(self.gameboard.screen)
            #displays balance
            for i, player in enumerate(players):
                text_balance = text_font.render(f"{player.name}'s Balance {player.balance}", False, util.hex_to_rgb("#000000"))
                text_balance_rect = text_balance.get_rect(center=(self.gameboard.screen.get_width() / 1.35, self.gameboard.screen.get_height() / 16 + i * 30))
                self.gameboard.screen.blit(text_balance, text_balance_rect)

            turn_text = text_font.render(f"{players[current_player_index]._name}'s Turn, Roll Those Dice!", True, util.hex_to_rgb("#000000"))
            turn_text_rect = turn_text.get_rect(center=(self.gameboard.screen.get_width() / 1.35, self.gameboard.screen.get_height()/3.5))
            self.gameboard.screen.blit(turn_text, turn_text_rect)
            if is_ai:
                start_time = pygame.time.get_ticks()
                # Adjust the delay time (in milliseconds) as needed
                delay_duration = 3000  
                while pygame.time.get_ticks() - start_time < delay_duration:
                    pygame.display.update()
                    clock.tick(FPS)
                self.gameboard.dice_is_being_rolled(players, dice_surfaces, current_player_index)
                current_player_index = (current_player_index + 1) % len(players)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if dice_button.check_clicked(mouse_pos):
                            self.gameboard.dice_is_being_rolled(players, dice_surfaces, current_player_index)
                            current_player_index = (current_player_index + 1) % len(players)
                        for current_player,player_button in enumerate(player_info_buttons):
                            if player_button.check_clicked(mouse_pos):
                                PlayerInfoView.display_player_info(player= players[current_player])
            pygame.display.update()
            clock.tick(FPS)
    

        pygame.quit()
        quit()
