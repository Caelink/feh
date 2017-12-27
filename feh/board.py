from collections import namedtuple


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
normal = lambda: Space('N')
normal_defensive = lambda: Space('ND', True)
tree = lambda: Space('T')
tree_defensive = lambda: Space('TD', True)
flyable = lambda: Space('F')
impassable = lambda: Space('I')


class Board():
    def __init__(self, spaces=None):
        self.spaces = [[normal() for i in range(6)] for j in range(8)] if not spaces else spaces


    def __str__(self):
        return str(self.spaces)


    def pprint(self):
        """This was fun to write sorry if you want to try to read it though
        """
        print('\n'.join(map(lambda x: ' '.join(map(lambda y: str(y), x)), self.spaces)))

if __name__ == '__main__':
    x = Board()
    x.pprint()
