import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT




def main():
    pygame.init()
    print_intro()
    draw_screen()


def draw_screen():
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:                                                                 #infinite while loop
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 100                                               #limit to 60 fps
        


def print_intro():
        print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
