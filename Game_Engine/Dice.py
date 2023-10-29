# Dice
# Simulates dice rolls, providing random numbers for player movement. It’s crucial for determining how far players move on the board.

# class Dice

#  Generate Random Seed 
# Generates a unique seed used for producing random numbers. 
#  Pre-Condition: \@requires self.seed is not None 
#   Post-Condition: \@ensures self.seed == random.seed() 
#  Method signature: def generate_seed(self) -> None: 

# Roll Dice 
# Simulates rolling dice and returns the result as a random number between 1 and the number of sides on a dice (6 in Monopoly). 
# Pre-Condition: \@requires self.seed is not None 
# Post-Condition: \@ensures \result >= 1 and \result <= 6 
# Method signature: def roll_dice(self) -> int: 

