"""Module for testing word.py."""
from scripts_util.word import word_was_guessed


def test_word_was_guessed():
    """Test for guessing the word."""
    assert word_was_guessed("hello", "hello")
    assert word_was_guessed("hello", "nothello") is False
    assert word_was_guessed("hello", "lo") is False
