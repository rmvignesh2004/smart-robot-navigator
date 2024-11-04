import pygame
from robot import Robot
from pathfinding import astar, Node
from environment import Environment

# Constants
WIDTH, HEIGHT = 10, 10  # Grid size
CELL_SIZE = 50          # Size of each cell
SCREEN_WIDTH = WIDTH * CELL_SIZE
SCREEN_HEIGHT = HEIGHT * CELL_SIZE

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Smart Robot Game")
    clock = pygame.time.Clock()

    # Create environment and robot
    env = Environment(WIDTH, HEIGHT, CELL_SIZE)
    robot = Robot((0, 0), CELL_SIZE)

    # Add obstacles (stones)
    env.add_obstacle(4, 4)
    env.add_obstacle(4, 5)
    env.add_obstacle(4, 6)
    env.add_obstacle(5, 4)
    env.add_obstacle(6, 4)

    # Find path using A*
    start_node = Node(position=robot.position)
    goal_node = Node(position=(9, 9))
    path = astar(start_node, goal_node, env.grid)

    # Main game loop
    running = True
    path_index = 0
    while running:
        screen.fill((0, 0, 0))  # Clear screen with black

        # Draw the environment and robot
        env.draw(screen)
        robot.draw(screen)

        # Move the robot along the path step by step
        if path and path_index < len(path):
            robot.move_to(path[path_index])
            path_index += 1
            pygame.time.wait(500)  # Wait 500 milliseconds for each step

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
