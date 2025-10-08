"""Module for player logic."""

class Player:
    """Player class for handling the players."""
    def __init__(self, name: str, player_number: int):
        self.name: str = set_name(name, player_number)
        self.round_wins: int = 0
        self.wrong_letters = []
        self.selected_word = []
        self.guessing_word = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


def set_name(name: str, player_number: int) -> str:
    """Set player name.
    
    Args:
        name (str): name entered from player. If empty, use player_number to
            default to Player 1 or 2 accordingly.
        player_number (int): use if name is empty.
    
    Returns:
        name (str): player name
    """
    if name is None or len(name) == 0:
        name = f"Player {player_number}"
    return name