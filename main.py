import pygame
import pygame._sdl2
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

def alert():
    while True:
        screen.fill((255, 0, 0))
        pygame.display.flip()
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    return

while True:
    input()
    pygame.display.init()
    screen = pygame.display.set_mode((0, 0), FULLSCREEN)
    window = pygame._sdl2.video.Window.from_display_module()
    window.focus()
    alert()
    print("exit!")