# Generate neighbors
def get_neighbors(state):

    neighbors = []

    for i in range(len(state)):

        # Get top block
        block = state[i][-1]

        # Move block to table
        if len(state[i]) > 1:

            new_state = list(state)

            new_state[i] = state[i][:-1]

            new_state.append((block,))

            neighbors.append(tuple(sorted(new_state)))

        # Move block onto another tower
        for j in range(len(state)):

            if i != j:

                new_state = list(state)

                new_state[i] = state[i][:-1]

                new_state[j] = state[j] + (block,)

                temp = []
                for s in new_state:
                    if s:
                        temp.append(s)
                new_state = temp

                neighbors.append(tuple(sorted(new_state)))

    return neighbors


# Goal condition
def is_goal(state):
    return state == (("A", "B", "C", "D"),)

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
start = (("B", "C", "D", "A"),)

solution = dfs(start, get_neighbors, is_goal)

print_solution(solution)