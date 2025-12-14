import pygame

from GameObject import GameObject
from settings import (BOARD_BACKGROUND_COLOR, BORDER_COLOR, DOWN, GRID_SIZE,
                      LEFT, RIGHT, SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_COLOR,
                      UP)


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self) -> None:
        super().__init__(self.reset(), SNAKE_COLOR)

    def update_direction(self) -> None:
        """Обновляет направление движения змейки."""
        if self._next_direction:
            self._direction, self._next_direction = (
                self._next_direction,
                None,
            )

    def draw(self, screen: pygame.Surface) -> None:
        """Отрисовывает змейку."""
        for position in self._positions[:-1]:
            rectangle = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rectangle)
            pygame.draw.rect(screen, BORDER_COLOR, rectangle, 1)

        if self._length > 1:
            tail = self._positions[-1]
            tail_rectangle = pygame.Rect(tail, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(
                screen,
                BOARD_BACKGROUND_COLOR,
                tail_rectangle,
            )

    def reset(self) -> tuple[int, int]:
        """Сбрасывает змейку."""
        start_x = SCREEN_WIDTH // 2
        start_y = SCREEN_HEIGHT // 2
        start_position = (start_x, start_y)

        self._positions = [start_position]
        self._length = 1
        self._direction = RIGHT
        self._next_direction = None

        return start_position

    def move(self) -> None:
        """Двигает змейку на одну клетку."""
        dx, dy = self._direction
        head_x, head_y = self._positions[0]
        new_x = (head_x + dx * GRID_SIZE) % SCREEN_WIDTH
        new_y = (head_y + dy * GRID_SIZE) % SCREEN_HEIGHT

        self._positions = [(new_x, new_y)] + self._positions[: self._length]

    def handle_keys(self, event: pygame.event.Event) -> None:
        """Устанавливает направление по клавише."""
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP and self._direction != DOWN:
            self._next_direction = UP
        elif event.key == pygame.K_DOWN and self._direction != UP:
            self._next_direction = DOWN
        elif event.key == pygame.K_LEFT and self._direction != RIGHT:
            self._next_direction = LEFT
        elif event.key == pygame.K_RIGHT and self._direction != LEFT:
            self._next_direction = RIGHT

    @property
    def collision(self) -> bool:
        """Столкновение змейки с её телом."""
        return self._positions[0] in self._positions[1:]

    @property
    def positions(self) -> list[tuple[int, int]]:
        """Возвращает позиции змейки."""
        return self._positions
