import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)

# Screen dimensions
WIDTH = 600
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Game clock
clock = pygame.time.Clock()
SNAKE_SIZE = 10
SNAKE_SPEED = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Display score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, BLACK)
    SCREEN.blit(value, [0, 0])

# Snake movement
def our_snake(SNAKE_SIZE, snake_list):
    for x in snake_list:
        pygame.draw.rect(SCREEN, GREEN, [x[0], x[1], SNAKE_SIZE, SNAKE_SIZE])

# Message display
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    SCREEN.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Snake movement speed
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1

    # Random apple position
    foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0

    while not game_over:

        while game_close:
            SCREEN.fill(BLUE)
            message("You Lost! Press C-Continue or Q-Quit", RED)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_SIZE
                    x1_change = 0

        # Check if snake hits the walls
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        SCREEN.fill(BLUE)
        pygame.draw.rect(SCREEN, YELLOW, [foodx, foody, SNAKE_SIZE, SNAKE_SIZE])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if snake collides with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(SNAKE_SIZE, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Food eaten
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Run the game
gameLoop()
