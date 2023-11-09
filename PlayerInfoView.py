# PlayerInfoView
# Displays player-specific information, including names, financial status, and property ownership. Ensures player’s data is accurately presented to the user.

# Show Property Details 
# Communicates with any Property to display its information when a player selects it. (Owned by them, someone else, Or no one) 
# Pre-Condition: \@requires self.is_property_owned() or not self.is_property_owned() 
# Post-Condition: \@ensures self.ui.display_property_selected() 
# Method Signature: display_property(self) ->None 
import  tkinter as tk

class PlayerInfoView:
    def __init__(self, root, playername):
        self.root = root
        self.player_name = playername
        self.player_info = None  # Player information will be displayed here

        # Create a button to show player information
        self.button = tk.Button(root, text=f"View {self.player_name}'s Info", command=self.display_player_info)
        self.button.pack()
        
    def display_player_info(self):
        # Create a new window for displaying player information
        self.player_info = tk.Toplevel(self.root)
        self.player_info.title(f"{self.player_name}'s Information")

        # Add labels and text fields to display player information
        label_name = tk.Label(self.player_info, text=f"Player Name: {self.player_name}")
        label_name.pack()

        # Add labels and text fields to display financial status and property ownership
        label_financial_status = tk.Label(self.player_info, text="Financial Status:")
        label_financial_status.pack()

        # You can retrieve financial status from your existing data structures and classes
        financial_status = "Retrieve Financial Status Here"
        text_financial_status = tk.Label(self.player_info, text=financial_status)
        text_financial_status.pack()

        label_property_ownership = tk.Label(self.player_info, text="Property Ownership:")
        label_property_ownership.pack()

        # You can retrieve property ownership information from your existing data structures and classes
        property_ownership = "Retrieve Property Ownership Here"
        text_property_ownership = tk.Label(self.player_info, text=property_ownership)
        text_property_ownership.pack()
    
if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Cloneopoly Game")

    # Create PlayerView instances for each player
    player1_view = PlayerInfoView(root, "Player 1")
    player2_view = PlayerInfoView(root, "Player 2")

    root.mainloop()