# GameboardView
# In charge of rendering the game board, properties, and other visual
# elements related to the game board. Handles user interactions with the game board, such as property selections and purchases.
import pygame, os, textwrap, math

FPS = 60
WIDTH, HEIGHT = 1280, 720
from Game_Engine.GameboardManager import Gameboard, Player, Property, Square
from User_Interface.PlayerInfoView import *
from User_Interface.util import *
from User_Interface.MenuView import options_menu

class GameboardView:
    def __init__(self, screen: pygame.Surface):
        self.gameboard = Gameboard()
        self.screen = screen
        self.space_size = screen.get_width() / 25.6
        self.squares = self.gameboard._board
        self.board_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.border_width = 2

        # Load images for each property
        self.property_images = {"GO.png": None, "medAve.png": None, "blank.png": None, "balticAve.png": None, "iTax.png": None, "readingRailroad.png": None,
                                "orientalAve.png": None, "blank.png": None, "vermontAve.png": None, "conAve.png": None, "jail.png": None,
                                "stCharles.png": None, "electricCompany.png": None, "statesAve.png": None, "virginiaAve.png": None, "penRailroad.png": None,
                                "stJames.png": None, "blank.png": None, "tenAve.png": None, "nyAve.png": None, "fParking.png": None, "kenAve.png": None,
                                "blank.png": None, "indiAve.png": None, "illiAve.png": None, "boRailroad.png": None, "atlAve.png": None, "venAve.png": None,
                                "waterWorks.png": None, "mGardensAve.png": None, "goToJail.png": None, "pacificAve.png": None, "nCarAve.png": None,
                                "blank.png": None, "penAve.png": None, "slRailroad.png": None, "blank.png": None, "parkPL.png": None, "luxTax.png": None,
                                "broadAve.png": None}

        for space in self.gameboard._board:

            # bottom row images
            go_path = "assets/images/GO.png"
            self.go_image = pygame.image.load(go_path)

            medAve_path = "assets/images/medAve.png"
            self.med_image = pygame.image.load(medAve_path)

            liceTax_path = "assets/images/blank.png"
            self.lice_image = pygame.image.load(liceTax_path)

            baltic_path = "assets/images/balticAve.png"
            self.baltic_image = pygame.image.load(baltic_path)

            iTax_path = "assets/images/iTax.png"
            self.iTax_image = pygame.image.load(iTax_path)

            rRail_path = "assets/images/readingRailroad.png"
            self.rRail_image = pygame.image.load(rRail_path)

            oriAve_path = "assets/images/orientalAve.png"
            self.oriAve_image = pygame.image.load(oriAve_path)

            blank_path = "assets/images/blank.png"
            self.blank_image = pygame.image.load(blank_path)

            verAve_path = "assets/images/vermontAve.png"
            self.verAve_image = pygame.image.load(verAve_path)

            conAve_path = "assets/images/conAve.png"
            self.conAve_image = pygame.image.load(conAve_path)

            jail_path = "assets/images/jail.png"
            self.jail_image = pygame.image.load(jail_path)

            # left column images
            stCharles_path = "assets/images/stCharles.png"
            self.stCharles_image = pygame.image.load(stCharles_path)

            electricCompany = "assets/images/electricCompany.png"
            self.electricCompany_image = pygame.image.load(electricCompany)

            statesAve = "assets/images/statesAve.png"
            self.statesAve_image = pygame.image.load(statesAve)

            virginiaAve = "assets/images/virginiaAve.png"
            self.virginiaAve_image = pygame.image.load(virginiaAve)

            penRailroad = "assets/images/penRailroad.png"
            self.penRailroad_image = pygame.image.load(penRailroad)

            stJames = "assets/images/stJames.png"
            self.stJames_image = pygame.image.load(stJames)

            blank_path = "assets/images/blank.png"
            self.blank_image = pygame.image.load(blank_path)

            tenAve = "assets/images/tenAve.png"
            self.tenAve_image = pygame.image.load(tenAve)

            nyAve = "assets/images/nyAve.png"
            self.nyAve_image = pygame.image.load(nyAve)

            fParking = "assets/images/fParking.png"
            self.fParking_image = pygame.image.load(fParking)

            kenAve = "assets/images/kenAve.png"
            self.kenAve_image = pygame.image.load(kenAve)

            #upper row images
            kenAve = "assets/images/kenAve.png"
            self.kenAve_image = pygame.image.load(kenAve)

            blank = "assets/images/blank.png"
            self.blank_image = pygame.image.load(blank)

            indiAve = "assets/images/indiAve.png"
            self.indiAve_image = pygame.image.load(indiAve)

            illiAve = "assets/images/illiAve.png"
            self.illiAve_image = pygame.image.load(illiAve)

            boRailroad = "assets/images/boRailroad.png"
            self.boRailroad = pygame.image.load(boRailroad)

            atlAve = "assets/images/atlAve.png"
            self.atlAve_image = pygame.image.load(atlAve)

            venAve = "assets/images/venAve.png"
            self.venAve_image = pygame.image.load(venAve)

            waterWorks = "assets/images/waterWorks.png"
            self.waterWorks_image = pygame.image.load(waterWorks)

            mGardensAve = "assets/images/mGardensAve.png"
            self.mGardensAve_image = pygame.image.load(mGardensAve)

            goToJail = "assets/images/goToJail.png"
            self.goToJail_image = pygame.image.load(goToJail)

            # right column images
            pacificAve_path = "assets/images/pacificAve.png"
            self.pacificAve_image = pygame.image.load(pacificAve_path)

            nCarAve = "assets/images/nCarAve.png"
            self.nCarAve_image = pygame.image.load(nCarAve)

            blank = "assets/images/blank.png"
            self.blank_image = pygame.image.load(blank)

            penAve = "assets/images/penAve.png"
            self.penAve_image = pygame.image.load(penAve)

            slRailroad = "assets/images/slRailroad.png"
            self.slRailroad_image = pygame.image.load(slRailroad)

            blank = "assets/images/blank.png"
            self.blank_image = pygame.image.load(blank)

            parkPL_path = "assets/images/parkPL.png"
            self.parkPL_image = pygame.image.load(parkPL_path)

            tenAve = "assets/images/tenAve.png"
            self.tenAve_image = pygame.image.load(tenAve)

            luxTax = "assets/images/luxTax.png"
            self.luxTax_image = pygame.image.load(luxTax)

            broadAve = "assets/images/broadAve.png"
            self.broadAve_image = pygame.image.load(broadAve)


    def setup_board(self):
        self.board_surface.fill((255, 255, 255))
        for row in range(1, 14):
            for col in range(1, 14):
                x = (col - 1) * self.space_size
                y = (row - 1) * self.space_size
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
                hex_to_rgb("#cce6cf"),
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
                hex_to_rgb("#cce6cf"),
                (x, y, int(self.space_size), int(self.space_size * 2)),
            )
            pygame.draw.rect(
<<<<<<< Updated upstream
                        self.board_surface,
                        hex_to_rgb("#171717"),
                        (x, y, int(self.space_size), int(self.space_size * 2)), width = self.border_width
                    )

    def render_player_move(self,players:list[Player], player: Player, distance: int):
=======
                self.board_surface,
                hex_to_rgb("#171717"),
                (x, y, int(self.property_size), int(self.property_size * 2)), width=self.border_width
            )

    def render_player_move(self, players, player: Player, distance: int):
>>>>>>> Stashed changes
        for step in range(distance):
            # Calculate the next position based on the step
            if player._position_y == self.space_size * 11:
                if player._position_x == self.space_size:
                    next_x, next_y = player._position_x, player._position_y - self.space_size
                else:
                    next_x, next_y = player._position_x - self.space_size, player._position_y
            elif player._position_y == self.space_size:
                if player._position_x == self.space_size * 11:
                    next_x, next_y = player._position_x, player._position_y + self.space_size
                else:
                    next_x, next_y = player._position_x + self.space_size, player._position_y
            else:
                if player._position_x == self.space_size:
                    next_x, next_y = player._position_x, player._position_y - self.space_size
                else:
                    next_x, next_y = player._position_x, player._position_y + self.space_size

            player._position_x, player._position_y = next_x, next_y
            self.draw_board(players)
            self.screen.blit(player.token, (player._position_x, player._position_y))
            pygame.display.update()
            pygame.time.delay(250)

<<<<<<< Updated upstream
    def draw_board(self,players:list[Player]):
        self.screen.blit(self.board_surface, (0, 0))
        for player in players:
            self.screen.blit(player.token, (player._position_x, player._position_y))
            
    def main_loop_screen(self,players: list[Player]):
        
        text_font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 35)
        button_font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 20)
        dice_img = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "dice.png")), (50, 50))
        button_background = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets","images","button_background.png")), 
                                                         ((self.screen.get_width()/8.5),(self.screen.get_height()/7)))
        player_info_buttons = []
        for index, player in enumerate(players):
            player_info_buttons.append(Button(((self.screen.get_width() / 17.5) + (index * (self.screen.get_width()/8.5)), (self.screen.get_height()/1.05)), 
                                              text_input= (f"{player.name}'s Info"), font= button_font, base_color= "#000000",hover_color="#4100ff",image=button_background))
        dice_button = ImageButton(((self.screen.get_width() / 1.75), (self.screen.get_height() / 1.20)), dice_img)
        dice_surfaces = [pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", f"dice_{index}.png")), (50, 50)) for index in range(1, 7)]
        
=======
    def draw_board(self, players):
        # Redraw the entire board (you may need to adapt this based on your implementation)
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

        # Iterate through the board to display property images
        for row in range(11):
            for col in range(11):
                index = row * 1 + col
                if index < len(self.gameboard._board):
                    space = self.gameboard._board[index]
                    x = col * self.property_size
                    y = row * self.property_size

                    if isinstance(space, Property):
                        if space in self.property_images:
                            property_image = self.property_images[space]
                            self.board_surface.blit(property_image, (x, y))
                        else:
                            # Handle the case where the image is not available
                            pygame.draw.rect(
                                self.board_surface,
                                hex_to_rgb("#cce6cf"),
                                (x, y, int(self.property_size), int(self.property_size * 2)),
                            )

        # Draw the GO square
        x_go = 11 * self.property_size
        y_go = 11 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(pygame.transform.scale(self.go_image, (specific_image_width, specific_image_height)),
                                (x_go, y_go))

        # Draw the mediterranean rectangle, bottom row begins
        x_specific = 10 * self.property_size
        y_specific = 11 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.med_image, (specific_image_width, specific_image_height)),
            (x_specific, y_specific))

        # Draw the liceTax rectangle
        x_lice = 9 * self.property_size
        y_lice = 11 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.lice_image, (specific_image_width, specific_image_height)),
            (x_lice, y_lice))

        # Draw the baltic rectangle
        x_baltic = 8 * self.property_size
        y_baltic = 11 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.baltic_image, (specific_image_width, specific_image_height)),
            (x_baltic, y_baltic))

        # Draw the iTax rectangle
        x_iTax = 7 * self.property_size
        y_iTax = 11 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.iTax_image, (specific_image_width, specific_image_height)),
            (x_iTax, y_iTax))

        # Draw the rRail rectangle
        x_rRail = 6 * self.property_size
        y_rRail = 11 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.rRail_image, (specific_image_width, specific_image_height)),
            (x_rRail, y_rRail))

        # Draw the oriAve rectangle
        x_oriAve = 5 * self.property_size
        y_oriAve = 11 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.oriAve_image, (specific_image_width, specific_image_height)),
            (x_oriAve, y_oriAve))

        # Draw the blank rectangle
        x_blank = 4 * self.property_size
        y_blank = 11 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.blank_image, (specific_image_width, specific_image_height)),
            (x_blank, y_blank))

        # Draw the vermontAve rectangle
        x_verAve = 3 * self.property_size
        y_verAve = 11 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.verAve_image, (specific_image_width, specific_image_height)),
            (x_verAve, y_verAve))

        # Draw the conAve rectangle
        x_conAve = 2 * self.property_size
        y_conAve = 11 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.conAve_image, (specific_image_width, specific_image_height)),
            (x_conAve, y_conAve))


        # Draw the jail square, bottom row ends
        x_jail = 0 * self.property_size
        y_jail = 11 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(pygame.transform.scale(self.jail_image, (specific_image_width, specific_image_height)),
                                (x_jail, y_jail))

        # left column begins
        # Draw the stCharles square, bottom row ends
        x_stCharles = 0 * self.property_size
        y_stCharles = 10 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.stCharles_image, (specific_image_width, specific_image_height)),
                                (x_stCharles, y_stCharles))


        # Draw the electric company rectangle
        x_electricCompany = 0 * self.property_size
        y_electricCompany = 9 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.electricCompany_image, (specific_image_width, specific_image_height)),
                                (x_electricCompany, y_electricCompany))

        # Draw the statesAve rectangle
        x_statesAve = 0 * self.property_size
        y_statesAve = 8 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.statesAve_image, (specific_image_width, specific_image_height)),
                                (x_statesAve, y_statesAve))

        # Draw the virginiaAve rectangle
        x_virginiaAve = 0 * self.property_size
        y_virginiaAve = 7 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.virginiaAve_image, (specific_image_width, specific_image_height)),
                                (x_virginiaAve, y_virginiaAve))

        # Draw the penRailroad rectangle
        x_penRailroad = 0 * self.property_size
        y_penRailroad = 6 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.penRailroad_image, (specific_image_width, specific_image_height)),
                                (x_penRailroad, y_penRailroad))

        # Draw the stJames rectangle
        x_stJames = 0 * self.property_size
        y_stJames = 5 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.stJames_image, (specific_image_width, specific_image_height)),
                                (x_stJames, y_stJames))

        # Draw the blank rectangle
        x_blank = 0 * self.property_size
        y_blank = 4 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.blank_image, (specific_image_width, specific_image_height)),
                                (x_blank, y_blank))

        # Draw the tenAve rectangle
        x_tenAve = 0 * self.property_size
        y_tenAve = 3 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.tenAve_image, (specific_image_width, specific_image_height)),
                                (x_tenAve, y_tenAve))

        # Draw the nyAve rectangle
        x_nyAve = 0 * self.property_size
        y_nyAve = 2 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.nyAve_image, (specific_image_width, specific_image_height)),
                                (x_nyAve, y_nyAve))

        # Draw the fParking square, end of the left column
        x_fParking = 0 * self.property_size
        y_fParking = 0 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(pygame.transform.scale(self.fParking_image, (specific_image_width, specific_image_height)),
                                (x_fParking, y_fParking))

        # upper row begins, Draw the KenAve rectangle
        # Draw the KenAve rectangle, bottom row begins
        x_KenAve = 2 * self.property_size
        y_KenAve = 0 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.kenAve_image, (specific_image_width, specific_image_height)),
            (x_KenAve, y_KenAve))

        # Draw the blank.png rectangle
        x_blank = 3 * self.property_size
        y_blank = 0 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.blank_image, (specific_image_width, specific_image_height)),
            (x_blank, y_blank))

        # Draw the indiAve rectangle
        x_indiAve = 4 * self.property_size
        y_indiAve = 0 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.indiAve_image, (specific_image_width, specific_image_height)),
            (x_indiAve, y_indiAve))

        # Draw the illiAve rectangle
        x_illiAve = 5 * self.property_size
        y_illiAve = 0 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.illiAve_image, (specific_image_width, specific_image_height)),
            (x_illiAve, y_illiAve))

        # Draw the boRailroad rectangle
        x_boRailroad = 6 * self.property_size
        y_boRailroad = 0 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.boRailroad, (specific_image_width, specific_image_height)),
            (x_boRailroad, y_boRailroad))

        # Draw the atlAve rectangle
        x_atlAve = 7 * self.property_size
        y_atlAve = 0 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.atlAve_image, (specific_image_width, specific_image_height)),
            (x_atlAve, y_atlAve))

        # Draw the venAve rectangle
        x_venAve = 8 * self.property_size
        y_venAve = 0 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.venAve_image, (specific_image_width, specific_image_height)),
            (x_venAve, y_venAve))

        # Draw the waterWorks rectangle
        x_waterWorks = 9 * self.property_size
        y_waterWorks = 0 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.waterWorks_image, (specific_image_width, specific_image_height)),
            (x_waterWorks, y_waterWorks))

        # Draw the mGardensAve rectangle
        x_mGardensAve = 10 * self.property_size
        y_mGardensAve = 0 * self.property_size
        specific_image_width = int(self.property_size / 1.02)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(
            pygame.transform.scale(self.mGardensAve_image, (specific_image_width, specific_image_height)),
            (x_mGardensAve, y_mGardensAve))

        # Draw the goToJail square, end of the upper row
        x_goToJail = 11 * self.property_size
        y_goToJail = 0 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size * 1.98)
        self.board_surface.blit(pygame.transform.scale(self.goToJail_image, (specific_image_width, specific_image_height)),
                                (x_goToJail, y_goToJail))

        # right column begins
        # Draw the pacificAve rectangle
        x_pacificAve = 11 * self.property_size
        y_pacificAve = 2 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.pacificAve_image, (specific_image_width, specific_image_height)),
                                (x_pacificAve, y_pacificAve))

        # Draw the nCarAve rectangle
        x_nCarAve = 11 * self.property_size
        y_nCarAve = 3 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.nCarAve_image, (specific_image_width, specific_image_height)),
                                (x_nCarAve, y_nCarAve))

        # Draw the blank rectangle
        x_blank = 11 * self.property_size
        y_blank = 4 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.blank_image, (specific_image_width, specific_image_height)),
                                (x_blank, y_blank))

        # Draw the penAve rectangle
        x_penAve = 11 * self.property_size
        y_penAve = 5 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.penAve_image, (specific_image_width, specific_image_height)),
                                (x_penAve, y_penAve))

        # Draw the slRailroad rectangle
        x_slRailroad = 11 * self.property_size
        y_slRailroad = 6 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.slRailroad_image, (specific_image_width, specific_image_height)),
                                (x_slRailroad, y_slRailroad))

        # Draw the blank rectangle
        x_blank = 11 * self.property_size
        y_blank = 7 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.blank_image, (specific_image_width, specific_image_height)),
                                (x_blank, y_blank))

        # Draw the parkPL rectangle
        x_parkPL = 11 * self.property_size
        y_parkPL = 8 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.parkPL_image, (specific_image_width, specific_image_height)),
                                (x_parkPL, y_parkPL))

        # Draw the luxTax rectangle
        x_luxTax = 11 * self.property_size
        y_luxTax = 9 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.luxTax_image, (specific_image_width, specific_image_height)),
                                (x_luxTax, y_luxTax))

        # Draw the boardAve rectangle
        x_broadAve = 11 * self.property_size
        y_broadAve = 10 * self.property_size
        specific_image_width = int(self.property_size * 1.98)
        specific_image_height = int(self.property_size / 1.02)
        self.board_surface.blit(pygame.transform.scale(self.broadAve_image, (specific_image_width, specific_image_height)),
                                (x_broadAve, y_broadAve))


        # Add code to redraw all player tokens at their current positions
        for player in players:
            self.screen.blit(player.token, (player._position_x, player._position_y))

        self.screen.blit(self.board_surface, (0, 0))
        pygame.display.update()

    def initialize_players(self, number_players) -> list[Player]:
        players = []

        tokens = (
        pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "car.png")).convert_alpha(),
                                     (35, 35)),
        pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "penguin.png")).convert_alpha(),
                                     (35, 35)))

        player_one = Player("Michel", tokens[0], self.property_size, 0)
        player_two = Player("Luis", tokens[1], self.property_size, 1)

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

    def main_loop_screen(self, number_players: int):
        players = self.initialize_players(number_players)
        dice_img = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", "dice.png")),
                                                (50, 50))
        dice_button = ImageButton(((self.screen.get_width() / 1.75), (self.screen.get_height() / 1.20)), dice_img)
        dice_surfaces = [
            pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", f"dice_{index}.png")),
                                         (50, 50)) for index in range(1, 7)]
        font = pygame.font.Font(os.path.join("assets", "images", "Minecraft.ttf"), 35)
>>>>>>> Stashed changes
        run = True
        clock = pygame.time.Clock()
        current_player_index = 0

        while run:
            mouse_pos = pygame.mouse.get_pos()

            dice_button.update(self.screen)

<<<<<<< Updated upstream
            for button in player_info_buttons:
                button.change_color(mouse_pos)
                button.update(self.screen)

            turn_text = text_font.render(f"{players[current_player_index]._name}'s Turn, Roll Those Dice!", True, hex_to_rgb("#000000"))
            turn_text_rect = turn_text.get_rect(center=(self.screen.get_width() / 1.35, self.screen.get_height()/3.5))
=======
            display_surface = pygame.Surface(size=(self.screen.get_width() / 2.25, self.screen.get_height() / 1.75))
            display_surface_rect = display_surface.get_rect(
                center=(self.screen.get_width() / 1.35, self.screen.get_height() / 2))

            turn_text = font.render(f"{players[current_player_index]._name}'s Turn, Roll Those Dice!", True,
                                    hex_to_rgb("#000000"))
            turn_text_rect = turn_text.get_rect(center=(self.screen.get_width() / 1.35, self.screen.get_height() / 3.5))
>>>>>>> Stashed changes
            self.screen.blit(turn_text, turn_text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
<<<<<<< Updated upstream
                    if event.button == 1:
                        if dice_button.check_clicked(mouse_pos):
                            dice_rolls = self.gameboard.roll_dice()
                            player_position = players[current_player_index].move(sum(dice_rolls))
                            self.render_player_move(players,players[current_player_index] ,dice_rolls[0] + dice_rolls[1])
                            for index, roll in enumerate(dice_rolls):
                                self.screen.blit(dice_surfaces[roll - 1], (self.screen.get_width() / (1.65 - index * 0.12), self.screen.get_height() / 1.25))
                            self.display_action(players[current_player_index], player_position)
                            current_player_index = (current_player_index + 1) % len(players)
                        for index,button in enumerate(player_info_buttons):
                            if button.check_clicked(mouse_pos):
                                print(f"clicked on{players[index].name}")
                                display_player_info(player= players[index])
                    
=======
                    if event.button == 1 and dice_button.checkForInput(mouse_pos):
                        self.screen.fill((255, 255, 255), display_surface_rect)
                        dice_rolls = self.gameboard.roll_dice()
                        player_position = players[current_player_index].move(sum(dice_rolls))
                        self.render_player_move(players, players[current_player_index], dice_rolls[0] + dice_rolls[1])
                        for index, roll in enumerate(dice_rolls):
                            self.screen.blit(dice_surfaces[roll - 1], (
                            self.screen.get_width() / (1.65 - index * 0.12), self.screen.get_height() / 1.25))
                        self.display_action(players[current_player_index], player_position)
                        current_player_index = (current_player_index + 1) % len(players)
>>>>>>> Stashed changes

            pygame.display.update()
            clock.tick(FPS)

        pygame.quit()
        quit()

    def display_action(self, player: Player, square_index):
        current_space = self.gameboard._board[square_index]
<<<<<<< Updated upstream
        if isinstance(current_space,Property):
            _display_property_action(self.screen,current_space,player)
        elif isinstance(current_space,Square):
            _display_square_action(self.screen,current_space,player)
=======
        if isinstance(current_space, Property):
            if current_space.square_type == "property":
                _display_property_action(self.screen, current_space, player)
            else:
                print("this is utility")
        elif isinstance(current_space, Square):
            _display_square_action(self.screen, current_space, player)
>>>>>>> Stashed changes

        return

<<<<<<< Updated upstream
def _display_property_action(screen:pygame.Surface,property_object:Property,player:Player):
    font = pygame.font.Font(os.path.join("assets","images", "Minecraft.ttf"), 30)
=======

def _display_property_action(screen: pygame.Surface, property_object: Property, player: Player):
    font = pygame.font.Font(os.path.join("assets", "images", "Minecraft.ttf"), 30)
>>>>>>> Stashed changes
    clock = pygame.time.Clock()
    run = True
    while run:
        if not property_object.is_owned():
            action = [(f"Would you like to buy"),
<<<<<<< Updated upstream
                       (f"{property_object.name}"),
                        (f"for ${property_object.price}?")]
            action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
            action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
            for surface,rect in zip(action_text, action_text_rect):
                screen.blit(surface,rect)
                
            yes_button  = Button((screen.get_width()/1.25-150,screen.get_height()/2),"YES", font, "#000000", "#00ff00")
            no_button = Button((screen.get_width()/1.25,screen.get_height()/2), "NO", font, "#000000", "#ff0000")
=======
                      (f"{property_object.name}"),
                      (f"for ${property_object.price}?")]
            action_text = [font.render(action[0], False, hex_to_rgb("#000000")),
                           font.render(action[1], False, hex_to_rgb("#000000")),
                           font.render(action[2], False, hex_to_rgb("#000000")), ]
            action_text_rect = [action_text[0].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.75)),
                                action_text[1].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.50)),
                                action_text[2].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.25))]
            for surface, rect in zip(action_text, action_text_rect):
                screen.blit(surface, rect)

            yes_button = Button((screen.get_width() / 1.25 - 150, screen.get_height() / 2), "YES", font, "#000000",
                                "#00ff00")
            no_button = Button((screen.get_width() / 1.25, screen.get_height() / 2), "NO", font, "#000000", "#ff0000")
>>>>>>> Stashed changes
            mouse_pos = pygame.mouse.get_pos()

            for button in [yes_button, no_button]:
                button.change_color(mouse_pos)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button.check_clicked(mouse_pos):
                        if player.balance >= property_object.price:
                            property_object.action(player)
                            player.add_property(property_object)
                            action = [(f"Player {player.name} bought"),
                                      (f"{property_object.name} for ${property_object.price}!"),
                                      (f"New Balance ${player.balance}")]
                            for inx, rect in enumerate(action_text_rect):
                                screen.fill((255, 255, 255), action_text_rect[inx])
<<<<<<< Updated upstream
                            action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
                            action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
                            for surface,rect in zip(action_text, action_text_rect):
                                screen.blit(surface,rect)
=======
                            action_text = [font.render(action[0], True, hex_to_rgb("#000000")),
                                           font.render(action[1], True, hex_to_rgb("#000000")),
                                           font.render(action[2], True, hex_to_rgb("#000000")), ]
                            action_text_rect = [
                                action_text[0].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.75)),
                                action_text[1].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.50)),
                                action_text[2].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.25))]
                            for surface, rect in zip(action_text, action_text_rect):
                                screen.blit(surface, rect)
>>>>>>> Stashed changes
                            return
                        else:
                            action = [(f"Unable to buy{property_object.name} for ${property_object.price}"),
                                      (f"Not Enough Funds, Player Balance ${player.balance}")]
                            for inx, rect in enumerate(action_text_rect):
                                screen.fill((255, 255, 255), action_text_rect[inx])
<<<<<<< Updated upstream
                            action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
                            action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
                            for surface,rect in zip(action_text, action_text_rect):
                                screen.blit(surface,rect)
=======
                            action_text = [font.render(action[0], True, hex_to_rgb("#000000")),
                                           font.render(action[1], True, hex_to_rgb("#000000"))]
                            action_text_rect = [
                                action_text[0].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.75)),
                                action_text[1].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.50))]
                            for surface, rect in zip(action_text, action_text_rect):
                                screen.blit(surface, rect)
>>>>>>> Stashed changes
                            return
                    elif no_button.check_clicked(mouse_pos):
                        print("no")
                        return
        elif property_object.owner is not player:
            property_object.action(player)
            action = [(f"Player {property_object.owner_name}"),
<<<<<<< Updated upstream
                       (f"owns {property_object.name},"),
                      (f"pay ${property_object.calculate_rent(player)}"),
                      (f"{player.name}'s new Balance ${player.balance}")]
            action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
            action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
            for surface,rect in zip(action_text, action_text_rect):
                screen.blit(surface,rect)
=======
                      (f"owns {property_object.name},"),
                      (f"pay ${property_object._rent_values}"),
                      (f"{player.name}'s new Balance ${player.balance}")]
            action_text = [font.render(action[0], True, hex_to_rgb("#000000")),
                           font.render(action[1], True, hex_to_rgb("#000000")),
                           font.render(action[2], True, hex_to_rgb("#000000")),
                           font.render(action[3], True, hex_to_rgb("#000000")), ]
            action_text_rect = [action_text[0].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.75)),
                                action_text[1].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.50)),
                                action_text[2].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.25)),
                                action_text[3].get_rect(
                                    center=(screen.get_width() / 1.35, screen.get_height() / 2.00)), ]
            for surface, rect in zip(action_text, action_text_rect):
                screen.blit(surface, rect)
>>>>>>> Stashed changes
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            return
        else:
            action = (f"You own {property_object.name}")
            action_text = font.render(action, True, hex_to_rgb("#000000"))
            action_text_rect = action_text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2))
            screen.blit(action_text, action_text_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            return
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


def _display_square_action(screen: pygame.Surface, square_object: Square, player: Player):
    font = pygame.font.Font(os.path.join("assets", "images", "Minecraft.ttf"), 30)
    clock = pygame.time.Clock()
    run = True
    while run:
        if square_object.square_type == "corner":
            if square_object.name == "Go":
                action = (f"Landed on {square_object.name}, collect $200")
            else:
                action = (f"Landed on Free Parking")
            action_text = font.render(action, True, hex_to_rgb("#000000"))
            action_text_rect = action_text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2))
            screen.blit(action_text, action_text_rect)
            square_object.action(player)
            return
        elif square_object.square_type == "jail":
            action = (f"Landed on Jail, Just Visiting")
            action_text = font.render(action, True, hex_to_rgb("#000000"))
            action_text_rect = action_text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2))
            screen.blit(action_text, action_text_rect)
            square_object.action(player)
            return
        elif square_object.square_type == "go_to_jail":
            action = (f"GO TO JAIL!")
            action_text = font.render(action, True, hex_to_rgb("#000000"))
            action_text_rect = action_text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2))
            screen.blit(action_text, action_text_rect)
            square_object.action(player)
            return
        elif square_object.square_type == "tax":
            action = [(f"Oh no! Landed on {square_object.name}!"),
                      (f"Pay 10% of Balance = {int(player.balance * 0.1)}"),
                      (f"New Balance = {player.balance - int(player.balance * 0.1)}")]
            square_object.action(player)
<<<<<<< Updated upstream
            action_text = [font.render(line, True, hex_to_rgb("#000000")) for line in action]
            action_text_rect = [text.get_rect(center=(screen.get_width() / 1.35, screen.get_height() / (3 - i * 0.25))) for i, text in enumerate(action_text)]
            for surface,rect in zip(action_text, action_text_rect):
                screen.blit(surface,rect)
=======
            action_text = [font.render(action[0], True, hex_to_rgb("#000000")),
                           font.render(action[1], True, hex_to_rgb("#000000")),
                           font.render(action[2], True, hex_to_rgb("#000000"))]
            action_text_rect = [action_text[0].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.75)),
                                action_text[1].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.50)),
                                action_text[2].get_rect(center=(screen.get_width() / 1.35, screen.get_height() / 2.25))]
            for surface, rect in zip(action_text, action_text_rect):
                screen.blit(surface, rect)
>>>>>>> Stashed changes
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