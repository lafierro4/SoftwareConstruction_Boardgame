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
            
    def dice_is_being_rolled(self, players: list[Player], current_player_index:int):
        random.seed()
        dice_rolls =(random.randint(1, 6), random.randint(1, 6))
        dice_surfaces = [pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "images", f"dice_{index}.png")), (50, 50)) for index in range(1, 7)]
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
        return (players[current_player_index], players[current_player_index].position)


    @property
    def board(self):
        return self._board