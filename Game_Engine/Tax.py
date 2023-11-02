from Game_Engine.Square import Square
from Game_Engine.Player import Player


class Tax(Square):
    """Represents a tax square on the Monopoly board."""

    def __init__(self, name: str) -> None:
        Square.__init__(self, name)

    def action(self, player: Player) -> None:
        if player.balance < 200:
            pass
