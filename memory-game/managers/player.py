"""Managers: Player"""

from typing import List, Tuple
from pygame import (
    MOUSEBUTTONUP,
    QUIT,
    Vector2,
    event as pygame_event,
    QUIT,
    quit as pygame_quit,
    K_ESCAPE,
    KEYUP,
)
from models.players import Mouse


class PlayerManager:
    """Singleton: Player Control Center."""

    __INSTANCE = None
    __SELECTIONS = []

    def __new__(cls, name: str = "Player 1"):
        """Singleton Constructor."""

        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)
            cls.clicked = False
            cls.mouse = Mouse(0, 0)
            cls.name = name
        return cls.__INSTANCE

    @property
    def selections(self) -> List[Tuple[int, int]]:
        return self.__SELECTIONS

    @selections.setter
    def selections(self, selection: Tuple[int, int]):
        if len(self.__SELECTIONS) < 2:
            if selection:
                self.__SELECTIONS.append(selection)
        else:
            self.__SELECTIONS = []

    def poll_player_inputs(self):
        """Event Listener for User Inputs."""

        for event in pygame_event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame_quit()
                return 1
            if event.type == MOUSEBUTTONUP:
                self.mouse = Mouse(*event.pos)
                self.clicked = True
        return 0
