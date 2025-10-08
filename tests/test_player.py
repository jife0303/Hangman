"""Module for testing player.py"""
import pytest
from src.player import set_name
from src.player import Player

# Used for testing with a player object
@pytest.fixture
def player():
    return Player("Jialin", 1)


def test_set_name():
    """Test for setting the name."""
    assert set_name("Jialin", 1) == "Jialin"
    assert set_name(None, 1) == "Player 1"
    assert set_name(None, 2) == "Player 2"


def test_player():
    """Test for initialization of players."""
    assert Player("Jialin", 1)

