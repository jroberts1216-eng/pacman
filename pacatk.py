import pygame
import random
import sys
import os

os.environ["SDL_AUDIODRIVER"] = "dummy"
# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Pac-Man")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Pac-Man setup
pacman_pos = [300, 300]
pacman_radius = 20
pacman_speed = 5

# Dots
dots = [[random.randint(20, 580), random.randint(20, 580)] for _ in range(30)]

# Score
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw_pacman(pos):
    pygame.draw.circle(screen, YELLOW, pos, pacman_radius)

def draw_dots():
    for dot in dots:
        pygame.draw.circle(screen, WHITE, dot, 5)

def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_pos[0] -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_pos[0] += pacman_speed
    if keys[pygame.K_UP]:
        pacman_pos[1] -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_pos[1] += pacman_speed

    # Dot collision
    for dot in dots[:]:
        if pygame.Rect(pacman_pos[0]-pacman_radius, pacman_pos[1]-pacman_radius, 40, 40).collidepoint(dot):
            dots.remove(dot)
            score += 1

    draw_dots()
    draw_pacman(pacman_pos)
    show_score()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
