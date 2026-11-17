import random

# Distance between cities
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)

# Calculate total distance
def cost(path):

    total = 0

    for i in range(n - 1):
        total += dist[path[i]][path[i + 1]]

    total += dist[path[-1]][path[0]]

    return total


# Generate neighboring paths
def get_neighbors(path):

    neighbors = []

    for i in range(1, n):
        for j in range(i + 1, n):

            new_path = list(path)

            new_path[i], new_path[j] = new_path[j], new_path[i]

            neighbors.append(tuple(new_path))

    return neighbors


# Local Beam Search
def local_beam_search(k):

    # Generate k random paths
    beam = []

    for i in range(k):
        path = list(range(n))
        random.shuffle(path)
        beam.append(tuple(path))

    while True:

        neighbors = []

        # Generate neighbors of all paths
        for path in beam:
            neighbors.extend(get_neighbors(path))

        # Sort paths according to cost
        neighbors.sort(key=cost)

        # Select best k paths
        new_beam = neighbors[:k]

        # Check whether improvement is possible
        if cost(new_beam[0]) >= min(cost(p) for p in beam):
            break

        beam = new_beam

    return min(beam, key=cost)


# Run algorithm
k = 3

solution = local_beam_search(k)

print("Best Path:", solution)
print("Minimum Distance:", cost(solution))

print("Tour:")

for city in solution:
    print(city, end=" -> ")

print(solution[0])