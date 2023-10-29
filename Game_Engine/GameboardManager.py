#This is the first file
# Represent the Monopoly game board with properties, squares, and rules.
import Property

#  Initialize Gameboard
# Declares all the rules for the game, initializes all the board tiles, and sets up the properties so a game of Cloneopoly may be played. 
# Pre-Condition: \@require len(self.players) > 1 
#  Post-Condition: \@ensures len(self.properties) > 40 and self.dice.seed is not None and (\forall player in self.players: player.position == 0) 
#  Method Signature: def initialize(self) -> None: 

def set_properties() -> list[Property.Property]:
    properties = [    
    Property("Mediterranean Meals", "#a37759", 60, [2, 10, 30, 90, 160, 250]),
    Property("Baltic Breezeway", "#a37759", 60, [4, 20, 60, 180, 320, 450]),
    Property("Skipping Railroad", "#000000", 200, [25,50,100,200]),
    Property("Oriental Oasis", "#e8a541", 100, [6, 30, 90, 270, 400, 550]),
    Property("Vermont Vacation", "#e8a541", 100, [6, 30, 90, 270, 400, 550]),
    Property("Connecticut Courtyard", "#e8a541", 120, [8, 40, 100, 300, 450, 600]),
    Property("Sir Charles' Sanctuary", "#a14685", 140, [10, 50, 150, 450, 625, 750]),
    Property("United Estates", "#a14685", 140, [10, 50, 150, 450, 625, 750]),
    Property("Virginia Vineyards", "#a14685", 160, [12, 60, 180, 500, 700, 900]),
    Property("Quarter Railroad", "#000000", 200, [25,50,100,200]),
    Property("Saintly James' Square", "#ef756d", 180, [14, 70, 200, 550, 750, 950]),
    Property("Tunessee Avenue", "#ef756d", 180, [14, 70, 200, 550, 750, 950]),
    Property("Big Apple Avenue", "#ef756d", 200, [16, 80, 220, 600, 800, 1000]),
    Property("Kentucky Fried Avenue", "#ca6e47", 220, [18, 90, 250, 700, 875, 1050]),
    Property("Indy Car Avenue", "#ca6e47", 220, [18, 90, 250, 700, 875, 1050]),
    Property("Illusion Avenue", "#ca6e47", 240, [20, 100, 300, 750, 925, 1100]),
    Property("R. R. Railroad", "#000000", 200, [25,50,100,200]),
    Property("Atlantic Adventure", "#2277a2", 260, [22, 110, 330, 800, 975, 1150]),
    Property("Ventilation Avenue", "#2277a2", 260, [22, 110, 330, 800, 975, 1150]),
    Property("Marvin's Magic Meadow", "#2277a2", 280, [24, 120, 360, 850, 1025, 1200]),
    Property("Pacific Playground", "#55a95d", 300, [26, 130, 390, 900, 1100, 1275]),
    Property("Northern Charm Avenue", "#55a95d", 300, [26, 130, 390, 900, 1100, 1275]),
    Property("Penny-sylvania Avenue", "#55a95d", 320, [28, 150, 450, 1000, 1200, 1400]),
    Property("Longline Railroad", "#000000", 200, [25,50,100,200]),
    Property("Parking Place", "#e34537", 350, [35, 175, 500, 1100, 1300, 1500]),
    Property("Bored Walk", "#e34537", 400, [50, 200, 600, 1400, 1700, 2000])
    ]
    return properties

class Gameboard:
    """
    Sets up the board's intial rules and settings
 
    Attributes:
        properties: list of Properties with their default settings
    """
    properties = set_properties()


# Handle Turn Base Action
# Responsible for coordinating player actions during their turns by controlling the sequence of player turns and game events. 
# Pre-Condition: \@require self.game_running == True 
# Post-Condition: \@ensures self.current_player_index == \old(self.current_player_index) + 1 
# Method Signature: def handle_turn(self) -> None: 
