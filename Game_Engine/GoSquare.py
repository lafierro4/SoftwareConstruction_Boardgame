from Game_Engine.Square import Square
from Game_Engine.Player import Player


class Utility(Square):
    """
    Represents a utility square on the Monopoly board.
    """

    def __init__(self) -> None:
        Square.__init__(self, "Go")

    def action(self, player: Player) -> None:
        pass
