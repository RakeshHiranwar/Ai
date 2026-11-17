# Initial State
state = [
    ("On", "B", "A"),
    ("OnTable", "A"),
    ("OnTable", "C"),
    ("OnTable", "D"),
    ("Clear", "B"),
    ("Clear", "C"),
    ("Clear", "D"),
    ("ArmEmpty",)
]

# Goal State
goals = [
    ("On", "C", "A"),
    ("On", "B", "D")
]

plan = []


# Check whether a block is clear
def is_clear(block):
    return ("Clear", block) in state


# Apply action to the current state
def apply(action):

    name = action[0]

    if name == "UNSTACK":

        x, y = action[1], action[2]

        state.remove(("On", x, y))
        state.remove(("Clear", x))
        state.remove(("ArmEmpty",))

        state.append(("Clear", y))
        state.append(("Holding", x))

    elif name == "PICKUP":

        x = action[1]

        state.remove(("OnTable", x))
        state.remove(("Clear", x))
        state.remove(("ArmEmpty",))

        state.append(("Holding", x))

    elif name == "STACK":

        x, y = action[1], action[2]

        state.remove(("Holding", x))
        state.remove(("Clear", y))

        state.append(("On", x, y))
        state.append(("Clear", x))
        state.append(("ArmEmpty",))

    elif name == "PUTDOWN":

        x = action[1]

        state.remove(("Holding", x))

        state.append(("OnTable", x))
        state.append(("Clear", x))
        state.append(("ArmEmpty",))

    plan.append(action)


# Goal Stack Planning
def achieve(goal):

    if goal in state:
        return

    # Achieve On(x, y)
    if goal[0] == "On":

        x, y = goal[1], goal[2]

        achieve(("Holding", x))
        achieve(("Clear", y))

        apply(("STACK", x, y))

    # Achieve Holding(x)
    elif goal[0] == "Holding":

        x = goal[1]

        if ("OnTable", x) in state:

            apply(("PICKUP", x))

        else:

            for item in state:

                if item[0] == "On" and item[1] == x:

                    y = item[2]

                    achieve(("Clear", x))

                    apply(("UNSTACK", x, y))
                    break

    # Achieve Clear(x)
    elif goal[0] == "Clear":

        x = goal[1]

        if goal not in state:

            for item in state:

                if item[0] == "On" and item[2] == x:

                    block = item[1]

                    achieve(("Holding", block))

                    apply(("PUTDOWN", block))
                    break


# Execute goals in reverse order
for goal in reversed(goals):

    achieve(goal)


# Display solution
print("Initial State:")
print("B on A, C on Table, D on Table")

print("\nActions:")

for i, action in enumerate(plan, 1):

    print(i, action)

print("\nFinal State:")

for item in state:
    print(item)