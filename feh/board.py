# from feh.unit import Unit, Skills
from collections import namedtuple
from random import choice

Unit = namedtuple('unit', 'name health attack defence resistance speed skills')
Skills = namedtuple('skills', 'a b c seal weapon assist special')

class Space(
    namedtuple('space', 
        ['movement_type', 'is_defensive']
    )):
    def __new__(cls, movement_type='?', is_defensive=False):
        self = super(Space, cls).__new__(cls, movement_type, is_defensive)
        return self

    def __str__(self):
        return self.movement_type


# Creation lambdas might make factory?
normal = lambda: Space('N ')
normal_defensive = lambda: Space('ND', True)
tree = lambda: Space('T ')
tree_defensive = lambda: Space('TD', True)
flyable = lambda: Space('F ')
impassable = lambda: Space('I ')
all_types = [normal, normal_defensive, tree, tree_defensive, flyable, impassable]


def _format_map(map_list):
    """This was fun to write sorry if you want to try to read it though
    """
    return '\n'.join(
        map(
            lambda x: ' '.join(
                map(lambda y: str(y), x)
            ),
            map_list
        )
    )

class Board():
    def __init__(self, starting_zones, spaces=None):
        self.starting_zones = starting_zones
        self.spaces = [[normal() for i in range(6)] for j in range(8)] if not spaces else spaces
        self.units = [[None for i in range(6)] for j in range(8)]

    def __str__(self):
        return _format_map(self.spaces) + '\n' + _format_map(self.units)

    def place_units(self, units, player):
        starting_zone = self.starting_zones[player]
        assert len(units) <= len(starting_zone)
        for index, unit in enumerate(units):
            x, y = self.starting_zones[player][index]
            assert self.units[x][y] is None
            self.units[x][y] = unit

def generic_units():
    return [
        Unit(
            name=str(i),
            health=1,
            attack=1,
            defence=1,
            resistance=1,
            speed=1,
            skills=None,
        )
        for i in range(4)
    ]

if __name__ == '__main__':
    board = Board(starting_zones=[[(0, i) for i in range(4)], [(5, i) for i in range(4)]])
    board.place_units(generic_units(), 0)
    board.place_units(generic_units(), 1)

    print(board)

    print(_format_map([[choice(all_types)() for i in range(6)] for j in range(8)]))
