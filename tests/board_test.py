from feh.board import normal
from feh.board import normal_defensive
from feh.board import tree
from feh.board import tree_defensive
from feh.board import flyable
from feh.board import impassable

# Massive TODO here


def test_defensive_tiles():
    assert normal().is_defensive
    assert not normal_defensive().is_defensive
    assert tree().is_defensive
    assert not tree_defensive().is_defensive
    assert flyable().is_defensive
    assert not impassable().is_defensive

test_defensive_tiles()