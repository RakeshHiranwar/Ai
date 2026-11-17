
# Game tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [2, 3],
    'E': [5, 9],
    'F': [0, 1],
    'G': [7, 5]
}

# Alpha-Beta Pruning function
def alpha_beta(node, alpha, beta, maximizing):

    # If node is a leaf, return its value
    if node not in tree:
        return node

    if maximizing:

        value = float('-inf')

        for i, child in enumerate(tree[node]):

            result = alpha_beta(child, alpha, beta, False)

            value = max(value, result)

            alpha = max(alpha, value)

            # Check pruning condition
            if alpha >= beta:
                print("Pruned:", tree[node][i+1:])
                break

        return value

    else:

        value = float('inf')

        for i, child in enumerate(tree[node]):

            result = alpha_beta(child, alpha, beta, True)

            value = min(value, result)

            beta = min(beta, value)

            # Check pruning condition
            if alpha >= beta:
                print("Pruned:", tree[node][i+1:])
                break

        return value

# Start the algorithm
result = alpha_beta('A', float('-inf'),
                    float('inf'), True)

print("Optimal Value:", result)