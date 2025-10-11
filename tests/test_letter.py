"""Module for testing letter.py."""
import pytest
from scripts_util.letter import letter_in_word, add_letter_to_list
from src.player import Player


@pytest.fixture
def player():
    """Initialize a player for testing.

    Returns:
        Player
    """
    return Player("Jialin", 1)


def test_add_letter_to_list(player: Player):
    """Test for adding the letter to the correct list."""
    player.guessing_word = [""] * 5
    player = add_letter_to_list("e", "hello", player)
    assert player.guessing_word == ["", "E", "", "", ""]
    player.guessing_word = [""] * 5
    player = add_letter_to_list("a", "hello", player)
    assert player.wrong_letters == ["A"]


def test_letter_in_word():
    """Test for checking if guessed letter is in selected word."""
    assert letter_in_word("e", list("hello")) == [1]
    assert letter_in_word("l", list("hello")) == [2, 3]
