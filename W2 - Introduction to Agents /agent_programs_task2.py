class Location:
    def __init__(self, name):
        self.name = name
        self.dirty_prb = 0.4 if self.name == "A" else 0.2

class Action:
    def __init__(self, name):
        self.name = name

class Agent:
    def __init__(self, location):
        self.actions = []
        self.location = location

    def add_action(self, action):
        self.actions.append(action)

    def utility_function(self, action):
        loc = self.location

        if action.name == "Suck":
            reward = 10
            return loc.dirty_prb * reward + (1- loc.dirty_prb) * -4
        
        elif action.name == "Move":
            return -1
        
        return 0

    def choose_action(self):
        actions = [self.actions[0], self.actions[1]]

        best_action = max(actions, key=self.utility_function)
        return best_action

# Example usage:
if __name__ == "__main__":
    agent = Agent(Location("A"))

    # Define actions with their utilities
    action1 = Action("Move")
    action2 = Action("Suck")

    # Add actions to the agent
    agent.add_action(action1)
    agent.add_action(action2)

    # Choose the best action based on utility
    best_action = agent.choose_action()
    print("Best action:", best_action.name)