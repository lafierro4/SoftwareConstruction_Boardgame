
import pygame

class Player:
    """
    Represents a Player

    A Player is a human or AI player that has can move across the board, contain token, assets, and balance.
    """
    def __init__(self, name: str, token: pygame.Surface, space_size, button = None, is_ai:bool = False) -> None:
        self._name = name
        self._token = token
        self.button = button
        self._balance = 1500
        self._is_ai:bool = is_ai
        self._assets = []
        self._position = 0
        self._last_roll = 0
        self._position_x = space_size * 11
        self._position_y = space_size * 11
        self._in_jail = False
    
    # region Contract Manage Position

    @property
    def position(self) -> int:
        return self._position

    def change_position(self, position: int) -> int:
        """
        Sets the player's position to a certain space on the board.

        Updates the player's position, taking into account the number of spaces
        on the board by taking the modulus of 40.

        Returns:
            The player's new position.
        """
        self._position = position % 40
        return self._position

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
        new_position = self.change_position(old_position + steps)
        if old_position > new_position:
            self.increase_balance(200)
        self._last_roll = steps
        return new_position
    
    # endregion

    # region Contract Manage Balance

    def increase_balance(self, amount: int) -> None:
        if amount >= 0:
            self._balance += amount
        else:
            return

    def decrease_balance(self, amount: int) -> None:
        if amount >= 0:
            self._balance -= amount
        else:
            return
    
    # endregion

    def set_position(self, x, y):
        self._position_x = x
        self._position_y = y
    
    def transfer_money(self, owner, amount: int) -> bool:
        """
        Pays rent out to a property owner.
        returns True if transfer was successful otherwise
        False if rent bankrupted player, transfers remaing balance to owner
        """
        if (self._balance - amount) <= 0:
            owner.balance += self.balance
            self.balance = 0
            return False
        else:
            owner.balance += amount
            self._balance -= amount
            return True

    def add_property(self, property_item) -> None:
        self._assets.append(property_item)

    def is_bankrupt(self) -> bool:
        return self._balance <= 0
    
    def in_jail(self) -> bool:
        return self._in_jail
    
    def set_jail_status(self, in_jail: bool) -> None:
        self._in_jail = in_jail

    def owns_both_utilities(self) -> bool:
        return sum(asset.space_type == "utility" for asset in self._assets) >= 2

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
    def is_ai(self) -> bool:
        return self._is_ai
    
    @is_ai.setter
    def is_ai(self, value:bool):
        self._is_ai = value

    @property
    def last_roll(self) -> int:
        return self._last_roll