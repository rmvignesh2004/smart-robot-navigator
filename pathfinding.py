# pathfinding.py

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost to the goal
        self.f = 0  # Total cost

def astar(start, goal, grid):
    open_list = []
    closed_list = []

    open_list.append(start)

    while open_list:
        current = min(open_list, key=lambda node: node.f)

        if current.position == goal.position:
            return reconstruct_path(current)

        open_list.remove(current)
        closed_list.append(current)

        for neighbor in get_neighbors(current, grid):
            if neighbor in closed_list:
                continue
            
            tentative_g = current.g + 1  # Cost from current to neighbor
            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g >= neighbor.g:
                continue

            neighbor.g = tentative_g
            neighbor.h = heuristic(neighbor, goal)
            neighbor.f = neighbor.g + neighbor.h
            neighbor.parent = current

    return None

def reconstruct_path(node):
    path = []
    while node is not None:
        path.append(node.position)
        node = node.parent
    return path[::-1]

def heuristic(node, goal):
    return abs(node.position[0] - goal.position[0]) + abs(node.position[1] - goal.position[1])

def get_neighbors(node, grid):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_position = (node.position[0] + dx, node.position[1] + dy)
        if 0 <= new_position[0] < grid.shape[0] and 0 <= new_position[1] < grid.shape[1]:
            if grid[new_position] == 0:  # Check if it's walkable
                neighbors.append(Node(new_position, node))
    return neighbors
