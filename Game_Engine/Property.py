from typing import Optional, List
from Game_Engine.BoardSpace import BoardSpace
from Game_Engine.Player import Player


class Property(BoardSpace):
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

    def __init__(self, name: str, property_type: str, color: str, price: int, rent_values: List[int] = [], house_price: int= 0):
        """
        Initializes a Property object with the specified attributes.

        Args:
            name: The name of the property.
            color: The color of the property represented as a Hex value.
            price: The initial purchase value.
            rent_values: List of rent values in ascending order.
        """
        BoardSpace.__init__(self, name, property_type, color)
        self._price = price
        self._owner:Optional[Player] = None

        if self.space_type == "property":
            self._rent_values = rent_values
            self._num_houses = 0
            self._house_price = house_price
        
    def reset(self):
        self._owner = None
        if self.space_type == "property":
            self._num_houses = 0

    def is_owned(self) -> bool:
        return self._owner is not None

    def action(self, player: Player) -> bool:
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
            return True
        elif self._owner is not player:
            rent = self.calculate_rent(player)
            return player.transfer_money(self._owner, rent)
        return True

    def build_house(self):
        if self.owner != None:
            if self.space_type == "property":
                if self.owner.balance > self._house_price:
                    if self.num_houses <= 4:
                        self.owner.decrease_balance(self._house_price) 
                        self._num_houses += 1
                        return (f"Successfully Bought a House for ${self.house_price}\nCurrent Number of Houses: {self.num_houses}")
                    else:
                        return f"Maximum Houses Purchased for {self.name}"
                else:
                    return (f"Insufficent funds to purchase house, House Price: ${self.house_price}")   
            else:
                return f"{self.name} is Not a Property\nUnable to Purchase Houses"
        else:
            return "Error Self Building Houses"




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
        if self.space_type == "property":
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
    def num_houses(self):
        return self._num_houses
    @property
    def current_rent(self):
        return self._rent_values[self._num_houses]
    
    @property
    def house_price(self):
        if self.space_type == "property":
            return self._num_houses
    
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
