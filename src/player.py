"""Module for player logic."""

class Player:
    """Player class for handling the players."""
    def __init__(self, name: str, player_number: int):
        self.name = set_name(name, player_number)


def set_name(name: str, player_number: int):
    if name is None:
        name = f"Player {player_number}"

    return name