# Property
# Simulates a property that is on the board, allowing for the management of property ownership, calculating rent, and handling property development.

from Game_Engine.Square import Square
from Game_Engine.Player import Player


class Property(Square):
    """
    Represents a property in a game.

    Attributes:
        name (str): The name of the Property.
        color (str): The color of the Property, in Hex Code.
        purchase_value (int): The purchase value of the Property.
        rent_values (list of int): List of rent values for the Property.
        is_owned (bool): True if the Property is owned, False otherwise.
        owner: The player who owns the Property (if it is owned).
    """

    def __init__(self, name: str, color: str, price: int, rent_values: list[int]):
        """
        Initializes a Property object with the specified attributes.

        Args:
            name (str): The name of the Property.
            color (str): The color of the Property, in Hex Code.
            price (int): The initial purchase value of the Property.
            rent_values (list of int): List of rent values for the Property.
        """
        Square.__init__(self, name, color)
        self._price = price
        self.rent_values = rent_values
        self._owner = None

    def action(self, player: Player) -> None:
        if self._owner is None:
            decision = input(
                f"Player {player._name} at position {player.position} buy Property {self._name}? "
            )
            if player.balance >= self._price and decision == "yes":
                player.balance -= self._price
                self._owner = player
        elif self._owner is not player:
            rent = self._calculate_rent()
            print(
                f"Player {player._name} at position {player.position} paying {rent} for {self._name}"
            )
            player.pay_rent(self._owner, rent)

    def _calculate_rent(self) -> int:
        return self.rent_values[0]


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
