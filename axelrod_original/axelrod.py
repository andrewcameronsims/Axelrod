"""
Implementation of the Axelrod model of cultural convergence and polarisation

AXELROD R (1997) The dissemination of culture - A model with local convergence and global polarization. 
    Journal of Conflict Resolution 41(2), pp. 203-226.

"""

# Convention: greediness is the first component, money the second

# Import libraries
import random as rd

# Define constants
SIZE = 5
RUNS = 1000

# Seed pseudo-random number generator
rd.seed(1)

# Define the model and the agents as classes
class Agent():
    "Agents to populate the model"
    
    def __init__(self):
        self.greediness = rd.uniform(0, 1)
        self.money = rd.uniform(0, 1)
    def game(self, target, model):
        interaction_probability = self.greediness

        if self.money > model.agents[target].money:
            win_probability = 0.55
        else:
            win_probability = 0.45

        if rd.uniform(0, 1) < interaction_probability:
            if rd.uniform(0, 1) < win_probability:    
                model.agents[target].money = model.agents[target].money - 0.1
                self.money = self.money + 0.1
            else: 
                model.agents[target].money = model.agents[target].money + 0.1
                self.money = self.money - 0.1

class Axelrod():
    "This is the model"
    
    def __init__(self):
        self.agents = [Agent() for i in range(SIZE**2)]
    
    def tick(self):
        "Runs a single cycle of the simulation"
        try:
            active = rd.choice(list(enumerate(self.agents)))
            passive = rd.choice(list(enumerate(self.agents)))
            while active[0] == passive[0]:
                passive = rd.choice(list(enumerate(self.agents)))
            active[1].game(passive[0], self)
        except IndexError:
            self.tick()
 
    def show_state(self):
        for n in range(0, SIZE):
            row = [ [self.agents[i].greediness, self.agents[i].money] for i in range(n * SIZE, n * (SIZE) + SIZE)]
            for agent in row:
                print("[", end="")
                print(*agent, sep=",", end="")
                print("]", end="")
            print()
            print("-" * (SIZE*2*2+SIZE))
    
    def run_sim(self):
        print("Initial state of the model:")
        print()
        self.show_state()
        print()
        print("Running simulation...")
        for r in range(1,RUNS):
            self.tick()
        print("Final state of the model:")
        self.show_state()
        
model = Axelrod()

model.run_sim()
