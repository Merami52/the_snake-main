import pygame

from Apple import Apple
from GameObject import GameObject
from Snake import Snake
from settings import *

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


def handle_keys(game_object: GameObject):
    """Обработка событий клавиатуры."""
    for event in pygame.event.get():
        esc_quit_cond = (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
        )
        if event.type == pygame.QUIT or esc_quit_cond:
            pygame.quit()
            raise SystemExit
        game_object.handle_keys(event)


def main():
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    snake = Snake()
    apple = Apple(snake.positions)
    max_len = 1

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()
        snake.move()
        if snake.get_head_position() == apple.position:
            snake.add_node()
            apple.randomize_position(snake.positions)
            max_len = max(max_len, snake.length)
            pygame.display.set_caption(f'Змейка - рекорд {max_len}')
        elif snake.collision:
            snake.reset()
            apple.randomize_position(snake.positions)

        screen.fill(BOARD_BACKGROUND_COLOR)
        apple.draw(screen)
        snake.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()


# Метод draw класса Apple


# Метод draw класса Snake
def draw(self):
    for position in self.positions[:-1]:
        rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

    # Отрисовка головы змейки
    head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, self.body_color, head_rect)
    pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

    # Затирание последнего сегмента
    if self.last:
        last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)


def handle_keys(game_object):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def update_direction(self):
    if self.next_direction:
        self.direction = self.next_direction
        self.next_direction = None
