import pygame
import pygame._sdl2
from pygame.locals import *

import random

pygame.init()
clock = pygame.time.Clock()

font = pygame.font.Font("SpaceGrotesk-Regular.ttf", 50)
time_font = pygame.font.Font("SpaceGrotesk-Regular.ttf", 30)

class Rotator:
    def __init__(self, filename, screen):
        self.screen = screen
        self.image = pygame.image.load(filename).convert_alpha()

        # resize image so max length is 300
        width = random.randint(100, 300)
        ratio = width / self.image.get_width()
        self.image = pygame.transform.scale(self.image, (int(width), int(self.image.get_height() * ratio)))

        self.theta = random.randint(0, 360)
        self.x = random.randint(0, screen.get_width())
        self.y = random.randint(0, screen.get_height())

        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)
        self.dt = random.randint(-10, 10)

    def blitRotateCenter(self, topleft):
        rotated_image = pygame.transform.rotate(self.image, self.theta)
        new_rect = rotated_image.get_rect(
            center=self.image.get_rect(
                topleft=topleft
            ).center
        )
        self.screen.blit(rotated_image, new_rect)

    def step(self):
        self.blitRotateCenter((self.x, self.y))
        self.theta = (self.theta + self.dt) % 360
        self.x += self.dx
        self.y += self.dy
        if self.x < 0 or self.x > self.screen.get_width():
            self.dx *= -1
        if self.y < 0 or self.y > self.screen.get_height():
            self.dy *= -1

def alert(text, time):
    # Initialize window
    pygame.display.init()
    screen = pygame.display.set_mode((0, 0), FULLSCREEN)
    window = pygame._sdl2.video.Window.from_display_module()
    window.focus()

    # flashing background
    bg_ctr = 0
    background_colors = [(217, 2, 63), (4, 4, 89)]
    curr_background = 0

    # Initialize rotators
    rotators = [Rotator(f"motivational_images/{random.randint(0, 5)}.png", screen) for _ in range(10)]

    while True:
        # flashing background
        screen.fill(background_colors[curr_background])
        bg_ctr = (bg_ctr + 1) % 10
        if bg_ctr % 10 == 0:
            curr_background = (curr_background + 1) % len(background_colors)

        # glorious aesthetic display
        for rotator in rotators:
            rotator.step()

        # text
        text_render = font.render(text, True, (255, 255, 255))
        text_rect = text_render.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(text_render, text_rect)

        time_render = time_font.render(time, True, (255, 255, 255))
        time_rect = time_render.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 100))
        screen.blit(time_render, time_rect)

        pygame.display.flip()
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    return

if __name__ == "__main__":
    while True:
        input()
        alert("skydiving appointment!!", "in 10 minutes")
        print("exit!")