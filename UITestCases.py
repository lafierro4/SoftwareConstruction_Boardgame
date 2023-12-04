"""This module contains all of the necessary PyGame components for
running a simplified game loop.
Use it for test cases on PyGame-related code.
"""
import sys, os
import pygame
from User_Interface import GameboardView
from User_Interface import util
from User_Interface.Game import Cloneopoly
from Game_Engine.Property import Property
from Game_Engine.Player import Player
from pygame.locals import *
# Import additional modules here.


# Feel free to edit these constants to suit your requirements.
FRAME_RATE = 60.0
SCREEN_SIZE = (1280, 720)


def pygame_modules_have_loaded():
    success = True

    if not pygame.display.get_init:
        success = False
    if not pygame.font.get_init():
        success = False
    if not pygame.mixer.get_init():
        success = False

    return success

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.font.init()

if pygame_modules_have_loaded():
    pygame.display.set_caption('Test')
    clock = pygame.time.Clock()

    def declare_globals():
        global space_size, game_screen, space_size, tokens, player, player_two, gameboard, players, game, player_property
        game_screen = pygame.display.set_mode(SCREEN_SIZE)
        space_size = game_screen.get_width() / 25.6
        tokens = util.token_image_surface(space_size/1.4)
        player = Player("Tester1",tokens[0],space_size)
        player_two = Player("Tester2",tokens[0],space_size)
        gameboard = GameboardView.GameboardView(game_screen)
        players = [player, player_two]
        game = Cloneopoly(True)
        game.gameboard = gameboard
        game.remaining_players = 2
        font = pygame.font.Font(os.path.join("assets", "images", "Minecraft.ttf"), 30)
        button = util.Button((game.gameboard.screen.get_width() / 1.25, game.gameboard.screen.get_height() / 2), "NO", font,"#ff0000", "#ff0000")
        player.button = button
        game.player_buttons.append(button)
        player_property = Property("Mediterranean Meals", "property", "#a37759", 60, [2, 10, 30, 90, 160, 250], 50)
        # The class(es) that will be tested should be declared and initialized
        # here with the global keyword.
        # Yes, globals are evil, but for a confined test script they will make
        # everything much easier. This way, you can access the class(es) from
        # all three of the methods provided below.
        pass

    def prepare_test():
        game_screen.fill("white")
        gameboard.setup_board()
        
        player.set_position(space_size * 11, space_size * 11)
        game_screen.blit(tokens[0], (player._position_x, player._position_y))
        pygame.display.update()
        # Add in any code that needs to be run before the game loop starts.
        pass

    def handle_input(testNumber):
        if testNumber == 1:
            player.move(5)
            gameboard.render_player_move(players, player, 5)
            assert(player._position == 5)
        if testNumber == 2:
            player.move(30)
            gameboard.render_player_move(players, player, 30)
            game.display_action(player,player._position)
            pygame.time.wait(2000)
            if player._in_jail == True:
                gameboard.render_player_move(players, player, 10)
            assert(player._in_jail == True)
            assert(player._balance == 1500)
        if testNumber == 3:
            assert(game.remaining_players == 2)
            print("Remaining players: ", game.remaining_players)
            player._assets = []
            player._balance = 0
            game.handle_bankrupt(player)
            assert(len(player._assets) == 0)
            assert(game.remaining_players == 1)
            print("Remaining players: ", game.remaining_players)
            game.victory_screen(player_two.name)
        # Add in code for input handling.
        # key_name provides the String name of the key that was pressed.
        pass

    def update(screen, time):
        # Add in code to be run during each update cycle.
        # screen provides the PyGame Surface for the game window.
        # time provides the seconds elapsed since the last update.
        pygame.display.update()

    # Add additional methods here.

    def main():
        declare_globals()
        prepare_test()
        testNumber = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    declare_globals()
                    prepare_test()
                    testNumber += 1
                    handle_input(testNumber)

            milliseconds = clock.tick(FRAME_RATE)
            seconds = milliseconds / 1000.0
            update(game_screen, seconds)

            sleep_time = (1000.0 / FRAME_RATE) - milliseconds
            if sleep_time > 0.0:
                pygame.time.wait(int(sleep_time))
            else:
                pygame.time.wait(1)

    main()