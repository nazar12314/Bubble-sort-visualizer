import pygame
from visualization.canvas import Canvas

from visualization.constants import BLACK, HEIGHT, WIDTH

pygame.font.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble sort visualizer")
FPS = 60


def main():
    run = True
    clock = pygame.time.Clock()
    canvas = Canvas(WINDOW)

    WINDOW.fill(BLACK)

    while run:
        clock.tick(FPS)
        canvas.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    canvas.bubble_sort()

                if event.key == pygame.K_r:
                    canvas.reset()
                    canvas.bubble_sort()

    pygame.quit()


if __name__ == "__main__":
    main()
