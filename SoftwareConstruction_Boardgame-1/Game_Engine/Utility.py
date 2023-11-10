from Game_Engine.Square import Square
from Game_Engine.Player import Player


class Utility(Square):
    """Represents a utility square on the Monopoly board."""

    def __init__(self, name: str, price: int) -> None:
        Square.__init__(self, name)
        self._price = price
        self._owner = None

    def action(self, player: Player) -> None:
        """
        Allows the player to purchase the utility or pay rent.

        If the utility has no owner, then the player will be prompted with the
        choice to purchase the utility if their balance is sufficient. If so,
        then their balance will be subtracted by the utility's price and
        ownership is updated. If the utility is already owned by someone else
        besides the current player, then rent is calculated and paid.

        Args:
            player: The player that has landed on the utility.
        """
        if self._owner is None:
            if player.balance >= self._price:
                player.balance -= self._price
                self._owner = player
        elif self._owner is not player:
            rent = self._calculate_rent(player.last_roll)
            player.pay_rent(self._owner, rent)

    def _calculate_rent(self, dice_roll: int) -> int:
        """
        Determines how much the utility's rent costs.

        The price of rent is calculated by the total of the dice the player
        rolled multipled by 4 if the user owns one utility, or ten if they own
        both.

        Returns:
            The price of rent.
        """
        # TODO Multiply dice_roll by 10 if the player owns both utility squares
        return 4 * dice_roll
