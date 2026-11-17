from collections import deque

# Initial and goal states
# 1 = Smallest disk, 3 = Largest disk

start = ((3, 2, 1), (), ())

goal = ((), (), (3, 2, 1))


# Generate neighbors
def get_neighbors(state):

    neighbors = []

    # Select source rod
    for i in range(3):

        # Check if source rod is not empty
        if state[i]:

            # Get top disk
            disk = state[i][-1]

            # Select destination rod
            for j in range(3):

                if i != j:

                    # Check whether destination is empty
                    # or its top disk is larger
                    if not state[j] or state[j][-1] > disk:

                        new_state = list(state)

                        # Remove disk from source rod
                        new_state[i] = state[i][:-1]

                        # Place disk on destination rod
                        new_state[j] = state[j] + (disk,)

                        neighbors.append(tuple(new_state))

    return neighbors


# Goal condition
def is_goal(state):

    return state == goal


# BFS algorithm
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


# Print solution
def print_solution(solution):

    if solution:

        rods = ["A", "B", "C"]

        for k in range(len(solution) - 1):

            current = solution[k]
            next_state = solution[k + 1]

            # Find source and destination rods
            for i in range(3):

                if len(current[i]) > len(next_state[i]):
                    source = i
                    disk = current[i][-1]

                elif len(current[i]) < len(next_state[i]):
                    destination = i

            print("Move disk", disk)
            print(rods[source], " -> ", rods[destination])

        print("Minimum number of Steps:", len(solution) - 1)

    else:
        print("No solution found")


# Run BFS
solution = bfs(start, get_neighbors, is_goal)

print_solution(solution)