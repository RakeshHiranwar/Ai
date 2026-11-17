from collections import deque
import heapq

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


# Calculate misplaced tiles
def heuristic(state):

    count = 0

    for i in range(9):

        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


# A* Search
def astar(start, get_neighbors, is_goal):

    # Priority queue: (f, g, state, path)
    pq = []

    heapq.heappush(pq, (heuristic(start), 0, start, [start]))

    visited = {}

    while pq:

        f, g, state, path = heapq.heappop(pq)

        # Skip if a better path was already found
        if state in visited and visited[state] <= g:
            continue

        visited[state] = g

        # Check goal
        if is_goal(state):
            return path

        # Explore neighbors
        for neighbor in get_neighbors(state):

            new_g = g + 1
            new_h = heuristic(neighbor)

            new_f = new_g + new_h

            heapq.heappush(
                pq,
                (new_f, new_g, neighbor, path + [neighbor])
            )

    return None


# Print solution
def print_solution(solution):

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


# Run A* Search
solution = astar(start, get_neighbors, is_goal)

print_solution(solution)