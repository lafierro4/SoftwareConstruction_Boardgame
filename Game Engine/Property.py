# Property
# Simulates a property that is on the board, allowing for the management of property ownership, calculating rent, and handling property development.

# class Property
    # name
    # color
    # purchase value
    # rent values

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