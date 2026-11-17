from collections import deque

# Environment
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Agent's internal state
agent_state = {
    "position": start,
    "visited": set(),
    "environment": grid
}


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


# BFS
def bfs():

    queue = deque([(start, [start])])

    agent_state["visited"].add(start)

    while queue:

        state, path = queue.popleft()

        # Update internal position
        agent_state["position"] = state

        if state == goal:
            return path

        for neighbor in get_neighbors(state):

            if neighbor not in agent_state["visited"]:

                agent_state["visited"].add(neighbor)

                queue.append((neighbor, path + [neighbor]))

    return None


# Print solution
solution = bfs()

if solution:

    print("Path found!")

    for step, position in enumerate(solution):
        print("Step", step, ":", position)

    print("Total moves:", len(solution) - 1)

else:
    print("No solution found")