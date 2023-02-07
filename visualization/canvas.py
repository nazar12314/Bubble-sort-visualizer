import random
from time import sleep
import pygame
from typing import List

from visualization.cell import Cell
from visualization.constants import AMOUNT_OF_CELLS, BLACK, BLUE, NUMBER_RANGE, RED, WHITE


class Canvas:
    def __init__(self, window) -> None:
        self.cells: List[Cell] = []
        self.window = window
        self.labels = []
        self.font = pygame.font.SysFont("monospace", 15)
        self.__generate_cells()

        self.create_label(self.font, "Press \"Space\" to launch!", (5, 5))
        self.create_label(self.font, "Press \"r\" to restart!", (5, 20))

    def __generate_cells(self):
        for idx in range(AMOUNT_OF_CELLS):
            value = random.randint(*NUMBER_RANGE)
            self.cells.append(Cell(value, idx))

    def draw(self):
        for idx, cell in enumerate(self.cells):
            cell.set_idx(idx)
            cell.set_x()
            cell.draw_cell(self.window)

        self.show_labels()
        pygame.display.update()

    def bubble_sort(self):
        for i in range(AMOUNT_OF_CELLS - 1):
            for j in range(0, AMOUNT_OF_CELLS - i - 1):
                if self.cells[j] > self.cells[j + 1]:
                    self.cells[j].color = RED
                    self.cells[j + 1].color = BLUE

                    self.cells[j], self.cells[j + 1] = self.cells[j + 1], self.cells[j]

                    self.window.fill(BLACK)
                    self.draw()

                    self.cells[j].color = WHITE
                    self.cells[j + 1].color = WHITE

                    sleep(0.03)

    def reset(self):
        self.cells.clear()
        self.__generate_cells()

    def create_label(self, font, text, coordinates):
        label = font.render(text, 1, (255,255,255))
        self.labels.append((label, coordinates))
        return label

    def show_labels(self):
        for label, coordinates in self.labels:
            self.window.blit(label, coordinates)
