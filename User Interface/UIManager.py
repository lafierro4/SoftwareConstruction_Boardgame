# UIManager
# Responsible for managing and coordination the game’s user interface. Interacts with other UI components for rendering and displaying the game information. 
# This is where we will have all the pygame components, along with the other UI classes

# Initial Board Rendering 
# Collaborates with the GameBoardView to render the Initial Board State. 
# Pre-Condition: \@requires self.ui.board.is_rendered == False 
# Post-Condition: \@ensures self.ui.board.is_rendered == True 
# Method Signature: def render_initial_board(self) -> None: 

# Player Info Display 
# Informs PlayerView how to display the Player’s status and information. 
# Pre-Condition: \@requires self.is_valid_status(player_status) == True 
# Post-Condition: \@ensures self.ui.display_status() 
# Method Signature: def display_player_status(self) -> None: 

# Menu Management 
# Helps layer the Menu assets to display the correct formatting 
# Pre-Condition: \@requires self.is_layered_menu() == True 
# Post-Condition: \@ensures self.ui.display_menu() 
# Method Signature: def form_menu(self) -> None: 