import pygame

from GameObject import GameObject
from settings import SNAKE_COLOR, GRID_SIZE, BORDER_COLOR, BOARD_BACKGROUND_COLOR, SCREEN_HEIGHT, RIGHT, SCREEN_WIDTH, \
    LEFT, DOWN, UP


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self):
        super().__init__(self.reset(), SNAKE_COLOR)

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self._next_direction:
            self._direction, self._next_direction = self._next_direction, None

    def draw(self, screen) -> None:
        """Отрисовывает змейку на игровом поле."""
        for position in self._positions[:-1]:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Затирание последнего сегмента
        if self._length > 1:
            tail = self._positions[-1]
            last_rect = pygame.Rect(tail, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self) -> tuple[int, int]:
        """Возвращает позицию головы змейки."""
        return self._positions[0]

    def reset(self) -> tuple[int, int]:
        """Сбрасывает змейку в начальное положение."""
        position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self._positions = [position]
        self._length = 1
        self._direction = RIGHT
        self._next_direction = None
        return position

    def move(self) -> None:
        """Осуществляет движение змейки."""
        dx, dy = self._direction
        x, y = self.get_head_position()
        new_x = (x + dx * GRID_SIZE) % SCREEN_WIDTH
        new_y = (y + dy * GRID_SIZE) % SCREEN_HEIGHT
        self._positions = [(new_x, new_y)] + self._positions[:self._length]

    def handle_keys(self, event: pygame.event.Event) -> None:
        """Обрабатывает нажатия клавиш."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self._direction != DOWN:
                self._next_direction = UP
            elif event.key == pygame.K_DOWN and self._direction != UP:
                self._next_direction = DOWN
            elif event.key == pygame.K_LEFT and self._direction != RIGHT:
                self._next_direction = LEFT
            elif event.key == pygame.K_RIGHT and self._direction != LEFT:
                self._next_direction = RIGHT

    def add_node(self) -> None:
        """Добавляет новый сегмент змейки."""
        self._length += 1

    @property
    def length(self) -> int:
        """Возвращает длину змейки."""
        return self._length

    @property
    def collision(self) -> bool:
        """Возвращает True, если змейка столкнулась со своим телом."""
        return self.get_head_position() in self._positions[1:]

    @property
    def positions(self) -> list[tuple[int, int]]:
        """Возвращает список позиций змейки."""
        return self._positions

    @property
    def direction(self) -> tuple[int, int]:
        """Возвращает текущее направление движения."""
        return self._direction

    @property
    def next_direction(self) -> tuple[int, int]:
        """Возвращает следующую направление движения."""
        return self._next_direction
