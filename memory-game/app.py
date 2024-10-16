"""Application: Main"""

from time import sleep
from managers.board import BoardManager
from managers.game import GameManager, GameStates
from managers.player import PlayerManager
from pygame import Rect, font, quit as pygame_quit

from models.colors import Colors


def main():
    """Game Ingress Point."""

    # Create Player and Game Board.
    player = PlayerManager()
    board = BoardManager()

    # Start Game Loop
    game = GameManager(board=board, player=player)
    result = game.start_game()
    match result:
        case GameStates.WINNER:
            text = f"{player.name}: {result.value}"
        case GameStates.LOSER:
            text = f"{player.name}: {result.value}"
        case result:
            text = result.value
    game.render_result(text)
    return text


if __name__ == "__main__":
    response = main()
    print(response)
