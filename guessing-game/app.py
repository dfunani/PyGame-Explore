from random import randint
from typing import Tuple
from pygame import (
    display,
    init as pygame_init,
    event,
    quit,
    QUIT,
    KEYUP,
    KEYDOWN,
    K_ESCAPE,
    K_BACKSPACE,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_7,
    K_8,
    K_9,
    K_RETURN,
    time,
    draw,
    Color,
    Rect,
    key,
    font,
)
from pyinputplus import inputInt
from logging import basicConfig, getLogger, BASIC_FORMAT, DEBUG
from pydantic import BaseModel

logger = getLogger(__name__)
basicConfig(level=DEBUG, format=BASIC_FORMAT)
ALLOWED_GUESSES = 5


class Size(BaseModel):
    width: int = 640
    height: int = 480


class Position(BaseModel):
    x: int = 240
    y: int = 200


class GameManager:
    __WINDOW_SIZE = Size()
    __INPUT_BOX_SIZE = Size(width=160, height=80)
    __INPUT_BOX_POS = Position()

    def __init__(self, title: str = "Unknown Window") -> None:
        self.display = display
        self.title = title
        self.create_window_context()
        pygame_init()

    @property
    def window_size(self) -> Size:
        return self.__WINDOW_SIZE

    @property
    def input_box_size(self) -> Size:
        return self.__INPUT_BOX_SIZE

    @property
    def input_box_pos(self) -> Position:
        return self.__INPUT_BOX_POS

    def create_window_context(self):
        self.surface = self.display.set_mode(
            (self.__WINDOW_SIZE.width, self.__WINDOW_SIZE.height)
        )
        self.display.set_caption(self.title)


def game_logic():
    game_over = False
    random_number = randint(0, 20)
    guesses = 0
    while not game_over:
        guess = inputInt("Enter Guess: ")
        guesses += 1
        if guess == random_number:
            game_over = True

        if guess > random_number:
            logger.info(f"Guess {guesses} Too High!")

        if guess < random_number:
            logger.info(f"Guess {guesses} Too Low!")

        if guesses == ALLOWED_GUESSES:
            game_over = True


def poll_event_keys(player: "Player") -> int:
    for entry in event.get():
        if entry.type == QUIT or (entry.type == KEYUP and entry.key == K_ESCAPE):
            quit()
            return 1

        if entry.type == KEYUP:
            if entry.key == K_RETURN:
                player.play()
            elif entry.key in (K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9):
                player.update(entry.unicode)
            elif entry.key == K_BACKSPACE:
                player.update(None)

    return 0


class GameOverError(Exception):
    pass


class Player:
    def __init__(self) -> None:
        self.guess = ""
        self.tries = 5

    def update(self, guess: int):
        if guess is None:
            self.guess = self.guess[0:-1]
        self.guess += guess

    def play(self):
        if self.tries == 0:
            raise GameOverError("No More Tries Left.")
        self.tries += 1


def main():
    game_manager = GameManager()
    player = Player()
    draw.rect(
        game_manager.surface,
        Color(255, 0, 0, 255),
        Rect(
            game_manager.input_box_pos.x,
            game_manager.input_box_pos.y,
            game_manager.input_box_size.width,
            game_manager.input_box_size.height,
        ),
    )
    while True:
        if poll_event_keys(player) != 0:
            return 1
        text = font.Font(None, 18).render(player.guess, True, (255, 255, 255))
        game_manager.surface.blit(
            text,
            (
                game_manager.input_box_pos.x,
                game_manager.input_box_pos.y,
            ),
        )
        game_manager.display.flip()
        time.Clock().tick(30)


if __name__ == "__main__":
    logger.info(main())
