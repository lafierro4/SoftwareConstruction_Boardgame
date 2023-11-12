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

import functools ,pygame


class Player:
    def __init__(self, name: str, token: pygame.Surface, space_size) -> None:
        self._name = name
        self._token = token
        self._balance = 1500
        self._assets = []
        self._position = 0
        self._last_roll = 0
        self._position_x = space_size * 11
        self._position_y = space_size * 11

    def move(self, steps: int) -> int:
        """
        Moves the player a specified number of steps.

        Increments the player's position by the specified number of steps. If
        the player's new position happens to be more than 40 (where the player
        has circled the entire board), then $200 will be added the their
        balance and the offset is set as the new position.

        Args:
            steps: The number of squares the player will move forward.
        
        Returns:
            The player's new position.
        """
        old_position = self._position
        self._position = (self._position + steps) % 40
        if old_position > self._position:
            self._balance += 200
        self._last_roll = steps
        return self._position

    def set_position(self, x, y):
        self._position_x = x
        self._position_y = y
    
    def transfer_money(self, owner, amount: int) -> None:
        """
        Pays rent out to a property owner.
        """
        if self._balance >= amount:
            self._balance -= amount
            owner.balance += amount

    def add_property(self, property_item):
        self._assets.append(property_item)

    def is_bankrupt(self) -> bool:
        return self._balance < 0

    def increase_balance(self, amount):
        if amount >= 0:
            self._balance += amount
        else:
            return

    def decrease_balance(self, amount: int) -> None:
        if amount >= 0:
            self._balance -= amount
        else:
            return

    def calculate_assets(self) -> int:
        return functools.reduce(lambda sum_assets, asset: asset.price + sum_assets, self._assets)
    
    def owns_both_utilities(self) -> bool:
        return sum(asset.square_type == "utility" for asset in self._assets) >= 2

    # def add_property(self, property: Property) -> None:
    #     self._properties.append(property)


    @property
    def assets(self):
        if self._assets is not None:
            return self._assets
        else:
            return None

    @property
    def token(self) -> pygame.Surface:
        return self._token

    @property
    def name(self) -> str:
        return self._name

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def last_roll(self) -> int:
        return self._last_roll