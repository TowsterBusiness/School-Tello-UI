# importing
from Tello.tello import *
import pygame

# starting the Tello interface
start()
power = get_battery()
print("Power Level: ", power, "%")
takeoff()

# getting the controlls from pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    QUIT,
)

# calculates if the x y is in cx cy with r radius
def inside_circle(x, y, cx, cy, r):
    if cx - r < x < cx + r and cy - r < y < cy + r:
        return True
    return False


# initializes pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

button_clicked = -1

game_state = 0
# makes the buttons red when the drone is still moving
is_moving = False

drone_speed = 100

# this is the color of the buttons
BLUE = (92, 154, 255)
RED = (255, 115, 99)

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            # Use this elif for any keystrokes
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]

            if inside_circle(mouse_x, mouse_y, 250, 50, 40):
                button_clicked = 1
            if inside_circle(mouse_x, mouse_y, 250, 200, 40):
                button_clicked = 2
            if inside_circle(mouse_x, mouse_y, 150, 125, 40):
                button_clicked = 3
            if inside_circle(mouse_x, mouse_y, 350, 125, 40):
                button_clicked = 4
            if inside_circle(mouse_x, mouse_y, 400, 300, 40):
                button_clicked = 5
            if inside_circle(mouse_x, mouse_y, 400, 400, 40):
                button_clicked = 6
            if inside_circle(mouse_x, mouse_y, 100, 300, 40):
                button_clicked = 7
            if inside_circle(mouse_x, mouse_y, 100, 400, 40):
                button_clicked = 8
        elif event.type == MOUSEBUTTONUP:
            button_clicked = -1

    screen.fill((40, 40, 40))

    # if button is clicked
    if button_clicked != -1:
        is_moving = True

    # top
    pygame.draw.circle(screen, RED if is_moving else BLUE, (250, 50), 30 if button_clicked == 1 else 40)
    # down
    pygame.draw.circle(screen, RED if is_moving else BLUE, (250, 200), 30 if button_clicked == 2 else 40)
    # left
    pygame.draw.circle(screen, RED if is_moving else BLUE, (150, 125), 30 if button_clicked == 3 else 40)
    # right
    pygame.draw.circle(screen, RED if is_moving else BLUE, (350, 125), 30 if button_clicked == 4 else 40)
    # up
    pygame.draw.circle(screen, RED if is_moving else BLUE, (400, 300), 30 if button_clicked == 5 else 40)
    # down
    pygame.draw.circle(screen, RED if is_moving else BLUE, (400, 400), 30 if button_clicked == 6 else 40)
    # flip-forward
    pygame.draw.circle(screen, RED if is_moving else BLUE, (100, 300), 30 if button_clicked == 7 else 40)
    # flip-backward
    pygame.draw.circle(screen, RED if is_moving else BLUE, (100, 400), 30 if button_clicked == 8 else 40)

    pygame.display.flip()

    if is_moving:
        if button_clicked == 1:
            forward(drone_speed)
        elif button_clicked == 2:
            backward(drone_speed)
        elif button_clicked == 3:
            left(drone_speed)
        elif button_clicked == 4:
            right(drone_speed)
        elif button_clicked == 5:
            up(drone_speed)
        elif button_clicked == 6:
            down(drone_speed)
        elif button_clicked == 7:
            flip_forward()
        elif button_clicked == 8:
            flip_backward()
        is_moving = False
        button_clicked = -1

land()

# Done! Time to quit.
pygame.quit()
