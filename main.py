import pygame
from visualization.canvas import Canvas

from visualization.constants import BLACK, HEIGHT, WIDTH

pygame.font.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble sort visualizer")
FPS = 60
labels = []


def create_label(font, text, coordinates):
    label = font.render(text, 1, (255,255,255))
    labels.append((label, coordinates))
    return label


def show_labels():
    for label, coordinates in labels:
        WINDOW.blit(label, coordinates)

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
