from abc import ABC, abstractmethod
from Game_Engine.Player import Player


class Space(ABC):
    """Represents an abstract space on the Monopoly board."""

    def __init__(self, name: str, square_type: str, color: str):
        self._name = name
        self._square_type = square_type
        self._color = color


    @abstractmethod
    def action(self, player: Player) -> None:
        """
        Executes the action taken when a players lands on this space.

        Args:
            player: The player that has landed on the space.
        """
        pass