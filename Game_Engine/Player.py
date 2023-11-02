# Player
# Represent individual players in the game, storing their assets, financial status, and property holdings.

# class Player:
# money, connect to bank
# list of Properties, connect to Property
# name
# token

# Update Player Funds
# Change the amount of money the player has and perform any actions as a result of reaching this new amount.
# Pre-Condition: \@requires new_amount >= 0
# Post-Condition: \@ensures self.funds == new_amount
# Method signature: def update_funds(self, new_amount) -> None:


# Update Property
# Not in the SDD but we should have a method that updates the property of the player


# from Game_Engine.Property import Property


import functools


class Player:
    def __init__(self, name: str, token) -> None:
        self._name = name
        self.token = token
        self._balance = 1500
        self._properties = []
        self._position = 0
        self._last_roll = 0

    def move(self, steps: int) -> None:
        """
        Moves the player a specified number of steps.

        Args:
            steps: The number of squares the player will move forward.
        """
        self._position = (self._position + steps) % 26
        self._last_roll = steps

    def pay_rent(self, owner, amount: int) -> None:
        if self._balance >= amount:
            self._balance -= amount
            owner.balance += amount

    def is_bankrupt(self) -> bool:
        return self._balance < 0

    def increase_funds(self, amount):
        if amount >= 0:
            self._balance += amount
        else:
            exit

    def decrease_funds(self, amount: int) -> None:
        if amount >= 0:
            self._balance -= amount
        else:
            exit

    def calculate_assets(self):
        return functools.reduce(lambda property: property._price, self._properties)

    # def add_property(self, property: Property) -> None:
    #     self._properties.append(property)

    def move_player(self, win, game_board, pos_x):
        for x in range(100):  # animate 100 frames
            win.blit(game_board.board_surface, (0, 0))  # erase board
            position = self.token.get_rect()  # gets player rectangle
            pos_x += game_board.property_size
            position.move_ip(pos_x, 0)
            win.blit(self.token, position)  # redraws player token
            return pos_x

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def last_roll(self) -> int:
        return self._last_roll

    @property
    def position(self) -> int:
        return self._position
