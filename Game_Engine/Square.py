from Game_Engine.Player import Player


class Square:
    """Represents a square on the Monopoly board."""

    def __init__(self, name: str, color: str = "#a37759"):
        self._name = name
        self._color = color

    def action(self, player: Player) -> None:
        """
        Executes the action taken when a players lands on this square.

        Args:
            player: The player that has landed on the square.
        """
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def color(self) -> str:
        return self._color
