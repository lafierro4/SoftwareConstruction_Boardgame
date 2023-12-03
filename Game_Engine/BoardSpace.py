from abc import ABC, abstractmethod


class BoardSpace(ABC):
    """Represents an abstract space on the Monopoly board."""

    def __init__(self, name: str, space_type: str, color: str):
        self._name = name
        self._space_type = space_type
        self._color = color
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def space_type(self) -> str:
        return self._space_type

    @property
    def color(self) -> str:
        return self._color


    @abstractmethod
    def action(self, player) -> None:
        """
        Executes the action taken when a players lands on this space.

        Args:
            player: The player that has landed on the space.
        """
        pass