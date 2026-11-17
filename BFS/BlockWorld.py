from collections import deque

# Initial and goal states

start = (("B",), ("C", "A"))

goal = (("C", "B", "A"),)


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

                # Remove empty towers
                temp = []

                for s in new_state:
                    if s:
                        temp.append(s)

                new_state = temp

                neighbors.append(tuple(sorted(new_state)))

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