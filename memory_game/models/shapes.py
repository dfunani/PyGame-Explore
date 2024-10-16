from enum import Enum
from random import shuffle
from typing import List


class Shapes(Enum):
    """Enum: Possible Shapes."""

    BLUE_CIRCLE = "🔵"
    RED_CIRCLE = "🔴"
    GREEN_CIRCLE = "🟢"
    YELLOW_CIRCLE = "🟡"
    PURPLE_CIRCLE = "🟣"
    ORANGE_CIRCLE = "🟠"

    RED_SQUARE = "🟥"
    GREEN_SQUARE = "🟩"
    YELLOW_SQUARE = "🟨"
    BLUE_SQUARE = "🟦"
    PINK_SQUARE = "🟪"
    ORANGE_SQUARE = "🟧"

    IN_LOVE_EMOJI = "😍"
    CONFUSED_EMOJI = "🤔"
    HUG_EMOJI = "🤗"
    HAPPY_EMOJI = "🙂"
    SAD_EMOJI = "😒"
    LAUGHING_EMOJI = "🤣"

    PINK_HEART = "🩷"
    PURPLE_HEART = "💜"
    BLUE_HEART = "💙"
    YELLOW_HEART = "💛"
    GREEN_HEART = "💚"
    ORANGE_HEART = "🧡"

    WATERMELON = "🍉"
    APPLE = "🍎"
    BANANA = "🍌"
    ORANGE = "🍊"
    PEAR = "🍐"
    PINEAPPLE = "🍍"

    STAR = "⭐"
    PIN = "📌"
    DICE = "🎲"
    ROCKET = "🚀"
    RAINBOW = "🌈"
    WALL = "🧱"
    FIRE = "🔥"
    EARTH = "🌎"
    PHONE = "📞"
    FLAG = "🚩"
    DROPLET = "💧"
    HAMMER = "🔨"
