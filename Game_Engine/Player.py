#Player
#Represent individual players in the game, storing their assets, financial status, and property holdings.

# class Player:
    # money, connect to bank
    # list of Properties, connect to Property
    # name
    # token

# Update Player Funds
# Change the amount of money the player has and perform any actions as a result of reaching this new amount. 
# Pre-Condition: \@requires new_amount >= 0 
# Post-Condition: \@ensures self.funds == new_amount 
# Method signature: def update_funds(self, new_amount) -> None: 


# Update Property
# Not in the SDD but we should have a method that updates the property of the player

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.funds = 0
        self.properties = []

    def increase_funds(self, amount):
        if amount >= 0:
            self.funds += amount
        else:
            exit
    
    def decrease_funds(self, amount):
        if amount >= 0:
            self.funds -= amount
        else:
            exit
    def update_property(self, property_obj):
        self.properties.append(property_obj)