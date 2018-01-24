#My first experiments with pygame

import pygame, time

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def main():
    pygame.init()
    global black
    global red
    screen_width = 600
    scree_heigh = 400
    game_screen = pygame.display.set_mode((scree_heigh,screen_width))
    game_screen.fill(black)
    pygame.draw.circle(game_screen, red, (250, 300), 20)

game_on = True
while game_on is True:
    main()
    pygame.display.update()
    time.sleep(10)
    game_on = False

