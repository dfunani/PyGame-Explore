from managers.game import GameManager
from managers.board import BoardManager
from managers.player import PlayerManager
from unittest.mock import patch


def test_board_manager():
    board_manager = BoardManager()
    assert len(board_manager.generate_board(4, 4)) == 4
    assert len(board_manager.generate_board(4, 4)[0]) == 4


def test_game_manager():
    with patch("managers.game.time") as mock_time:
        mock_time.time.return_value = 10
        game_manager = GameManager(None, None)
        result = game_manager.track_time(5)
        assert result == 5


def test_player_manager():
    player_manager = PlayerManager()
    player_manager.clicked = True
    assert player_manager.clicked == True
