# Kevin Rodriguez
# 2D Graphics Demo CSCI 43700

import pygame


# Initialize Pygame
pygame.init()

# Screen size
window = pygame.display.set_mode((1206, 966))
pygame.display.set_caption("2D Demo")


# colors
red = (255, 0, 0)
# Shortcut variables
x, y, width, height, vel = 301, 300, 40, 40, 30

# Background image
background = pygame.image.load('background.png')

# "Frames per second"
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 50)

# Screen Text Definition
def text_on_screen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    window.blit(screen_text, [x,y])



# Event Loop
loop = True

while loop:
    # Time
    pygame.time.delay(100)
    clock.tick(30)

    # Background image
    window.fill((0, 0, 0))
    window.blit(background, (0,0))

    # Screen Text
    text_on_screen("Hello, this is my 2D game", red, 400, 0)
    text_on_screen("Use the arrow keys to move around", red, 400, 50)

    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # Tracks keyboard input to move our character
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 1150 :
        x += vel

    if keys[pygame.K_UP] and y > vel:
        y -= vel

    if keys[pygame.K_DOWN] and y < 900:
        y += vel

    # Movable rectangle
    pygame.draw.rect(window, (255, 255, 0), (x, y, width, height))

    # Draws lines connecting circles
    pygame.draw.line(window, (255, 0, 0), (100, 200), (300, 450), 5)
    pygame.draw.line(window, (255, 0, 0), (450, 150), (750, 450), 5)
    pygame.draw.line(window, (255, 0, 0), (150, 150), (450, 150), 5)
    pygame.draw.line(window, (255, 0, 0), (350, 450), (750, 450), 5)
    pygame.draw.line(window, (255, 0, 0), (150, 150), (750, 450), 5)
    pygame.draw.line(window, (255, 0, 0), (350, 450), (450, 150), 5)

    # Draws circles
    pygame.draw.circle(window, (0, 255, 255), (150, 150), 75)
    pygame.draw.circle(window, (0, 255, 255), (350, 450), 75)
    pygame.draw.circle(window, (0, 255, 255), (450, 150), 75)
    pygame.draw.circle(window, (0, 255, 255), (750, 450), 75)

    # Update display to display all the images
    pygame.display.update()