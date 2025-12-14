"""Главная точка входа для запуска игры."""

import pygame

from Apple import Apple
from GameObject import GameObject
from settings import BOARD_BACKGROUND_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH, SPEED
from Snake import Snake

pygame.init()


def handle_keys(game_object: GameObject) -> None:
    """Обрабатывает все события PyGame."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        game_object.handle_keys(event)


def main() -> None:
    """Запускает главный цикл игры."""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Змейка')

    snake = Snake()
    apple = Apple(snake.positions)

    clock = pygame.time.Clock()
    highest_score = 1

    while True:
        clock.tick(SPEED)

        handle_keys(snake)
        snake.update_direction()
        snake.move()

        if snake.positions[0] == apple.position:
            snake._length += 1
            apple.randomize_position(snake.positions)
            highest_score = max(highest_score, snake._length)
            pygame.display.set_caption(f'Змейка — рекорд {highest_score}')

        if snake.collision:
            snake.reset()
            apple.randomize_position(snake.positions)

        screen.fill(BOARD_BACKGROUND_COLOR)
        apple.draw(screen)
        snake.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
