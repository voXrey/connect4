from dataclasses import dataclass

@dataclass
class Player:
    """Class of players's data"""
    name: str
    tab_number: int
    symbol: str
    type: str

    def __init__(self, name:str, tab_number:int, symbol:str, type:str):
        self.name = name
        self.tab_number = tab_number
        self.symbol = symbol
        self.type = type

@dataclass
class GameModel:
    """Class of game's data"""
    tab: list[list[int]] = None

    player1 = Player(
        name="Player1",
        tab_number=1,
        symbol="X",
        type="random"
    )
    player2 = Player(
        name="Player2",
        tab_number=-1,
        symbol="O",
        type="random"
    )

    counter:int = 0

    lines_count:int = 6
    columns_count:int = 7

