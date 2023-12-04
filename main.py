#Method made in order to start the system from the terminal
#Calls start_game() method from UIManager, 
# TO DO Make it possible for the user to select the number of player in the command line with arguments
# Example: python main.py 4 makes a game with 4 Players - LF

import User_Interface.UIManager as game


if __name__ == "__main__":
    game_start = game.Cloneopoly()