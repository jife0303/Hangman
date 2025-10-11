"""Module for logging information onto terminal.

info(): add 'GAME | INFO: ' before the given data.
error(): add 'GAME | ERROR: ' before the given data.
play(): add 'GAME | PLAY: ' before the given data.
"""


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


def play(data: str):
    """Print game message to terminal.

    Args:
        data (str): print this string data with prefix 'GAME | PLAY: '.
    """
    print(f"GAME | PLAY: {data}")
