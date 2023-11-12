# This is the first file
# Represent the Monopoly game board with properties, squares, and rules.
import random, time
from Game_Engine.Property import Property
from Game_Engine.Player import Player
from Game_Engine.Space import Space
from Game_Engine.Square import Square

#  Initialize Gameboard
# Declares all the rules for the game, initializes all the board tiles, and sets up the properties so a game of Cloneopoly may be played.
# Pre-Condition: \@require len(self.players) > 1
#  Post-Condition: \@ensures len(self.properties) > 40 and self.dice.seed is not None and (\forall player in self.players: player.position == 0)
#  Method Signature: def initialize(self) -> None:


class Gameboard:
    """
    Sets up the board's intial rules and settings

    Attributes:
        properties: list of Properties with their default settings
    """

    def __init__(self) -> None:
        self._players: list[Player] = []
        self._board: list[Space] = [
            Square("Go", "corner"),
            Property("Mediterranean Meals", "property", "#a37759", 60, [2, 10, 30, 90, 160, 250]),
            Square("Lice Tax", "tax"),
            Property("Baltic Breezeway", "property", "#a37759", 60, [4, 20, 60, 180, 320, 450]),
            Square("Income Tax", "tax"),
            Property("Skipping Railroad", "property", "#000000", 200, [25, 50, 100, 200]),
            Property("Oriental Oasis", "property", "#e8a541", 100, [6, 30, 90, 270, 400, 550]),
            Square("Apple Tax", "tax"),
            Property("Vermont Vacation", "property", "#e8a541", 100, [6, 30, 90, 270, 400, 550]),
            Property("Connecticut Courtyard", "property", "#e8a541", 120, [8, 40, 100, 300, 450, 600]),
            Square("Jail", "jail"),
            Property("Sir Charles' Sanctuary", "property", "#a14685", 140, [10, 50, 150, 450, 625, 750]),
            Property("Electric Company", "utility", "#a37759", 150),
            Property("United Estates", "property", "#a14685", 140, [10, 50, 150, 450, 625, 750]),
            Property("Virginia Vineyards", "property", "#a14685", 160, [12, 60, 180, 500, 700, 900]),
            Property("Quarter Railroad", "property", "#000000", 200, [25, 50, 100, 200]),
            Property("Saintly James' Square", "property", "#ef756d", 180, [14, 70, 200, 550, 750, 950]),
            Square("Charity Tax", "tax"),
            Property("Tunessee Avenue", "property", "#ef756d", 180, [14, 70, 200, 550, 750, 950]),
            Property("Big Apple Avenue", "property", "#ef756d", 200, [16, 80, 220, 600, 800, 1000]),
            Square("Free Parking", "corner"),
            Property("Kentucky Fried Avenue", "property", "#ca6e47", 220, [18, 90, 250, 700, 875, 1050]),
            Square("Bad Hair Tax", "tax"),
            Property("Indy Car Avenue", "property", "#ca6e47", 220, [18, 90, 250, 700, 875, 1050]),
            Property("Illusion Avenue", "property", "#ca6e47", 240, [20, 100, 300, 750, 925, 1100]),
            Property("R. R. Railroad", "property", "#000000", 200, [25, 50, 100, 200]),
            Property("Atlantic Adventure", "property", "#2277a2", 260, [22, 110, 330, 800, 975, 1150]),
            Property("Ventilation Avenue", "property", "#2277a2", 260, [22, 110, 330, 800, 975, 1150]),
            Property("Water Works", "utility", "#a37759", 150),
            Property("Marvin's Magic Meadow", "property", "#2277a2", 280, [24, 120, 360, 850, 1025, 1200]),
            Square("Go To Jail", "go_to_jail"),
            Property("Pacific Playground", "property", "#55a95d", 300, [26, 130, 390, 900, 1100, 1275]),
            Property("Northern Charm Avenue", "property", "#55a95d", 300, [26, 130, 390, 900, 1100, 1275]),
            Square("Juice Tax", "tax"),
            Property("Penny-sylvania Avenue", "property", "#55a95d", 320, [28, 150, 450, 1000, 1200, 1400]),
            Property("Longline Railroad", "property", "#000000", 200, [25, 50, 100, 200]),
            Square("Candy Tax", "tax"),
            Property("Parking Place", "property", "#e34537", 350, [35, 175, 500, 1100, 1300, 1500]),
            Square("Luxury Tax", "tax"),
            Property("Bored Walk", "property", "#e34537", 400, [50, 200, 600, 1400, 1700, 2000]),
        ]
    #REVIEW IF THIS IS NEEDED - LF
    def add_player(self, player: Player) -> None:
        """
        Adds a player to the gameboard.

        Args:
            player: Something else
        """
        self._players.append(player)

    def roll_dice(self) -> tuple[int, int]:
        """
        Simulates rolling dice and returns the result as a random number
        between 1 and the number of sides on a dice (6 in Monopoly).
        """
        random.seed()
        return (random.randint(1, 6), random.randint(1, 6))

# Handle Turn Base Action
# Responsible for coordinating player actions during their turns by controlling the sequence of player turns and game events.
# Pre-Condition: \@require self.game_running == True
# Post-Condition: \@ensures self.current_player_index == \old(self.current_player_index) + 1
# Method Signature: def handle_turn(self) -> None:

   # Roll Dice 
    #Simulates rolling dice and returns the result as a random number between 1 and the number of sides on a dice (6 in Monopoly). 
    #   Pre-Condition: \@requires self.seed is not None 
    #  Post-Condition: \@ensures \result >= 1 and \result <= 6 
   # Method signature: def roll_dice(self) -> int: 