# This is the first file
# Represent the Monopoly game board with properties, squares, and rules.
import random, time
from Game_Engine.Property import Property
from Game_Engine.Player import Player
from Game_Engine.Space import Space
from Game_Engine.Square import Square
from PIL import Image, PngImagePlugin

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
            Square("Go", "corner", "", "assets/images/GO.png"),
            Property("Mediterranean Avenue", "property", "#a37759", 60, Image.open("assets/images/medAve.png"), [2, 10, 30, 90, 160, 250]),
            Square("Lice Tax", "tax", "", "assets/images/blank.png"),
            Property("Baltic Avenue", "property", "#a37759", 60, Image.open("assets/images/balticAve.png"), [4, 20, 60, 180, 320, 450]),
            Square("Income Tax", "tax","", "assets/images/iTax.png"),
            Property("Reading Railroad", "property", "#000000", 200, Image.open("assets/images/readingRailroad.png"), [25, 50, 100, 200]),
            Property("Oriental Avenue", "property", "#e8a541", 100, Image.open("assets/images/orientalAve.png"), [6, 30, 90, 270, 400, 550]),
            Square("Apple Tax", "tax","","assets/images/blank.png"),
            Property("Vermont Avenue", "property", "#e8a541", 100, Image.open("assets/images/vermontAve.png"), [6, 30, 90, 270, 400, 550]),
            Property("Connecticut Avenue", "property", "#e8a541", 120, Image.open("assets/images/conAve.png"), [8, 40, 100, 300, 450, 600]),
            Square("Jail", "jail","","assets/images/jail.png"),
            Property("ST. Charles Place", "property", "#a14685", 140, Image.open("assets/images/stCharles.png"),[10, 50, 150, 450, 625, 750]),
            Property("Electric Company", "utility", "#a37759", 150, Image.open("assets/images/electricCompany.png")),
            Property("States Avenue", "property", "#a14685", 140, Image.open("assets/images/statesAve.png"), [10, 50, 150, 450, 625, 750]),
            Property("Virginia Avenue", "property", "#a14685", 160, Image.open("assets/images/virginiaAve.png") ,[12, 60, 180, 500, 700, 900]),
            Property("Pennsylvania Railroad", "property", "#000000", 200, Image.open("assets/images/penRailroad.png") ,[25, 50, 100, 200]),
            Property("ST. James Place", "property", "#ef756d", 180, Image.open("assets/images/stJames.png"), [14, 70, 200, 550, 750, 950]),
            Square("Charity Tax", "tax","","assets/images/blank.png"),
            Property("Tennessee Avenue", "property", "#ef756d", 180, Image.open("assets/images/tenAve.png"), [14, 70, 200, 550, 750, 950]),
            Property("New York Avenue", "property", "#ef756d", 200, Image.open("assets/images/nyAve.png"), [16, 80, 220, 600, 800, 1000]),
            Square("Free Parking", "corner","","assets/images/fParking.png"),
            Property("Kentucky Avenue", "property", "#ca6e47", 220, Image.open("assets/images/kenAve.png"), [18, 90, 250, 700, 875, 1050]),
            Square("Bad Hair Tax", "tax","","assets/images/blank.png"),
            Property("Indiana Avenue", "property", "#ca6e47", 220, Image.open("assets/images/indiAve.png"), [18, 90, 250, 700, 875, 1050]),
            Property("Illinois Avenue", "property", "#ca6e47", 240, Image.open("assets/images/illiAve.png"), [20, 100, 300, 750, 925, 1100]),
            Property("B & O Railroad", "property", "#000000", 200, Image.open("assets/images/boRailroad.png"), [25, 50, 100, 200]),
            Property("Atlantic Avenue", "property", "#2277a2", 260, Image.open("assets/images/atlAve.png"), [22, 110, 330, 800, 975, 1150]),
            Property("Veninor Avenue", "property", "#2277a2", 260, Image.open("assets/images/venAve.png"), [22, 110, 330, 800, 975, 1150]),
            Property("Water Works", "utility", "#a37759", 150, Image.open("assets/images/waterWorks.png")),
            Property("Marvin Gardens", "property", "#2277a2", 280, Image.open("assets/images/mGardensAve.png"), [24, 120, 360, 850, 1025, 1200]),
            Square("Go To Jail", "go_to_jail","","assets/images/goToJail.png"),
            Property("Pacific Avenue", "property", "#55a95d", 300, Image.open("assets/images/pacificAve.png"), [26, 130, 390, 900, 1100, 1275]),
            Property("North Carolina Avenue", "property", "#55a95d", 300, Image.open("assets/images/nCarAve.png"), [26, 130, 390, 900, 1100, 1275]),
            Square("Juice Tax", "tax","", "assets/images/blank.png"),
            Property("Pennsylvania Avenue", "property", "#55a95d", 320, Image.open("assets/images/penAve.png"), [28, 150, 450, 1000, 1200, 1400]),
            Property("Short Line Railroad", "property", "#000000", 200, Image.open("assets/images/slRailroad.png"), [25, 50, 100, 200]),
            Square("Candy Tax", "tax", "", "assets/images/blank.png"),
            Property("Park Place", "property", "#e34537", 350, Image.open("assets/images/parkPL.png"), [35, 175, 500, 1100, 1300, 1500]),
            Square("Luxury Tax", "tax", "", "assets/images/luxTax.png"),
            Property("Broadwalk", "property", "#e34537", 400, Image.open("assets/images/broadAve.png"), [50, 200, 600, 1400, 1700, 2000]),
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