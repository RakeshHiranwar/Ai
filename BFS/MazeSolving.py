from collections import deque

# 0 = Free cell, 1 = Obstacle

grid=[
    [0,0,0,1],
    [0,1,0,1],
    [0,1,0,0],
    [0,1,1,0]
]

start = (0, 0)
goal = (3, 3)

# Possible movements
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Generate neighbors
def get_neighbors(state):

    neighbors = []

    for dx, dy in moves:

        x = state[0] + dx
        y = state[1] + dy

        if (0 <= x < len(grid) and
            0 <= y < len(grid[0]) and
            grid[x][y] == 0):

            neighbors.append((x, y))

    return neighbors


# Goal condition
def is_goal(state):
    return state == goal



def bfs(start, get_neighbors, is_goal):

    queue = deque([(start, [start])])

    visited = {start}

    while queue:

        state, path = queue.popleft()

        # Check goal
        if is_goal(state):
            return path

        # Explore neighbors
        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append((neighbor, path + [neighbor]))

    return None


# Common function to print solution
def print_solution(solution):

    if solution:

        print("Solution found!")

        for step, state in enumerate(solution):
            print("Step", step, ":", state)

        print("Total moves:", len(solution) - 1)

    else:
        print("No solution found")


# Run BFS
solution = bfs(start, get_neighbors, is_goal)

print_solution(solution)