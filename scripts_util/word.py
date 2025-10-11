"""Module for handling words."""
import getpass
from src.player import Player
from scripts_util import logger

def word_was_guessed(selected_word: list, guessing_word: list) -> bool:
    """Check if word has been guessed.

    Args:
        selected_word (list): word that is to be guessed.
        guessing_word (list): current status of the guessing word.

    Returns:
        bool: True if word has been guessed.
    """
    if selected_word == guessing_word:
        return True
    return False


def select_word(player: Player) -> list:
    """Let player select word to be guessed.
    
    Args:
        player (Player): Player object that gets to choose the word.

    Returns:
        word (list): selected word that consists of only capitalized letters.
    """
    while True:
        logger.play(f"'{player}', please select the word:")
        word: str = getpass.getpass("")
        if word.isalpha():
            return list(word.upper())
        logger.error("Invalid word. Word can only consist of letters.")
