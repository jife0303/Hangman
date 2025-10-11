"""Module for testing game.py"""
import pytest
from src.game import add_players, someone_won, game_logic, Game
from src.player import Player


@pytest.fixture
def player():
    """Initialize a player for testing.

    Returns:
        Player
    """
    return Player("Jialin", 1)


def test_add_players():
    """Test for adding players to game."""
    players = add_players()
    assert isinstance(players["player_1"], Player)
    assert isinstance(players["player_2"], Player)


def test_someone_won(player: Player):
    """Test for checking who won."""
    guessing_player = player
    guessing_player.wrong_letters = ["c"] * 12
    afk_player = Player("AFK", 1)
    assert someone_won(guessing_player, afk_player)
    guessing_player.wrong_letters = ["c"] * 11
    afk_player.selected_word = "hello"
    guessing_player.guessing_word = ""
    assert someone_won(guessing_player, afk_player) is False
    guessing_player.guessing_word = "hello"
    assert someone_won(guessing_player, afk_player)


def test_game_logic():
    """Test for the game logic."""
    game = Game()
    afk_player = Player("", 1)
    guessing_player = Player("", 2)
    afk_player.selected_word = "hello"
    guessing_player.guessing_word = "hello"
    game.players["player_1"] = afk_player
    game.players["player_2"] = guessing_player
    assert game_logic(game)

    game_2 = Game()
    afk_player = Player("", 1)
    guessing_player = Player("", 2)
    afk_player.selected_word = "goobye"
    guessing_player.wrong_letters = "qwertzuiopasdfghjkl"
    guessing_player.guessing_word = ""
    game_2.players["player_1"] = afk_player
    game_2.players["player_2"] = guessing_player
    assert game_logic(game_2)
