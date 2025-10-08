"""Module for logging information onto terminal."""


def info(data: str):
    """Print info data to terminal.

    Args:
        data (str): print this string data with prefix 'GAME | INFO: '.
    """
    print(f"GAME | INFO: {data}")


def error(data: str):
    """Print error message to terminal.

    Args:
        data (str): print this string data with prefix 'GAME | ERROR: '.
    """
    print(f"GAME | ERROR: {data}")


def game(data: str):
    """Print game message to terminal.

    Args:
        data (str): print this string data with prefix 'GAME | GAME: '.
    """
    print(f"GAME | GAME: {data}")
