# Bank
#  Manages the game’s finances, tracking money, and facilitating transactions between players. It ensures fair play by handling income and expenses accordingly.

# class Bank

# Process Property Purchase 
# Handles the financial aspects of a player purchasing a property by ensuring the player has sufficient funds before finalizing the transaction. 
# Pre-Condition: @requires property.owner == None and player.funds >= property.price 
# Post-Condition: @ensures player.funds == \old(player.funds) - property.price 
# Method signature: def purchase_property(self, player: Player, property: Property) -> None: 

# Collect Rent 
# Managed the transfer of rent payments from players to the bank or to the property owner. 
# Pre-Condition: @requires player is not None and property is not None 
# Post-Condition: @ensures player.funds == \old(player.funds) - property.calculate_rent() 
# Method signature: def collect_rent(self, player: Player, property: Property) -> None: 

# Manage Trade
# Facilitate the negotiation and execution of property trades between players. 
# Pre-Condition: @requires property.owner == trader and tradee.funds >= property.offer_price 
# Post-Condition: @ensures property.owner == trade and tradee.funds == \old(tradee.funds) – property.offer_price and trader.funds == \old(trader.funds) + property.offer_price 
# Method signature: def manage_trade(self, trader: Player, tradee: Player, property: Property) -> None: 

# Handle Bankruptcy 
# Manage the transfer of rent payments from players to the bank or property owner. 
# Pre-Condition: @requires player is not None 
# Post-Condition: @ensures (\forall property in \old(player.properties): property.owner != player) 
# Method signature: def handle_bankruptcy (self, player: Player) -> None: 

from Game_Engine.Player import Player
from Game_Engine.Property import Property

class Bank:
    def purchase_property(self, player: Player, property: Property) -> None:
        if player.balance >= property.price:
            player.decrease_funds(property.price)
    

    def collect_rent(self, player: Player, property: Property) -> None:
        if player is not None & property is not None:
            player.decrease_funds(property.calculate_rent())