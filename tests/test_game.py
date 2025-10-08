"""Module for testing player.py"""
import pytest
from src.game import (add_players, word_was_guessed, add_letter_to_list,
                      someone_won, letter_in_word, game_logic, Game
                      )
from src.game import Player

# Used for testing with a player object
@pytest.fixture
def player():
    return Player("Jialin", 1)

def test_add_players():
    """Test for adding players to game."""
    players = add_players()
    assert players["player_1"] is not None
    assert players["player_2"] is not None


def test_word_was_guessed():
    """Test for guessing the word."""
    assert word_was_guessed("hello", "hello")
    assert word_was_guessed("hello", "nothello") is False


def test_add_letter_to_list(player: Player):
    """Test for adding the letter to the correct list."""
    player.guessing_word = [""] * 5
    player = add_letter_to_list("e", list("hello"), player)
    assert player.guessing_word == ["", "e", "", "", ""]


def test_someone_won(player: Player):
    """Test for checking who won."""
    guessing_player = player
    guessing_player.wrong_letters = ["c"] * 12
    afk_player = Player("AFK", 1)
    assert someone_won(guessing_player, afk_player)
    guessing_player.wrong_letters = ["c"] * 11
    afk_player.selected_word = list("hello")
    assert someone_won(guessing_player, afk_player) is False
    guessing_player.guessing_word = list("hello")
    assert someone_won(guessing_player, afk_player)


def test_letter_in_word():
    """Test for checking if guessed letter is in selected word."""
    assert letter_in_word("e", list("hello")) == [1]
    assert letter_in_word("l", list("hello")) == [2, 3]


def test_game_logic():
    """Test for the game logic."""
    game = Game()
    afk_player = Player("", 1)
    guessing_player = Player("", 2)
    afk_player.selected_word = list("hello")
    guessing_player.guessing_word = list("hello")
    game.players["player_1"] = afk_player
    game.players["player_2"] = guessing_player
    assert game_logic(game)

    game_2 = Game()
    afk_player = Player("", 1)
    guessing_player = Player("", 2)
    guessing_player.wrong_letters = list("qwertzuiopasdfghjkl")
    afk_player.selected_word = list("goobye")
    game_2.players["player_1"] = afk_player
    game_2.players["player_2"] = guessing_player
    assert game_logic(game_2)
