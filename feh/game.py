from feh.unit import Unit, Skills
from feh.board import Board

def generic_units():
    return [
        Unit(
            name=str(i),
            health=1,
            attack=1,
            defence=1,
            resistance=1,
            speed=1,
            skills=Skills(),
        )
        for i in range(4)
    ]

def run_game():
    board = Board(starting_zones=[[(0, i) for i in range(4)], [(0, i) for i in range(4)]])
    board.place_units(generic_units(), 0)
    board.place_units(generic_units(), 1)
