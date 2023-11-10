from Game_Engine.Player import Player
from Game_Engine.Space import Space


class Square(Space):
    """Represents a square on the Monopoly board."""

    def __init__(self, name: str, square_type: str, color: str = "#a37759"):
        Space.__init__(self, name, square_type, color)

    def action(self, player: Player) -> None:
        """
        Executes the action taken when a players lands on this square.

        Args:
            player: The player that has landed on the square.
        """
        if self.square_type == "chance":
            pass
        elif self.square_type == "community_chest":
            self._community_chest_action(player)
        elif self.square_type == "corner":
            pass
        elif self.square_type == "jail":
            pass
        elif self.square_type == "go_to_jail":
            pass
        elif self.square_type == "tax":
            self._tax_action(player)
    
    def _chance_action(self, player: Player) -> None:
        pass

    def _community_chest_action(self, player: Player) -> None:
        pass

    def _jail(self, player: Player) -> None:
        pass

    def go_to_jail(self, player: Player) -> None:
        pass

    def _tax_action(self, player: Player) -> None:
        """
        Allows the player to pay tax to the bank.

        If the player's balance is above the fixed tax amount ($200), the
        player will be prompted to pay either a fixed amount or a tax
        percentage of their total assets (10%).

        Args:
            player (Player): The player that has landed on the tax square.
        """
        player.decrease_balance(int(player.balance * 0.1))
        return
        # TODO Determine if user wants to pay $200 or 10%
        #choice = "percentage" if player.balance < 200 else "fixed"
        #if choice == "fixed":
        #    player.decrease_balance(200)
       # else:
        

    @property
    def name(self) -> str:
        return self._name

    @property
    def square_type(self) -> str:
        return self._square_type

    @property
    def color(self) -> str:
        return self._color
