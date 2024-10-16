"""Managers: Board"""

from random import shuffle, choice
from typing import List, Tuple
from pygame import (
    Rect,
    Surface,
    Vector2,
    draw as pygame_draw,
)
from pygame_emojis import load_emoji
from models.colors import Colors
from models.exceptions import ShapeGeneratorError
from models.players import Mouse
from models.shapes import Shapes


class BoardManager:
    """Factory: Manages Board Design."""

    __ROWS = 7
    __COLUMNS = 10
    __BOX_SIZE = 40
    __GAP_SIZE = 10
    __BOX_COLOR = choice(list(Colors))

    def __init__(self):
        """Factory Constructor."""

        self.board = self.generate_board(self.__ROWS, self.__COLUMNS)
        self.state = [[False for _ in row] for row in self.board]
        self.boxes = [[Rect(0, 0, 0, 0) for _ in row] for row in self.board]

    @property
    def columns(self) -> int:
        """Getter: Number of Board Columns."""

        return self.__COLUMNS

    @property
    def rows(self) -> int:
        """Getter: Number of Board Rows."""

        return self.__ROWS

    @property
    def box_size(self) -> int:
        """Getter: Square Icon Cover Size (box-size x box-size)."""

        return self.__BOX_SIZE

    @property
    def gap_size(self) -> int:
        """Getter: Gaps Between Square Icon Covers."""

        return self.__GAP_SIZE

    def generate_board(self, rows: int, columns: int) -> List[List[Shapes]]:
        """Factory Method: Creates Game Board as a Nested List of Shapes."""

        board = []
        number_of_shapes = int((rows * columns) / 2)
        shapes = self.generate_shapes(number_of_shapes) * 2
        for _ in range(rows):
            board.append([s for s in shapes[:columns]])
            shapes = shapes[columns:]
        return board

    def generate_shapes(self, count: int) -> List[Shapes]:
        """Factory Method: Generates Game Board Shapes."""

        if not isinstance(count, int):
            raise ShapeGeneratorError("Count Argument Must Be Integer.")

        shapes = list(Shapes)

        if count > len(shapes):
            raise ShapeGeneratorError(
                f"Can Not Generate that Many Shapes. Max: {len(shapes)}."
            )

        shuffle(shapes)
        return shapes[:count]

    def draw_board(self, surface: Surface, x_margin: int, y_margin: int):
        """Draws the Board Based on the Current Board State."""

        x = x_margin
        y = y_margin
        for row in range(self.__ROWS):
            for column in range(self.__COLUMNS):
                box = Rect(x, y, self.__BOX_SIZE, self.__BOX_SIZE)
                self.boxes[row][column] = box
                if not self.state[row][column]:
                    pygame_draw.rect(
                        surface,
                        self.__BOX_COLOR.value,
                        box,
                    )
                else:
                    text_surface = load_emoji(
                        self.board[row][column].value,
                        (self.__BOX_SIZE, self.__BOX_SIZE),
                    )
                    surface.blit(text_surface, box)

                x += self.__BOX_SIZE + self.__GAP_SIZE
            x = x_margin
            y += self.__BOX_SIZE + self.__GAP_SIZE

    def box_collision(self, mouse: Mouse) -> Tuple[int, int]:
        for row in range(self.__ROWS):
            for column in range(self.__COLUMNS):
                if self.boxes[row][column].collidepoint(mouse.x, mouse.y):
                    self.state[row][column] = True
                    return (row, column)
        return ()
