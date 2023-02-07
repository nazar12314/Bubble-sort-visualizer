import pygame

from visualization.constants import BORDER, CELL_WIDTH, GREY, HEIGHT, WHITE


class Cell:
    def __init__(self, value, idx, color=WHITE) -> None:
        self.height = value
        self.color = color
        self.idx = idx
        self.y = HEIGHT - value
        self.x = self.idx * CELL_WIDTH

    def draw_cell(self, window):
        pygame.draw.rect(
            window,
            GREY,
            (self.x, self.y, CELL_WIDTH, self.height)
        )

        pygame.draw.rect(
            window,
            self.color,
            (self.x, self.y, CELL_WIDTH - BORDER, self.height - BORDER)
        )

    def set_idx(self, idx):
        self.idx = idx

    def set_x(self):
        self.x = self.idx * CELL_WIDTH

    def __gt__(self, other):
        return self.height > other.height

    def __repr__(self) -> str:
        return str(self.height)
