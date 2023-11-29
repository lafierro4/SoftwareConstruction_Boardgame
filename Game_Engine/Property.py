from typing import Optional
from Game_Engine.Space import Space
from Game_Engine.Player import Player


class Property(Space):
    """
    Represents a property square on the Monopoly board.

    A Property is a broad classification that encompasses a variety of in-game
    assets, including real estate properties, such as residential houses and
    commercial buildings, as well as public utilities, like electric and water
    companies. These assets constitute the primary investment opportunities for
    players, representing avenues for accumulating wealth, generating rent
    income, and making strategic financial decisions. The class itself serves
    as a blueprint for modeling and managing these dynamic and multifaceted
    components of the game.
    """

    def __init__(self, name: str, property_type: str, color: str, price: int, rent_values: list[int] = []):
        """
        Initializes a Property object with the specified attributes.

        Args:
            name: The name of the property.
            color: The color of the property represented as a Hex value.
            price: The initial purchase value.
            rent_values: List of rent values in ascending order.
        """
        Space.__init__(self, name, property_type, color)
        self._price = price
        self._owner = None
        self._owned = False

        if property_type == "property":
            self._rent_values = rent_values
            self._num_houses = 0
        
    def is_owned(self) -> bool:
        if self._owner is None:
            return False
        else:
            return True

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
        if not self.is_owned():
            self.change_owner(player)
            player.decrease_balance(self.price)
            self._owner = player
        elif self._owner is not player:
            rent = self.calculate_rent(player)
            player.transfer_money(self._owner, rent)

    def build_house(self) -> None:
        """
        Builds a house on the property.

        Allows the player to build a house so that rent my be increased. To do
        so, the player must own all the properties on the color set.
        """
        pass

    def calculate_rent(self, player: Player) -> int:
        """
        Determines how much the property's rent costs.

        For properties, the price of rent is determined by how many houses have
        been built on the property. If the owner has built multiple houses,
        then rent should be increased. For utilities, the price of rent is
        calculated by the total of the dice the player rolled multipled by 4 if
        the user owns one utility, or 10 if they own both.

        Returns:
            The price of rent.
        """
        if self._square_type == "property":
            return self._rent_values[self._num_houses]
        else:
            multiplier = 4 if player.owns_both_utilities() else 10
            return multiplier * player.last_roll
    
    def change_owner(self,player:Player) -> None:
        self._owner = player

    @property
    def price(self) -> int:
        return self._price
    
    @property
    def owner_name(self) -> Optional[str]:
        if self._owner is not None:
            return self._owner.name
        else:
            return None
        
    @property
    def owner(self) -> Optional[Player]:
        if self._owner is not None:
            return self._owner
        else:
            return None



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
