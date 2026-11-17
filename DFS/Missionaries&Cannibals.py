# Check whether state is valid
def is_valid(m, c):

    rm = 3 - m
    rc = 3 - c

    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and c > m:
        return False

    if rm > 0 and rc > rm:
        return False

    return True


# Generate neighbors
def get_neighbors(state):

    m, c, boat = state

    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    neighbors = []

    for dm, dc in moves:

        if boat == 1:
            new_state = (m - dm, c - dc, 0)

        else:
            new_state = (m + dm, c + dc, 1)

        if is_valid(new_state[0], new_state[1]):
            neighbors.append(new_state)

    return neighbors


# Goal condition
def is_goal(state):
    return state == (0, 0, 0)


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

# Initial state
start = (3, 3, 1)

solution = dfs(start, get_neighbors, is_goal)

print_solution(solution)