# GameboardView
# In charge of rendering the game board, properties, and other visual
# elements related to the game board. Handles user interactions with the game board, such as property selections and purchases.
import pygame, os, random

FPS = 60
WIDTH, HEIGHT = 1280, 720
from Game_Engine.Square import Square
from Game_Engine.Property import Property
from User_Interface.PlayerInfoView import *
from User_Interface.util import *
from AI.Strategy import Strategy

class GameboardView:
    #Sam- Added this 
    is_ai = False
    def __init__(self,screen:pygame.Surface):
        self.screen = screen
        self.space_size = screen.get_width() / 25.6
        self._board = [
            Square("Go","corner"),
            Property("Mediterranean Meals", "property", "#a37759", 60, [2, 10, 30, 90, 160, 250], 50),
            Square("Lice Tax", "tax"),
            Property("Baltic Breezeway", "property", "#a37759", 60, [4, 20, 60, 180, 320, 450], 50),
            Square("Income Tax", "tax"),
            Property("Skipping Railroad", "property", "#000000", 200, [25, 50, 100, 200]), 
            Property("Oriental Oasis", "property", "#e8a541", 100, [6, 30, 90, 270, 400, 550], 50),
            Square("Apple Tax", "tax"),
            Property("Vermont Vacation", "property", "#e8a541", 100, [6, 30, 90, 270, 400, 550], 50),
            Property("Connecticut Courtyard", "property", "#e8a541", 120, [8, 40, 100, 300, 450, 600],  50),
            Square("Jail", "jail"),
            Property("Sir Charles' Sanctuary", "property", "#a14685", 140, [10, 50, 150, 450, 625, 750],  100),
            Property("Electric Company", "utility", "#a37759", 150),
            Property("United Estates", "property", "#a14685", 140, [10, 50, 150, 450, 625, 750],  100),
            Property("Virginia Vineyards", "property", "#a14685", 160, [12, 60, 180, 500, 700, 900], 100),
            Property("Quarter Railroad", "property", "#000000", 200, [25, 50, 100, 200],100),
            Property("Saintly James' Square", "property", "#ef756d", 180, [14, 70, 200, 550, 750, 950], 100),
            Square("Charity Tax", "tax"),
            Property("Tunessee Avenue", "property", "#ef756d", 180, [14, 70, 200, 550, 750, 950], 100),
            Property("Big Apple Avenue", "property", "#ef756d", 200, [16, 80, 220, 600, 800, 1000], 100),
            Square("Free Parking", "corner"),
            Property("Kentucky Fried Avenue", "property", "#ca6e47", 220, [18, 90, 250, 700, 875, 1050], 150),
            Square("Bad Hair Tax", "tax"),
            Property("Indy Car Avenue", "property", "#ca6e47", 220, [18, 90, 250, 700, 875, 1050], 150),
            Property("Illusion Avenue", "property", "#ca6e47", 240, [20, 100, 300, 750, 925, 1100],  150),
            Property("R. R. Railroad", "property", "#000000", 200, [25, 50, 100, 200]),
            Property("Atlantic Adventure", "property", "#2277a2", 260, [22, 110, 330, 800, 975, 1150], 150),
            Property("Ventilation Avenue", "property", "#2277a2", 260, [22, 110, 330, 800, 975, 1150], 150),
            Property("Water Works", "utility", "#a37759", 150),
            Property("Marvin's Magic Meadow", "property", "#2277a2", 280, [24, 120, 360, 850, 1025, 1200], 150),
            Square("Go To Jail", "go_to_jail"),
            Property("Pacific Playground", "property", "#55a95d", 300, [26, 130, 390, 900, 1100, 1275], 200),
            Property("Northern Charm Avenue", "property", "#55a95d", 300, [26, 130, 390, 900, 1100, 1275], 200),
            Square("Juice Tax", "tax"),
            Property("Penny-sylvania Avenue", "property", "#55a95d", 320, [28, 150, 450, 1000, 1200, 1400], 200),
            Property("Longline Railroad", "property", "#000000", 200, [25, 50, 100, 200]),
            Square("Candy Tax", "tax"),
            Property("Parking Place", "property", "#e34537", 350, [35, 175, 500, 1100, 1300, 1500], 200),
            Square("Luxury Tax", "tax"),
            Property("Bored Walk", "property", "#e34537", 400, [50, 200, 600, 1400, 1700, 2000], 200),
        ]
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
                hex_to_rgb("#cce6cf"),
                (x, y, int(self.space_size * 2), int(self.space_size * 2)),
            )
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#171717"),
                (x, y, int(self.space_size * 2), int(self.space_size * 2)),
                width=self.border_width,
            )
        elif is_lateral:
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb(color),
                (x, y, int(self.space_size * 2), int(self.space_size)),
            )
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#171717"),
                (x, y, int(self.space_size * 2), int(self.space_size)),
                width=self.border_width,
            )
        else:
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb(color),
                (x, y, int(self.space_size), int(self.space_size * 2)),
            )
            pygame.draw.rect(
                self.board_surface,
                hex_to_rgb("#171717"),
                (x, y, int(self.space_size), int(self.space_size * 2)), 
                width = self.border_width
            )

    def render_player_move(self, players:list[Player], current_player: Player | None, steps: int):
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
            
    def main_loop_screen(self,players: list[Player]):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join("assets","sounds","mysteryLand.mp3"))
        pygame.mixer.music.set_volume(0.45)
        pygame.mixer.music.play(loops= -1)
        text_font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 35)
        button_font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 20)
        player_info_font = pygame.font.Font(os.path.join("assets", "images", "Minecraft.ttf"), 25)
        dice_img = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "dice.png")), (50, 50))
        button_background = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets","images","button_background.png")), 
                                                         ((self.screen.get_width()/8.5),(self.screen.get_height()/7)))
        win_image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "win.jpg")), (self.screen.get_width(), self.screen.get_height()))
        player_info_buttons = []
        for index, player in enumerate(players):
            player_info_buttons.append(Button(((self.screen.get_width() / 17.5) + (index * (self.screen.get_width()/8.5)), (self.screen.get_height()/1.05)), 
                                              text_input= (f"{player.name}'s Info"), font= button_font, base_color= "#000000",hover_color="#4100ff",image=button_background))
        dice_button = ImageButton(((self.screen.get_width() / 1.75), (self.screen.get_height() / 1.20)), dice_img)
        dice_surfaces = [pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", f"dice_{index}.png")), (50, 50)) for index in range(1, 7)]
        run = True
        roll_dice_timer = None  # Timer to control automatic dice rolling for AI player
        clock = pygame.time.Clock()
        current_player_index = 0
        while run:
            #Sam-added this line
            GameboardView.is_ai = players[current_player_index].name.startswith("AI")
            mouse_pos = pygame.mouse.get_pos()
            dice_button.update(self.screen)
            for button in player_info_buttons:
                button.change_color(mouse_pos)
                button.update(self.screen)
            #Sam - added these 8 lines below for the balance
            margin = 10  
            for i, player in enumerate(players):
                # display balance
                player_info = f"{player.name}'s Balance: {player.balance}"
                text_surface = player_info_font.render(player_info, True, (0, 255, 0), (255, 255, 255))
                text_rect = text_surface.get_rect(center=(self.screen.get_width() / 1.35, self.screen.get_height() / 16 + i * (30 + margin)))
                box_rect = pygame.Rect(text_rect.x - 10, text_rect.y - 5, text_rect.width + 20, text_rect.height + 10)
                pygame.draw.rect(self.screen, (255, 0, 0), box_rect, 2)
                self.screen.blit(text_surface, text_rect)
            
            active_players = [player for player in players if not player.is_bankrupt()]
            if len(active_players) == 1:
                start_time = pygame.time.get_ticks()
                delay_duration = 3000

                while pygame.time.get_ticks() - start_time < delay_duration:
                    pygame.display.update()
                    clock.tick(FPS)

                action = f"{active_players[0].name} Has Won! Click to play again."
                action_text = text_font.render(action, True, hex_to_rgb("#000000"))
                action_text_rect = action_text.get_rect(center = (self.screen.get_width() * 0.30, self.screen.get_height() * 0.8))

                self.screen.blit(win_image, (0,0))
                self.screen.blit(action_text, action_text_rect)
                
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                return
                    pygame.display.update()
                    clock.tick(FPS)

            turn_text = text_font.render(f"{players[current_player_index]._name}'s Turn, Roll Those Dice!", True, hex_to_rgb("#000000"))
            turn_text_rect = turn_text.get_rect(center=(self.screen.get_width() / 1.35, self.screen.get_height()/3.5))
            self.screen.blit(turn_text, turn_text_rect)
            #Sam- added this to check if its ai and roll the dice and move player without clicking dice
            if GameboardView.is_ai:
                start_time = pygame.time.get_ticks()
                # Adjust the delay time (in milliseconds) as needed
                delay_duration = 3000  
                while pygame.time.get_ticks() - start_time < delay_duration:
                    pygame.display.update()
                    clock.tick(FPS)
                self.dice_is_being_rolled(players, dice_surfaces, current_player_index)
                current_player_index = (current_player_index + 1) % len(players)
                
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if dice_button.check_clicked(mouse_pos):
                            self.dice_is_being_rolled(players, dice_surfaces, current_player_index)
                            current_player_index = (current_player_index + 1) % len(players)
                        for current_player,player_button in enumerate(player_info_buttons):
                            if player_button.check_clicked(mouse_pos):
                                display_player_info(players[current_player])
            pygame.display.update()
            clock.tick(FPS)

    def dice_is_being_rolled(self, players, dice_surfaces, current_player_index):
        dice_rolls =(random.randint(1, 6), random.randint(1, 6))
        steps = sum(dice_rolls)
        if players[current_player_index].in_jail():
            if all(roll == dice_rolls[0] for roll in dice_rolls):
                players[current_player_index].set_jail_status(False)
                players[current_player_index].move(steps)
                self.render_player_move(players, players[current_player_index], steps)
            else:
                # Updates screen even if player doesn't roll doubles
                self.render_player_move(players, None, 1)
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
    
def property_is_being_bought(player: Player, property_object: Property, action_text, action, action_text_rect, screen, font):
    if player.balance >= property_object.price:
        property_object.action(player)
        player.add_property(property_object)
        #Move Action phrases to Property action method
        action = [(f"Player {player.name} bought"),
                    (f"{property_object.name} for ${property_object.price}!"),
                    (f"New Balance ${player.balance}")]
        for inx,rect in enumerate(action_text_rect):
            screen.fill((255, 255, 255), action_text_rect[inx])
        action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
        action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
        for surface,rect in zip(action_text, action_text_rect):
            screen.blit(surface,rect)
        return
    else:
        action = [(f"Unable to buy{property_object.name} for ${property_object.price}"),
                    (f"Not Enough Funds, Player Balance ${player.balance}")]
        for inx,rect in enumerate(action_text_rect):
            screen.fill((255, 255, 255), action_text_rect[inx])
        action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
        action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
        for surface,rect in zip(action_text, action_text_rect):
            screen.blit(surface,rect)
        return
# Long Method, idk how we can split it
def _display_property_action(screen:pygame.Surface,property_object:Property,player:Player):
    font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 30)
    clock = pygame.time.Clock()
    run = True
    is_ai = player.name.startswith("AI")
    while run:
        if not property_object.is_owned():      
            action = [(f"Would you like to buy"),
                    (f"{property_object.name}"),
                        (f"for ${property_object.price}?")]
            #Sam-added this if statement and everything inside it for ai
            if is_ai:
                if Strategy.should_buy_property(property_object,player): 
                    action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
                    action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
                    for surface,rect in zip(action_text, action_text_rect):
                        screen.blit(surface,rect)
                    property_is_being_bought(player, property_object, action_text, action, action_text_rect, screen, font)
                    #handles the ai houses to buy houses randomly when ai reaches property
                    ai_buy_house(property_object)
                    return
                else:
                    # AI Player did not buy the property
                    action = [(f"{player.name} chose not to buy"),
                    (f"{property_object.name}"),
                        (f"for ${property_object.price}")]
                    action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
                    action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
                    for surface, rect in zip(action_text, action_text_rect):
                        screen.blit(surface, rect)
                    pygame.display.update()
                    return
            else:    
                action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
                action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
                for surface,rect in zip(action_text, action_text_rect):
                    screen.blit(surface,rect)
                yes_button  = Button((screen.get_width()/1.25-150,screen.get_height()/2),"YES", font, "#000000", "#00ff00")
                no_button = Button((screen.get_width()/1.25,screen.get_height()/2), "NO", font, "#000000", "#ff0000")
                mouse_pos = pygame.mouse.get_pos()
                
                for button in [yes_button, no_button]:
                    button.change_color(mouse_pos)
                    button.update(screen)
                clicked = False  # Variable to track whether a button was clicked
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if yes_button.check_clicked(mouse_pos):
                            property_is_being_bought(player, property_object,action_text, action, action_text_rect, screen, font)
                            clicked = True
                        elif no_button.check_clicked(mouse_pos):
                            clicked = True
                            #return
                if clicked:
                    return
        elif property_object.owner is not player:
            property_object.action(player)
            action = [(f"Player {property_object.owner_name}"),
                       (f"owns {property_object.name},"),
                      (f"pay ${property_object.calculate_rent(player)}"),
                      (f"{player.name}'s new Balance ${player.balance}")]
            action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
            action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
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
            action = (f"Must Roll Doubles to Leave Jail!") if player.in_jail() else (f"Landed on Jail, Just Visiting")
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
            action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
            action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
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