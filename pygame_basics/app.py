"""Basic PyGame Window Session"""

from abc import ABC, abstractmethod
from enum import Enum
import os
import sys
from time import sleep
from typing import List, NamedTuple, Tuple
from pygame import (
    init as pygame_init,
    display,
    event,
    quit,
    Rect,
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
    draw,
    PixelArray,
    image,
    font,
    mixer,
)
from pygame.locals import QUIT

# class SoundManager:
#     def __init__(self, sound_file: str) -> None:
#         if not os.path.exists(sound_file):
#             raise FileNotFoundError("Sound File Not Found")
#         self.sound_file = sound_file


class WindowSize(NamedTuple):
    width: int
    height: int


class Coordinate(NamedTuple):
    x: int
    y: int


class Primitive(ABC):
    @abstractmethod
    def draw(self):
        pass


class Line(Primitive):
    def __init__(
        self, starting_point: Coordinate, endpoint_point: Coordinate, thickness: int = 1
    ) -> None:
        self.starting_point = starting_point
        self.endpoint_point = endpoint_point
        self.thickness = thickness

    def draw(self):
        return (self.starting_point, self.endpoint_point, self.thickness)


class Circle(Primitive):
    def __init__(
        self, centre_point: Coordinate, radius: int, thickness: int = 1
    ) -> None:
        self.centre_point = centre_point
        self.radius = radius
        self.thickness = thickness

    def draw(self):
        return (self.centre_point, self.radius, self.thickness)


class Rectangle(Primitive):
    def __init__(
        self, x: float, y: float, width: float, height: float, thickness: int = 0
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.thickness = thickness

    def draw(self):
        return (Rect(self.x, self.y, self.width, self.height), self.thickness)


class Polygon(Primitive):
    def __init__(self, points: List[Coordinate], width: int = 0) -> None:
        self.points = points
        self.width = width

    def draw(self):
        return (self.points, self.width)


class RGB(Enum):
    AQUA = (0, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    FUCHSIA = (255, 0, 255)
    GRAY = (128, 128, 128)
    GREEN = (0, 128, 0)
    LIME = (0, 255, 0)
    MAROON = (128, 0, 0)
    NAVYBLUE = (0, 0, 128)
    OLIVE = (128, 128, 0)
    PURPLE = (128, 0, 128)
    RED = (255, 0, 0)
    SILVER = (192, 192, 192)
    TEAL = (0, 128, 128)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)


class GameManager:
    """ "Singleton: Game Manager"""

    def __init__(
        self,
        window_size: WindowSize = WindowSize(0, 0),
        title: str = "Unknown Window",
        background: RGB | Tuple[int, int, int, int] = RGB.BLACK,
    ) -> None:
        self.display = display
        self.window_size = window_size
        self.title = title

        if isinstance(background, RGB):
            background = background.value
        self.background = background

        self.set_game_window()
        self.pygame_state = pygame_init()

    def set_game_window(self) -> int:
        self.surface = self.display.set_mode(self.window_size)
        self.display.set_caption(self.title)
        self.frame_reset()
        return 0

    def frame_reset(self):
        self.surface.fill(self.background)

    def game_loop(self) -> int:
        start_x = 90
        start_y = 390
        flip = False

        while True:
            self.frame_reset()
            for exec in event.get():
                if exec.type == QUIT or (exec.type == KEYDOWN and exec.key == K_ESCAPE):
                    quit()
                    return 1
                if exec.type == KEYDOWN and exec.key == K_RETURN:
                    mixer.music.load("flap.wav")
                    mixer.music.play(0, 0, 0)
            draw.rect(
                self.surface, RGB.AQUA.value, *Rectangle(200, 150, 100, 50).draw()
            )
            draw.line(
                self.surface,
                RGB.LIME.value,
                *Line(Coordinate(60, 60), Coordinate(120, 60), 6).draw()
            )
            draw.circle(
                self.surface,
                RGB.MAROON.value,
                *Circle(Coordinate(300, 50), 50, 15).draw()
            )
            draw.ellipse(
                self.surface, RGB.FUCHSIA.value, *Rectangle(300, 250, 40, 80, 1).draw()
            )
            draw.polygon(
                self.surface,
                RGB.WHITE.value,
                *Polygon(
                    ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)), 0
                ).draw()
            )
            pixObj = PixelArray(self.surface)
            pixObj[80][380] = RGB.RED.value
            pixObj[82][382] = RGB.RED.value
            pixObj[84][384] = RGB.RED.value
            pixObj[86][386] = RGB.RED.value
            pixObj[88][388] = RGB.RED.value
            del pixObj

            self.surface.blit(image.load("cat.png"), Coordinate(start_x, start_y))
            text = font.Font("freesansbold.ttf", 32).render(
                "Hello World!", True, RGB.PURPLE.value, RGB.WHITE.value
            )
            text_center = text.get_rect()
            text_center.center = (960, 450)
            self.surface.blit(text, text_center)
            if start_x >= int(self.surface.get_width() / 2):
                flip = True
            elif start_x <= 80:
                flip = False

            if flip:
                start_x -= 1
            else:
                start_x += 1

            # beep = mixer.Sound("flap.wav")
            # beep.play()
            # sleep(1)
            # beep.stop()

            self.display.update()


def main() -> int:
    print(GameManager().game_loop())
    return 0


if __name__ == "__main__":
    main()
