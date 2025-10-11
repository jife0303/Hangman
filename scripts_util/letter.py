"""Module for handling letters."""
from src.player import Player
from scripts_util.word import word_was_guessed
from scripts_util import logger


def add_letter_to_list(
        guessed_letter: str, selected_word: list, guessing_player: Player) -> Player:
    """Add guessed letter to the matching list.

    Skip remaining code if the guessed letter is the correct word. Else check
    if the letter exists in the word. Assign the letter to their correct
    position(s) if it exists. Else save it as wrong.

    Args:
        guessed_letter (list): Guessed letter that gets checked to decide where
            it gets stored in.
        selected_word (list): Word that is to be guessed.
        guessing_player (Player): Player, whose list get updated.

    Returns:
        guessing_player (Player): Player with their updated list.
    """
    if word_was_guessed(selected_word, list(guessed_letter)):
        guessing_player.guessing_word = list(guessed_letter)
        return guessing_player

    indexes: list = letter_in_word(guessed_letter, selected_word)
    if len(indexes) > 0:
        for index in indexes:
            guessing_player.guessing_word[index] = guessed_letter.upper()
    else:
        guessing_player.wrong_letters = add_wrong_letter(
            guessing_player.wrong_letters, guessed_letter)
    return guessing_player


def letter_in_word(guessed_letter: list, selected_word: list) -> list:
    """Check if guessed letter is in selected word.

    Args:
        guessed_letter (list): Check if this exists in the word list.
        selected_word (list): Check if guessed letter exists in this.

    Returns:
        letter_at_index (list): Includes the indexes, where the letter is at.
    """
    letter_at_index = []
    for index, letter in enumerate(selected_word):
        if letter == guessed_letter:
            letter_at_index.append(index)
    return letter_at_index


def add_wrong_letter(wrong_letters: list, letter: str) -> list:
    """Add wrong letter to list.

    Args:
        wrong_letters (list): list of wrong letters the wrong letter gets added
            to.
        letter (str): wrong letter that gets added to the list of wrong
            letters.

    Returns:
        wrong_letters (list): updated wrong letter list.
    """
    wrong_letters.append(letter.upper())
    return wrong_letters


def guess_letter() -> str:
    """Let player try guessing the word.

    Args:
        player (Player): Get correct word from this player.

    Returns:
        str: Player's guess.
    """
    while True:
        logger.play("Enter your choice (letter/whole word):")
        letter: str = str(input())
        if len(letter) >= 1 and letter.isalpha():
            return letter.upper()
        logger.error("Wrong input. Try again.")
