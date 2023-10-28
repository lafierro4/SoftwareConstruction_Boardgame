#This is the first file
# Represent the Monopoly game board with properties, squares, and rules.

# def class Gameboard

#  Initialize Gameboard
# Declares all the rules for the game, initializes all the board tiles, and sets up the properties so a game of Cloneopoly may be played. 
# Pre-Condition: \@require len(self.players) > 1 
#  Post-Condition: \@ensures len(self.properties) > 40 and self.dice.seed is not None and (\forall player in self.players: player.position == 0) 
#  Method Signature: def initialize(self) -> None: 


# Handle Turn Base Action
# Responsible for coordinating player actions during their turns by controlling the sequence of player turns and game events. 
# Pre-Condition: \@require self.game_running == True 
# Post-Condition: \@ensures self.current_player_index == \old(self.current_player_index) + 1 
# Method Signature: def handle_turn(self) -> None: 
