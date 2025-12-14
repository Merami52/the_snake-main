import random
from typing import Optional

import pygame

from GameObject import GameObject
from settings import APPLE_COLOR, BORDER_COLOR, GRID_SIZE


class Apple(GameObject):
    """Класс яблока."""

    def __init__(
        self, positions: Optional[list[tuple[int, int]]] = None
    ) -> None:
        positions = positions or []
        super().__init__(self.randomize_position(positions), APPLE_COLOR)

    def draw(self, screen: pygame.Surface) -> None:
        """Отрисовать яблоко."""
        rectangle = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rectangle)
        pygame.draw.rect(screen, BORDER_COLOR, rectangle, 1)

    def randomize_position(
        self, positions: list[tuple[int, int]]
    ) -> tuple[int, int]:
        """Случайная позиция вне змейки."""
        x = random.randrange(0, (640 // GRID_SIZE)) * GRID_SIZE
        y = random.randrange(0, (480 // GRID_SIZE)) * GRID_SIZE

        while (x, y) in positions:
            x = random.randrange(0, (640 // GRID_SIZE)) * GRID_SIZE
            y = random.randrange(0, (480 // GRID_SIZE)) * GRID_SIZE

        self.position = (x, y)
        return self.position

    def handle_keys(self, event: pygame.event.Event) -> None:
        """Яблоко не реагирует на клавиши."""
        pass
