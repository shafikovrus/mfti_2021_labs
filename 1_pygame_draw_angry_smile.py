# Import a library of functions called 'pygame'
import pygame
from math import pi

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


# Define functions drawing elements
def big_circle_face(x, y):
    pygame.draw.circle(screen, YELLOW, [x, y], 190.00, width=0)


def eyebrow_left(x, y):
    pygame.draw.line(screen, BLACK, [x, y], [x + 60, y + 40], width=8)


def eyebrow_right(x, y):
    pygame.draw.line(screen, BLACK, [x, y], [x - 60, y + 40], width=8)


def small_circle_eye(x, y):
    pygame.draw.circle(screen, WHITE, [x, y], 40.00, width=0)
    pygame.draw.polygon(screen, BLACK, [[x - 5, y - 10], [x + 5, y - 10], [x + 5, y + 10], [x - 5, y + 10]])


def nose(x, y):
    pygame.draw.line(screen, BLACK, [x, y - 60], [x - 30, y + 30], width=4)
    pygame.draw.line(screen, BLACK, [x - 30, y + 30], [x, y + 30], width=4)


def mouth(x, y):
    pygame.draw.ellipse(screen, BLACK, [x - 100, y + 20, 200, 80])
    pygame.draw.ellipse(screen, YELLOW, [x - 100, y + 60, 200, 40])


# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Angry smile")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    screen.fill(BLACK)
    big_circle_face(200, 200)
    small_circle_eye(110, 170)
    eyebrow_left(85, 100)
    small_circle_eye(290, 170)
    eyebrow_right(315, 100)
    nose(200, 230)
    mouth(200, 260)
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
