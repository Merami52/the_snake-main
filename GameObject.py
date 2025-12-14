import pygame
import typing as tp
from abc import ABC, abstractmethod


class GameObject(ABC):
    """Абстрактный игровой объект."""

    def __init__(
        self,
        position: tp.Optional[tuple[int, int]] = None,
        body_color: tp.Optional[tuple[int, int, int]] = None,
    ) -> None:
        self.position = position or (0, 0)
        self.body_color = body_color or (0, 0, 0)

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        """Рисует объект."""
        pass

    @abstractmethod
    def handle_keys(self, event: pygame.event.Event) -> None:
        """Обрабатывает нажатия клавиш."""
        pass
