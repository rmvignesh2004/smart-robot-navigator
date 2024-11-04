import pygame
import numpy as np

class Environment:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = np.zeros((height, width), dtype=int)  # 0: free space, 1: obstacle

    def add_obstacle(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 1  # Set an obstacle

    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, (139, 69, 19), rect)  # Brown color for stones
                else:
                    pygame.draw.rect(screen, (255, 215, 0), rect)  # Gold color for free space (coins)
                    pygame.draw.circle(screen, (255, 223, 0), rect.center, self.cell_size // 4)

    def display(self):
        print(self.grid)
