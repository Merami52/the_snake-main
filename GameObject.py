from abc import abstractmethod, ABC
import typing as tp

import pygame


class GameObject(ABC):
    def __init__(
            self,
            position: tp.Optional[tuple[int, int]] = None,
            body_color: tp.Optional[tuple[int, int, int]] = None,
    ):
        self.position = position or (0, 0)
        self.body_color = body_color or (0, 0, 0)

    @abstractmethod
    def draw(self, screen=None):
        pass

    @abstractmethod
    def handle_keys(self, event: pygame.event.Event) -> None:
        """Обрабатывает нажатия клавиш."""
        pass
