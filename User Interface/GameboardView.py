# GameboardView
# In charge of rendering the game board, properties, and other visual 
# elements related to the game board. Handles user interactions with the game board, such as property selections and purchases. 

# Update Game Board 
# Renders the current game state in real time by communicating with the Game Board Manager. 
# Pre-Condition: \@requires self.is_valid_game_state == True 
# Post-Condition: \@ensures self.update_board() 
# Method Signature: def update_game_board(self, board: GameboardManager, player_action) 

# Render Player Position 
# Renders Player’s position and movement whenever a change in game state occurs. 
# Pre-Condition: \@requires player is not None and player.position >= 0 and player.position <= 40 
# Post-Condition: \@ensures self.player_rendered() 
# Method Signature: def render_player_position(self, player: Player) -> None: 

# Render Dice Roll 
# Render the Dice Roll Animation when the Player rolls any dice. 
# Pre-Condition: \@requires roll >= 1 and roll <= 6 
# Post-Condition: \@ensures self.dice_rendered() 
# Method Signature: def render_dice_roll(self, roll: int) -> None: 