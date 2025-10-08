"""Module for game logic."""
import getpass
from src import logger
from src.player import Player


class Game:
    """Game class for handling the game."""

    def __init__(self):
        self.players = add_players()


def start_game(game: Game):
    """Start the game.
    
    Let first player decide on the word the second player has to guess. Then
    start the guessing process (game_logic()).
    """
    player_1: Player
    player_2: Player
    player_1, player_2 = get_players(game)
    logger.info(f"'{player_1}'s turn:")
    player_1.selected_word = select_word(player_1)
    player_2.guessing_word = [""] * len(player_1.selected_word)
    game_logic(game)


def game_logic(game: Game):
    """Handle the game logic, including game loop.
    
    First get the player objects, which will be used in the logic.Loop the
    guess process and break out if someone wins.
    
    Args:
        game (Game): game object that is used to play the game.
    """
    afk_player: Player
    guessing_player: Player
    afk_player, guessing_player = get_players(game)
    logger.info(f"'{guessing_player}'s turn:")
    while True:
        logger.game(f"Current word status: {guessing_player.guessing_word}")
        logger.game(f"Mistakes: {len(guessing_player.wrong_letters)}")
        logger.game(f"Wrong letters: {guessing_player.wrong_letters}")
        if someone_won(guessing_player, afk_player):
            return True
        guessed_letter = guess_letter()
        guessing_player = add_letter_to_list(
            guessed_letter, afk_player.selected_word, guessing_player)


def someone_won(guessing_player: Player, afk_player: Player) -> bool:
    """Check if anyone won.
    
    Args:
        guessing_player (Player): Check if they have over 12 mistakes and if they
            have guessed the word.
        afk_player (Player): They win, if guessing_player has over 12 mistakes.

    Returns:
        bool: True, if someone won.
    """
    if len(guessing_player.wrong_letters) >= 12:
        game_over(afk_player)
        return True
    elif word_was_guessed(
            ''.join(afk_player.selected_word),
            ''.join(guessing_player.guessing_word)):
        game_over(guessing_player)
        return True
    return False


def add_letter_to_list(
        guessed_letter: str, selected_word: list, guessing_player: Player) -> Player:
    """Add guessed letter to the matching list.

    Skip remaining code if the guessed letter is the correct word. If not,
    check if the letter exists in the word. Assign the letter to their correct
    position(s) if it was correct. Else save it as wrong.
    
    Args:
        guessed_letter (str): Guessed letter that gets checked to decide where
            it gets moved to.
        selected_word (list): The word that is to be guessed.
        guessing_player (Player): The player, whose list get updated.
    
    Returns:
        guessing_player (Player): Return player with their updated list.
    """
    if word_was_guessed(''.join(selected_word), guessed_letter):
        guessing_player.guessing_word = list(guessed_letter)
        return guessing_player
    
    indexes: list = letter_in_word(guessed_letter, selected_word)
    if len(indexes) > 0:
        for index in indexes:
            guessing_player.guessing_word[index] = guessed_letter
    else:
        guessing_player.wrong_letters = add_wrong_letter(
            guessing_player.wrong_letters, guessed_letter)
    return guessing_player


def letter_in_word(guessed_letter: str, selected_word: list) -> list:
    """Check if guessed letter is in selected word.
    
    Args:
        guessed_letter (str): Check if this exists in the word list.
        selected_word (list): Check if guessed letter exists in this.
    
    Returns:
        letter_in_index (list): Includes the indexes, where the letter is at.
    """
    letter_in_index = []
    for index, letter in enumerate(selected_word):
        if guessed_letter == letter:
            letter_in_index.append(index)
    return letter_in_index


def guess_letter() -> str:
    """Let player try guessing the word.

    Args:
        player (Player): Get correct word from this player.

    Returns:
        str: Player's guess.
    """
    while True:
        logger.game("Enter your choice (letter/whole word):")
        data: str = str(input())
        if len(data) >= 1 and data.isalpha():
            return data
        logger.error("Wrong input. Try again.")


def game_over(player: Player):
    """Handle game over situation.

    Args:
        player (Player): Player, who won the round.
    """
    player.round_wins = add_round_win(player.round_wins)
    logger.info(f"'{player}' has won this round.")
    logger.info("Game over.")


def get_players(game: Game) -> tuple:
    """Get player objects.

    Args:
        game (Game): game object to get its player objects.

    Returns:
        tuple: consisting of player objects.
    """
    player_1: Player = game.players["player_1"]
    player_2: Player = game.players["player_2"]
    return player_1, player_2


def word_was_guessed(selected_word: str, guessing_word: str) -> bool:
    """Check if word has been guessed.

    Args:
        selected_word (str): word that is to be guessed.
        guessing_word (str): current status of the guessing word.

    Returns:
        bool: True if word has been guessed.
    """
    if selected_word.lower() == guessing_word.lower():
        return True
    return False


def add_players() -> dict:
    """Add two players to the game.

    Returns:
        players (dict): same dict that gets returned
    """
    players = {
        "player_1": None,
        "player_2": None
    }
    for x in range(1, 3):
        player = Player(name=None, player_number=x)
        players[f"player_{x}"] = player
        logger.info(f"'{player}' has beed added to the game.")
    return players


def select_word(player: Player) -> list:
    """Let player select word to be guessed.
    
    Args:
        player (Player): Player object that gets to choose the word.

    Returns:
        word (list): selected word that consists of only letters, split into
            single letters.
    """
    while True:
        logger.game(f"'{player}', please select the word:")
        word: str = getpass.getpass("")
        if word.isalpha():
            return list(word.lower())
        logger.error("Invalid word. Word can only consist of letters.")


def add_round_win(round_wins: int) -> int:
    """Add 1 to round wins.
    
    Args:
        round_wins (int): Increase by 1.

    Returns:
        int: Round wins + 1.
    """
    return round_wins + 1


def add_wrong_letter(wrong_letters: list, letter: str) -> list:
    """Add wrong letter to list.
    
    Args:
        wrong_letters (list): list of wrong letters the wrong letter gets added
            to.
        letter (str): wrong letter that gets added to the list of wrong letters
            .
    
    Returns:
        wrong_letters (list): updated wrong letter list.
    """
    wrong_letters.append(letter.lower())
    return wrong_letters