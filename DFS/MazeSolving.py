# 0 = Free cell, 1 = Obstacle

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

moves = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


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


def dfs(start, get_neighbors, is_goal):

    stack = [(start, [start])]
    visited = {start}

    while stack:

        state, path = stack.pop()

        # Check goal
        if is_goal(state):
            return path

        # Explore neighbors
        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                visited.add(neighbor)

                stack.append((neighbor, path + [neighbor]))

    return None


# Common function to print solution
def print_solution(solution):

    if solution:

        print("Solution found!")

        for step, state in enumerate(solution):
            print("Step", step, ":", state)

        print("Total steps:", len(solution) - 1)

    else:
        print("No solution found")

solution = dfs(start, get_neighbors, is_goal)

print_solution(solution)