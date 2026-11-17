from collections import deque

# Initial state
start = (7, 2, 4,
         5, 0, 6,
         8, 3, 1)

# Goal state
goal = (0, 1, 2,
        3, 4, 5,
        6, 7, 8)


# Generate neighbors
def get_neighbors(state):

    neighbors = []

    zero_idx = state.index(0)

    moves = [-3, 3, -1, 1]

    for move in moves:

        new_pos = zero_idx + move

        if 0 <= new_pos < 9:

            # Prevent left-right boundary crossing
            if move == -1 and zero_idx % 3 == 0:
                continue

            if move == 1 and zero_idx % 3 == 2:
                continue

            new_state = list(state)

            new_state[zero_idx], new_state[new_pos] = new_state[new_pos], new_state[zero_idx]

            neighbors.append(tuple(new_state))

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

# print_solution(solution)

# Print solution in 3x3 format
if solution:

    print("Solution found!")

    for step, state in enumerate(solution):

        print("Step", step)

        print(state[0:3])
        print(state[3:6])
        print(state[6:9])

        print()

    print("Total moves:", len(solution) - 1)

else:
    print("No solution found")