# Property
# Simulates a property that is on the board, allowing for the management of property ownership, calculating rent, and handling property development.

from Game_Engine.Square import Square
from Game_Engine.Player import Player


class Property(Square):
    """Represents a property square on the Monopoly board."""

    def __init__(self, name: str, color: str, price: int, rent_values: list[int]):
        """
        Initializes a Property object with the specified attributes.

        Args:
            name: The name of the property.
            color: The color of the property represented as a Hex value.
            price: The initial purchase value.
            rent_values: List of rent values in ascending order.
        """
        Square.__init__(self, name, color)
        self._price = price
        self._rent_values = rent_values
        self._num_houses = 0
        self._owner = None

    def action(self, player: Player) -> None:
        """
        Allows the player to purchase the property or pay rent.

        If the property has no owner, then the player will be prompted with the
        choice to purchase the property if their balance is sufficient. If so,
        then their balance will be subtracted by the property's price and
        ownership is updated. If the property is already owned by someone else
        besides the current player, then rent is calculated and paid.

        Args:
            player: The player that has landed on the property.
        """
        if self._owner is None:
            if player.balance >= self._price:
                # TODO Prompt user to choose whether they want to purchase
                player.balance -= self._price
                self._owner = player
        elif self._owner is not player:
            rent = self._calculate_rent()
            player.pay_rent(self._owner, rent)

    def build_house(self) -> None:
        """
        Builds a house on the property.

        Allows the player to build a house so that rent my be increased. To do
        so, the player must own all the properties on the color set.
        """
        pass

    def _calculate_rent(self) -> int:
        """
        Determines how much the property's rent costs.

        The price of rent is determined by how many houses have been built on
        the property. If the owner has built multiple houses, then rent should
        be increased.

        Returns:
            The price of rent adjusted by the number of houses.
        """
        return self._rent_values[self._num_houses]


# Update Property Ownership
# Handles the transfer of property ownership by switching the owner to a different player.
# Pre-Condition: \@requires player is not None
#  Post-Condition: \@ensures self.owner == player
# Method Signature: def update_ownership(self, player: Player) -> None:

# Calculate Rent
# Determines the amount of rent to be paid by a player who lands on the property.
# Pre-Condition: \@requires self.owner is not None
# Post-Condition: \@ensures \result == self.rent + (self.price_per_house * self.num_houses)
# Method Signature: def calculate_rent(self) -> int:
