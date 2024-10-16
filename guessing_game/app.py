from random import randint
from time import sleep
from typing import Tuple
from pygame import (
    K_0,
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
    x: int = 176
    y: int = 200


class GameManager:
    __WINDOW_SIZE = Size()
    __INPUT_BOX_SIZE = Size(width=360, height=80)
    __INPUT_BOX_POS = Position()
    __TRIES = 5

    def __init__(self, title: str = "Unknown Window") -> None:
        self.display = display
        self.title = title
        self.create_window_context()
        pygame_init()

    @property
    def tries(self):
        return self.__TRIES

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


def poll_event_keys(player: "Player") -> int:
    for entry in event.get():
        if entry.type == QUIT or (entry.type == KEYUP and entry.key == K_ESCAPE):
            quit()
            return 1

        if entry.type == KEYUP:
            if entry.key == K_RETURN:
                if player.guessing:
                    player.play()
                player.guess = ""
                player.game.surface.fill((0, 0, 0))
            elif entry.key in (K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0):
                player.update(entry.unicode)
            elif entry.key == K_BACKSPACE:
                player.update(None)
                player.game.surface.fill((0, 0, 0))
    return 0


class GameOverError(Exception):
    pass


class Player:
    def __init__(self, game: GameManager) -> None:
        self.guess = ""
        self.title = "Guess a Number between 0 and 20!"
        self.tries = 0
        self.__random_number = randint(0, 20)
        self.__game = game
        self.guessing = False

    @property
    def game(self) -> GameManager:
        return self.__game

    def update(self, guess: int):
        self.guessing = True
        if guess is None:
            self.guess = self.guess[0:-1]
        elif self.tries == self.game.tries:
            self.guess = ""
            self.title = "You Lose! No More Tries Left."
        else:
            self.guess += guess

    def play(self):
        self.guessing = False
        if self.tries == self.game.tries:
            self.title = "You Lose! No More Tries Left."
            return False

        self.tries += 1
        if int(self.guess) == self.__random_number:
            self.title = f"You Win! Guessed {int(self.guess)} Correctly in {self.tries}"
            self.tries = self.game.tries

        if int(self.guess) > self.__random_number:
            self.title = f"Guess {self.tries} Too High!"

        if int(self.guess) < self.__random_number:
            self.title = f"Guess {self.tries} Too Low!"
        return True


def main():
    game_manager = GameManager()
    player = Player(game_manager)

    while True:
        if poll_event_keys(player) != 0:
            return player.title

        title = font.Font(None, 42).render(player.title, True, (255, 255, 255))
        guess = font.Font(None, 64).render(player.guess, True, (255, 255, 255))
        game_manager.surface.blit(
            title,
            (
                game_manager.input_box_pos.x - 100,
                game_manager.input_box_pos.y - 20,
            ),
        )
        game_manager.surface.blit(
            guess,
            (
                game_manager.input_box_pos.x,
                game_manager.input_box_pos.y,
            ),
        )
        game_manager.display.flip()
        if player.tries == game_manager.tries:
            sleep(10)
            quit()
            return player.title
        time.Clock().tick(30)


if __name__ == "__main__":
    logger.info(main())
