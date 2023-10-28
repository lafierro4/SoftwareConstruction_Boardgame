# PlayerInfoView
# Displays player-specific information, including names, financial status, and property ownership. Ensures player’s data is accurately presented to the user.

# Show Property Details 
# Communicates with any Property to display its information when a player selects it. (Owned by them, someone else, Or no one) 
# Pre-Condition: \@requires self.is_property_owned() or not self.is_property_owned() 
# Post-Condition: \@ensures self.ui.display_property_selected() 
# Method Signature: display_property(self) ->None 