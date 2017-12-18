from enum import Enum
from collections import namedtuple

class Space(namedtuple('space', 
    ['movement_type', 'is_defensive']
    ))
    def __new__(cls, movement_type='?', is_defensive=False):
        self = super(Z, cls).__new__(cls, movement_type, is_defensive)
        return self

    # def __init__(self, movement_type, is_defensive, ascii):
    #     return

# Creation lambdas
normal = lambda: Space('N')
normal_defensive = lambda: Space('ND', True)
tree = lambda: Space('T')
tree_defensive = lambda: Space('TD', True)
flyable = lambda: Space('F')
impassable = lambda: Space('I')


class Board():
    def __init__(self):
        self.spaces = [normal() for i in range(6 * 8)]


    def __str__(self):
        return str(self.spaces)


    def __pprint__(self):
        print('\n'.join('|'.join(map(lambda x: x.movement_type), self.spaces)))



