"""Main module."""
from src.game import Game, start_game

def main():
    """Start the game."""
    game = Game()
    start_game(game)

if __name__ == "__main__":
    main()
