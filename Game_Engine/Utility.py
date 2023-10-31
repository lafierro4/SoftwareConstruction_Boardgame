from Game_Engine.Square import Square
from Game_Engine.Player import Player


class Utility(Square):
    """
    Represents a utility square on the Monopoly board.
    """

    def __init__(self, name: str, price: int) -> None:
        Square.__init__(self, name)
        self._price = price
        self._owner = None

    def action(self, player: Player) -> None:
        if self._owner is None:
            if player.balance >= self._price:
                player.balance -= self._price
                self._owner = player
                player.add_property(self)
        elif self._owner is not player:
            rent = self._calculate_rent(player.last_roll)
            player.pay_rent(self._owner, rent)

    def _calculate_rent(self, dice_roll: int) -> int:
        return 4 * dice_roll
