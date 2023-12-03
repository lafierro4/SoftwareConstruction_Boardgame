from Game_Engine.Player import Player
from Game_Engine.BoardSpace import BoardSpace


class Square(BoardSpace):
    """Represents a square on the Monopoly board."""

    def __init__(self, name: str, square_type: str, color: str = "#cce6cf"):
        if square_type == "corner":
            color = "#cce6cf"
        elif square_type == "tax":
            color = "#a0c0c0"
        BoardSpace.__init__(self, name, square_type, color)

    def action(self, player: Player) -> None:
        """
        Executes the action taken when a players lands on this square.

        Args:
            player: The player that has landed on the square.
        """
        if self.space_type == "corner":
            pass
        elif self.space_type == "jail":
            self._jail(player)
        elif self.space_type == "go_to_jail":
            self._go_to_jail_action(player)
        elif self.space_type == "tax":
            self._tax_action(player)

    def _jail(self, player: Player) -> None:
        pass

    def _go_to_jail_action(self, player: Player) -> None:
        player.set_jail_status(True)
        player.change_position(10)

    def _tax_action(self, player: Player) -> None:
        """
        Allows the player to pay tax to the bank.

        The player will pay a tax percentage of their total balance (10%).

        Args:
            player (Player): The player that has landed on the tax square.
        """
        player.decrease_balance(int(player.balance * 0.1))

    @property
    def name(self) -> str:
        return self._name

    @property
    def space_type(self) -> str:
        return self._space_type

    @property
    def color(self) -> str:
        return self._color