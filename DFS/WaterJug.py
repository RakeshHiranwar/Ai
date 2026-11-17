# Generate neighbors
def get_neighbors(state):

    small, big = state

    neighbors = []

    # Empty small jug
    neighbors.append((0, big))

    # Empty big jug
    neighbors.append((small, 0))

    # Pour small into big
    transfer = min(small, 5 - big)
    neighbors.append((small - transfer, big + transfer))

    # Pour big into small
    transfer = min(big, 2 - small)
    neighbors.append((small + transfer, big - transfer))

    return neighbors


# Goal condition
def is_goal(state):
    return state == (0, 1)

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
start = (2, 5)

solution = dfs(start, get_neighbors, is_goal)

print_solution(solution)