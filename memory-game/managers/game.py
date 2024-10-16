"""Managers: Game"""

import time
from typing import List, Self
from pygame import (
    init as pygame_init,
    display as pygame_display,
    time as pygame_time,
    Vector2,
    font,
)
from managers.board import BoardManager
from managers.player import PlayerManager
from models.colors import Colors
from models.exceptions import GameManagerError


class GameManager:
    """Singleton: Game Control Center."""

    __INSTANCE = None
    __TITLE = "Py-Memory"
    __BACKGROUND_COLOR = Colors.BLACK
    __WINDOW_WIDTH = 640
    __WINDOW_HEIGHT = 480
    __GAME_FPS = 30
    __FPS_CLOCK = None

    def __new__(cls, board: BoardManager, player: PlayerManager) -> Self:
        """Singleton Constructor."""

        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)
            cls.board = board
            cls.player = player
            pygame_init()
            font.init()
            cls.display = pygame_display
        return cls.__INSTANCE

    @property
    def x_margin(self) -> int:
        """Getter: Left/Right Margins."""

        return int(
            (
                self.__WINDOW_WIDTH
                - (self.board.columns * (self.board.box_size + self.board.gap_size))
            )
            / 2
        )

    @property
    def y_margin(self) -> int:
        """Getter: Top/Bottom Margins."""

        return int(
            (
                self.__WINDOW_HEIGHT
                - (self.board.rows * (self.board.box_size + self.board.gap_size))
            )
            / 2
        )

    @property
    def background_color(self) -> Colors:
        """Getter: Background Color."""

        return self.__BACKGROUND_COLOR

    @background_color.setter
    def background_color(self, value):
        """Setter: Background Color."""

        if isinstance(value, Colors):
            raise GameManagerError("Invalid Background Color.")
        self.__BACKGROUND_COLOR = value

    def set_game_window(self):
        """Setup: Game Window and Surface Environment."""

        self.surface = self.display.set_mode(
            Vector2(self.__WINDOW_WIDTH, self.__WINDOW_HEIGHT)
        )
        self.display.set_caption(self.__TITLE)
        self.surface.fill(self.__BACKGROUND_COLOR.value)

    def start_game(self):
        """Invokes Game Loop."""

        self.__FPS_CLOCK = pygame_time.Clock()
        self.set_game_window()
        self.board.draw_board(self.surface, self.x_margin, self.y_margin)
        self.__loop()

    def __loop(self):
        """Private: Game Loop."""

        while True:
            if self.player.poll_player_inputs() != 0:
                break

            if self.player.clicked:
                selection = self.board.box_collision(self.player.mouse)
                self.player.selections = selection
                self.player.clicked = False
                self.board.draw_board(self.surface, self.x_margin, self.y_margin)

                if len(self.player.selections) == 2:
                    self.evaluate_selections()
                    self.player.selections = []

            self.display.update()
            self.__FPS_CLOCK.tick(self.__GAME_FPS)

    def evaluate_selections(self):
        if len(self.player.selections) == 2:
            selection1, selection2 = self.player.selections
            x1, y1 = selection1[0], selection1[1]
            x2, y2 = selection2[0], selection2[1]
            if self.board.board[x1][y1] != self.board.board[x2][y2]:
                self.board.state[x1][y1] = False
                self.board.state[x2][y2] = False
