
"""
Prompt: Create a Snake game in Python where the snake eats a block placed  randomly inside a square. 
After capturing the block, the snake's size  should increase by one, and each new block should appear in a different  color.
"""

import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
snake_color = (0, 255, 0)  # Green
background_color = (0, 0, 0)  # Black
block_colors = [
    (255, 0, 0),   # Red
    (0, 0, 255),   # Blue
    (255, 255, 0), # Yellow
    (255, 165, 0), # Orange
    (128, 0, 128)  # Purple
]

# Game settings
snake_block_size = 20
snake_speed = 10

# Initialize clock
clock = pygame.time.Clock()

# Snake initialization
snake = [(100, 100)]
snake_direction = 'RIGHT'

# Random block (food) initialization
block_pos = [random.randrange(0, width // snake_block_size) * snake_block_size,
             random.randrange(0, height // snake_block_size) * snake_block_size]
block_color = random.choice(block_colors)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, snake_color, [block[0], block[1], snake_block_size, snake_block_size])

def game_loop():
    global snake_direction, block_pos, block_color

    game_over = False
    x, y = snake[0]  # Snake head position
    dx, dy = 0, 0  # Snake movement

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Change direction with arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                    dx, dy = -snake_block_size, 0
                    snake_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                    dx, dy = snake_block_size, 0
                    snake_direction = 'RIGHT'
                elif event.key == pygame.K_UP and snake_direction != 'DOWN':
                    dx, dy = 0, -snake_block_size
                    snake_direction = 'UP'
                elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                    dx, dy = 0, snake_block_size
                    snake_direction = 'DOWN'

        # Move the snake
        x += dx
        y += dy

        # Snake boundary collision
        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        # Check if snake collides with itself
        if [x, y] in snake[1:]:
            game_over = True

        # Add new head to the snake
        snake.insert(0, [x, y])

        # Check if snake eats the block
        if x == block_pos[0] and y == block_pos[1]:
            # Generate a new block with a different color
            block_pos = [random.randrange(0, width // snake_block_size) * snake_block_size,
                         random.randrange(0, height // snake_block_size) * snake_block_size]
            block_color = random.choice(block_colors)
        else:
            # Remove the tail if block is not eaten
            snake.pop()

        # Fill the background
        screen.fill(background_color)

        # Draw the snake
        draw_snake(snake)

        # Draw the block (food)
        pygame.draw.rect(screen, block_color, [block_pos[0], block_pos[1], snake_block_size, snake_block_size])

        # Update the screen
        pygame.display.update()

        # Control the speed of the snake
        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
