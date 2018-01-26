#My first experiments with pygame

import pygame, time

def main():
    pygame.init()
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    orange = (226, 115, 8)
    screen_width = 600
    scree_heigh = 400
    game_screen = pygame.display.set_mode((scree_heigh,screen_width))
    game_screen.fill(black)
    pygame.draw.circle(game_screen, red, (160, 290), 20)
    pygame.draw.circle(game_screen, red, (260, 290), 20)
    pygame.draw.rect(game_screen, blue, (140, 200, 160, 70))
    pygame.draw.polygon(game_screen,blue,[(140,220), (90,269), (140,269)])
    pygame.draw.rect(game_screen, blue, (230, 160, 70, 70))
    pygame.draw.rect(game_screen, green, (253, 173, 25, 25))
    pygame.draw.circle(game_screen, orange,(150, 212), 5)
    pygame.draw.aaline(game_screen, (36, 123, 104), (140, 220), (140, 269))
    pygame.draw.aaline(game_screen, (36,123, 104), (130, 230), (130, 269))
    pygame.draw.aaline(game_screen, (36, 123, 104), (120, 240), (120, 269))
    pygame.draw.aaline(game_screen, (36, 123, 104), (110, 250), (110, 269))
    pygame.draw.aaline(game_screen, (36, 123, 104), (100, 260), (100, 269))

game_on = True
while game_on is True:
    main()
    pygame.display.update()
    time.sleep(10)
    game_on = False

