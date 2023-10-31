class Square:
    def __init__(self, name: str, color: str = "#a37759"):
        self._name = name
        self._color = color

    @property
    def name(self) -> str:
        return self._name

    @property
    def color(self) -> str:
        return self._color
