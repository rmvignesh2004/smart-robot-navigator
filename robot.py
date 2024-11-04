import pygame

class Robot:
    def __init__(self, position, cell_size):
        self.position = position
        self.cell_size = cell_size

    def move_to(self, position):
        self.position = position
        print(f"Robot moved to {self.position}")

    def draw(self, screen):
        x, y = self.position
        rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(screen, (0, 0, 255), rect)  # Blue color for the robot
