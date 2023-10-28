# MenuView
# Manages the various menu and options within the game, including the main menu, settings, and in-game menu.
# It allows players to navigate and make selections within the game. 

# Display Choice 
# Informs the GameBoardView about the user’s display setting such as size, brightness, or color blindness. 
# Pre-Conditions: \@requires self.is_initialized() 
# Post-Condition: \@ensures self.ui.display_updated_settings() 
# Method Signature: def display_choice(self) -> None: 