# Property
# Simulates a property that is on the board, allowing for the management of property ownership, calculating rent, and handling property development.
import typing

class Property:
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
    def __init__(self, name:str,color:str,purchase_value:int, rent_values: list[int]):
        """
        Initializes a Property object with the specified attributes.

        Args:
            name (str): The name of the Property.
            color (str): The color of the Property, in Hex Code.
            purchase_value (int): The initial purchase value of the Property.
            rent_values (list of int): List of rent values for the Property.
        """
        self.name = name
        self.color = color
        self.purchase_value = purchase_value
        self.rent_values = rent_values
        #Ownership Attributes , is_owned: checks if a Player owns the Property, owned_by: If a Player owns a Property, their name will be set to this.
        is_owned = False
        owned_by = None

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