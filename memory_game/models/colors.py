from enum import Enum
from pygame import Color

class Colors(Enum):
    """Enum: Possible Colors."""

    BLACK = Color(0, 0, 0)
    GRAY = Color(100, 100, 100)
    NAVYBLUE = Color(60, 60, 100)
    WHITE = Color(255, 255, 255)
    RED = Color(255, 0, 0)
    GREEN = Color(0, 255, 0)
    BLUE = Color(0, 0, 255)
    YELLOW = Color(255, 255, 0)
    ORANGE = Color(255, 128, 0)
    PURPLE = Color(255, 0, 255)
    CYAN = Color(0, 255, 255)
