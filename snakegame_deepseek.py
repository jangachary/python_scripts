
"""
Prompt: Create a Snake game in Python where the snake eats a block placed  randomly inside a square. 
After capturing the block, the snake's size  should increase by one, and each new block should appear in a different  color.
"""


import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [RED, GREEN, BLUE]

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Snake and food
snake = [(100, 100), (80, 100), (60, 100)]
snake_direction = (BLOCK_SIZE, 0)
food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
food_color = random.choice(COLORS)

# Score
score = 0

# Function to draw the snake
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

# Function to draw the food
def draw_food(food, color):
    pygame.draw.rect(screen, color, (*food, BLOCK_SIZE, BLOCK_SIZE))

# Function to check collision
def check_collision(snake):
    head = snake[0]
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    for segment in snake[1:]:
        if head == segment:
            return True
    return False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, BLOCK_SIZE):
                snake_direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -BLOCK_SIZE):
                snake_direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and snake_direction != (BLOCK_SIZE, 0):
                snake_direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-BLOCK_SIZE, 0):
                snake_direction = (BLOCK_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # Check if the snake eats the food
    if snake[0] == food:
        score += 1
        food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
        food_color = random.choice(COLORS)
    else:
        snake.pop()

    # Check for collision
    if check_collision(snake):
        running = False

    # Draw everything
    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food, food_color)

    # Display score
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the speed of the game
    clock.tick(10)

# Quit pygame
pygame.quit()