#Method made in order to start the system from the terminal
#Calls start_game() method from UIManager, 
# TO DO Make it possible for the user to select the number of player in the command line with arguments
# Example: python main.py 4 makes a game with 4 Players - LF

from User_Interface.UIManager import start_game

if __name__ == '__main__':
    start_game(4)