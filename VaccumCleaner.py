# Vacuum Cleaner World

# Environment
environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# Initial position of vacuum cleaner
position = 'A'

# Simple Reflex Agent
def vacuum_agent(position, environment):

    if environment[position] == 'Dirty':
        print("Room", position, "is Dirty -> Suck")
        environment[position] = 'Clean'

    elif position == 'A':
        print("Room A is Clean -> Move Right")
        position = 'B'

    elif position == 'B':
        print("Room B is Clean -> Move Left")
        position = 'A'

    return position


# Run the agent
for i in range(5):

    position = vacuum_agent(position, environment)

    print("Environment:", environment)
    print()
