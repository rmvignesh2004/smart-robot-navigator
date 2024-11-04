# main.py
import numpy as np
from robot import Robot
from pathfinding import astar, Node
from environment import Environment

def main():
    # Create an environment
    env = Environment(10, 10)
    # Adding obstacles
    env.add_obstacle(4, 4)
    env.add_obstacle(4, 5)
    env.add_obstacle(4, 6)
    env.add_obstacle(5, 4)
    env.add_obstacle(6, 4)

    # Display environment
    print("Environment Grid:")
    env.display()

    # Initialize robot
    robot = Robot(position=(0, 0))
    start_node = Node(position=robot.get_position())
    goal_node = Node(position=(9, 9))

    # Find path using A*
    path = astar(start_node, goal_node, env.grid)

    if path:
        print("Path found:")
        for step in path:
            robot.move_to(step)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
