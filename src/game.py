"""Module for game logic."""
from scripts_util import logger
from scripts_util.word import select_word, word_was_guessed
from scripts_util.letter import guess_letter, add_letter_to_list
from src.player import Player


class Game:
    """Game class, which has a dictionary of players."""

    def __init__(self):
        self.players: dict
        self.setup()

    def setup(self):
        """Add players to the game."""
        self.players = add_players()


def start_game(game: Game):
    """Start the game.

    Let first player decide on the word the second player has to guess.
    Initialise list variable from the guessing player to show length and status
    of the wanted word. Then start the guessing process.

    Args:
        game (Game): The played game, where also the players are stored in.
    """
    player_1: Player
    player_2: Player
    player_1, player_2 = get_players(game)
    logger.info(f"'{player_1}'s turn:")
    player_1.selected_word = select_word(player_1)
    player_2.guessing_word = [""] * len(player_1.selected_word)
    game_logic(game)


def game_logic(game: Game) -> bool:
    """Loop guessing player's turn until someone wins.

    First get the players, which will be used in the logic. Loop the guess
    process and break out if someone wins.

    Args:
        game (Game): The played game, where also the players are stored in.
    """
    afk_player: Player
    guessing_player: Player
    afk_player, guessing_player = get_players(game)
    logger.info(f"'{guessing_player}'s turn:")
    while True:
        logger.info(f"Current word status: {guessing_player.guessing_word}")
        logger.info(f"Mistakes: {len(guessing_player.wrong_letters)}")
        logger.info(f"Wrong letters: {guessing_player.wrong_letters}")
        if someone_won(guessing_player, afk_player):
            return True
        guessed_letter = guess_letter()
        guessing_player = add_letter_to_list(
            guessed_letter, afk_player.selected_word, guessing_player)


def game_over(player: Player, selected_word: list):
    """Add a round win to the player.

    Args:
        player (Player): Who won the round.
        selected_word (list): Word that was to be guessed.
    """
    selected_word[0].lower()
    player.round_wins = add_round_win(player.round_wins)
    logger.info(f"'{player}' has won this round.")
    logger.info(f"The word was '{''.join(selected_word)}'")
    logger.info("Game over.")


def someone_won(guessing_player: Player, afk_player: Player) -> bool:
    """Check if anyone won by checking against mistakes and word status.

    Args:
        guessing_player (Player): Check if they have over 12 mistakes and if
            they have guessed the word.
        afk_player (Player): They win, if guessing_player has over 12 mistakes.

    Returns:
        bool: True, if someone won.
    """
    if len(guessing_player.wrong_letters) >= 12:
        game_over(afk_player, afk_player.selected_word)
        return True
    if word_was_guessed(
            afk_player.selected_word, guessing_player.guessing_word):
        game_over(guessing_player, afk_player.selected_word)
        return True
    return False


def add_round_win(round_wins: int) -> int:
    """Add 1 to round wins.

    Args:
        round_wins (int): Increase by 1.

    Returns:
        int: Round wins + 1.
    """
    return round_wins + 1


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
