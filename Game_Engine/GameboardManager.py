# This is the first file
# Represent the Monopoly game board with properties, squares, and rules.
from Game_Engine.Property import Property
from Game_Engine.Dice import Dice
from Game_Engine.Player import Player
from Game_Engine.Square import Square
from Game_Engine.Tax import Tax
from Game_Engine.Utility import Utility

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
        self._dice = Dice()
        self._players = []
        self._board = [
            Square("Go"),
            Property("Mediterranean Meals", "#a37759", 60, [2, 10, 30, 90, 160, 250]),
            Square("Community Chest"),
            Property("Baltic Breezeway", "#a37759", 60, [4, 20, 60, 180, 320, 450]),
            Tax("Income Tax"),
            Property("Skipping Railroad", "#000000", 200, [25, 50, 100, 200]),
            Property("Oriental Oasis", "#e8a541", 100, [6, 30, 90, 270, 400, 550]),
            Square("Chance"),
            Property("Vermont Vacation", "#e8a541", 100, [6, 30, 90, 270, 400, 550]),
            Property(
                "Connecticut Courtyard", "#e8a541", 120, [8, 40, 100, 300, 450, 600]
            ),
            Square("Jail"),
            Property(
                "Sir Charles' Sanctuary", "#a14685", 140, [10, 50, 150, 450, 625, 750]
            ),
            Utility("Electric Company"),
            Property("United Estates", "#a14685", 140, [10, 50, 150, 450, 625, 750]),
            Property(
                "Virginia Vineyards", "#a14685", 160, [12, 60, 180, 500, 700, 900]
            ),
            Property("Quarter Railroad", "#000000", 200, [25, 50, 100, 200]),
            Property(
                "Saintly James' Square", "#ef756d", 180, [14, 70, 200, 550, 750, 950]
            ),
            Square("Community Chest"),
            Property("Tunessee Avenue", "#ef756d", 180, [14, 70, 200, 550, 750, 950]),
            Property("Big Apple Avenue", "#ef756d", 200, [16, 80, 220, 600, 800, 1000]),
            Square("Free Parking"),
            Property(
                "Kentucky Fried Avenue", "#ca6e47", 220, [18, 90, 250, 700, 875, 1050]
            ),
            Square("Chance"),
            Property("Indy Car Avenue", "#ca6e47", 220, [18, 90, 250, 700, 875, 1050]),
            Property("Illusion Avenue", "#ca6e47", 240, [20, 100, 300, 750, 925, 1100]),
            Property("R. R. Railroad", "#000000", 200, [25, 50, 100, 200]),
            Property(
                "Atlantic Adventure", "#2277a2", 260, [22, 110, 330, 800, 975, 1150]
            ),
            Property(
                "Ventilation Avenue", "#2277a2", 260, [22, 110, 330, 800, 975, 1150]
            ),
            Utility("Water Works"),
            Property(
                "Marvin's Magic Meadow", "#2277a2", 280, [24, 120, 360, 850, 1025, 1200]
            ),
            Square("Go To Jail"),
            Property(
                "Pacific Playground", "#55a95d", 300, [26, 130, 390, 900, 1100, 1275]
            ),
            Property(
                "Northern Charm Avenue", "#55a95d", 300, [26, 130, 390, 900, 1100, 1275]
            ),
            Square("Community Chest"),
            Property(
                "Penny-sylvania Avenue",
                "#55a95d",
                320,
                [28, 150, 450, 1000, 1200, 1400],
            ),
            Property("Longline Railroad", "#000000", 200, [25, 50, 100, 200]),
            Square("Chance"),
            Property("Parking Place", "#e34537", 350, [35, 175, 500, 1100, 1300, 1500]),
            Tax("Luxury Tax"),
            Property("Bored Walk", "#e34537", 400, [50, 200, 600, 1400, 1700, 2000]),
        ]

    # region Contracts

    def play_game(self) -> None:
        """Simulates the main game loop."""
        while len(self._players) > 1:
            for player in self._players:
                self._play_turn(player)
                if player.is_bankrupt():
                    self._players.remove(player)
        print("Player wins!")

    def add_player(self, player: Player) -> None:
        """Adds a player to the gameboard.

        Args:
            player: Something else
        """
        self._players.append(player)

    # endregion

    def _play_turn(self, player: Player) -> None:
        """Handles the current player's turn.

        Args:
            player: The current player.
        """
        roll1 = self._dice.roll()
        roll2 = self._dice.roll()

        player.move(roll1 + roll2)
        self.properties[player.position].action(player)


# Handle Turn Base Action
# Responsible for coordinating player actions during their turns by controlling the sequence of player turns and game events.
# Pre-Condition: \@require self.game_running == True
# Post-Condition: \@ensures self.current_player_index == \old(self.current_player_index) + 1
# Method Signature: def handle_turn(self) -> None:
