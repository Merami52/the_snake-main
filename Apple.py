from GameObject import GameObject
import pygame
from settings import GRID_SIZE, BORDER_COLOR, APPLE_COLOR, GRID_WIDTH, GRID_HEIGHT
import random
import typing as tp


class Apple(GameObject):
    """Класс яблока."""

    def __init__(self, positions: tp.Optional[list[tuple[int, int]]] = None):
        positions = positions or []
        super().__init__(self.randomize_position(positions), APPLE_COLOR)

    def draw(self, screen) -> None:
        """Отрисовывает яблоко на игровом поле."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

    def randomize_position(
            self,
            positions: list[tuple[int, int]],
    ) -> tuple[int, int]:
        """Возвращает случайную позицию на игровом поле."""
        x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
        y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        while (x, y) in positions:
            x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
            y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        self.position = (x, y)
        return self.position

    def handle_keys(self, event: pygame.event.Event) -> None:
        """Обрабатывает нажатия клавиш."""
        pass
