"""Module for logging information onto terminal."""


def info(data: str):
    """Print info data to terminal.

    Args:
        data (str): print this string data with prefix 'GAME | INFO: '.
    """
    print(f"GAME | INFO: {data}")


def error(data: str):
    """Print error msg to terminal.

    Args:
        data (str): print this string data with prefix 'GAME | ERROR: '.
    """
    print(f"GAME | ERROR: {data}")
