from feh.board import normal


def test_defensive_tiles():
    assert not is_defensive(Space.normal)
    assert is_defensive(Space.normal_defensive)
    assert not is_defensive(Space.tree)
    assert is_defensive(Space.tree_defensive)
    assert not is_defensive(Space.impassable)


try:
    test_defensive_tiles()
except AssertionError as e:
    print "Failure", e