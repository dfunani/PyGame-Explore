"""Application: Main"""

from managers.board import BoardManager
from managers.game import GameManager
from managers.player import PlayerManager


def main():
    """Game Ingress Point."""

    # Create Player and Game Board.
    player = PlayerManager()
    board = BoardManager()

    # Start Game Loop
    game = GameManager(board=board, player=player)
    game.start_game()


if __name__ == "__main__":
    main()
