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
    pygame.draw.line(screen, BLACK, [x, y], [x+60, y+40], width=8)


def eyebrow_right(x, y):
    pygame.draw.line(screen, BLACK, [x, y], [x-60, y+40], width=8)


def small_circle_eye(x, y):
    pygame.draw.circle(screen, WHITE, [x, y], 40.00, width=0)
    pygame.draw.polygon(screen, BLACK, [[x-5, y-10], [x+5, y-10], [x+5, y+10], [x-5, y+10]])


def nose(x, y):
    pygame.draw.line(screen, BLACK, [x, y-60], [x-30, y+30], width=4)
    pygame.draw.line(screen, BLACK, [x-30, y+30], [x, y+30], width=4)

def mouth(x, y):
    pygame.draw.ellipse(screen, BLACK, [x-100, y+20, 200, 80])
    pygame.draw.ellipse(screen, YELLOW, [x-100, y+60, 200, 40])




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

"""
    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Draw on the screen a GREEN line from (0, 0) to (50, 30)
    # 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [50, 30], 5)

    # Draw on the screen 3 BLACK lines, each 5 pixels wide.
    # The 'False' means the first and last points are not connected.
    pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)

    # Draw on the screen a GREEN line from (0, 50) to (50, 80)
    # Because it is an antialiased line, it is 1 pixel wide.
    pygame.draw.aaline(screen, GREEN, [0, 50], [50, 80], True)

    # Draw a rectangle outline
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)

    # Draw a solid rectangle
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

    # Draw a rectangle with rounded corners
    pygame.draw.rect(screen, GREEN, [115, 210, 70, 40], 10, border_radius=15)
    pygame.draw.rect(screen, RED, [135, 260, 50, 30], 0, border_radius=10, border_top_left_radius=0,
                     border_bottom_right_radius=15)

    # Draw an ellipse outline, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)

    # Draw an solid ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLACK, [210, 75, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, GREEN, [210, 75, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi, 3 * pi / 2, 2)
    pygame.draw.arc(screen, RED, [210, 75, 150, 125], 3 * pi / 2, 2 * pi, 2)

    # Draw a circle
    pygame.draw.circle(screen, BLUE, [60, 250], 40)

    # Draw only one circle quadrant
    pygame.draw.circle(screen, BLUE, [250, 250], 40, 0, draw_top_right=True)
    pygame.draw.circle(screen, RED, [250, 250], 40, 30, draw_top_left=True)
    pygame.draw.circle(screen, GREEN, [250, 250], 40, 20, draw_bottom_left=True)
    pygame.draw.circle(screen, BLACK, [250, 250], 40, 10, draw_bottom_right=True)
"""

# Be IDLE friendly
pygame.quit()
