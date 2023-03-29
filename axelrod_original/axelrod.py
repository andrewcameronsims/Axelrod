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
#TRAITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#FEATURES = 5
RUNS = 1000

SEED = 1

# Seed pseudo-random number generator
rd.seed(SEED)

# Helpful functions for a square grid
def find_location(index, SIZE):
    """
    Finds the x and y coordinates in a square grid of SIZE**2 given an index.
    It is assumed that we are counting from left to right on a set of rows top-down, and that area is square.
    Rows and columns start from 0 given Python indexing conventions.
    
    e.g.
        0  1  2
    0  [0, 1, 2,
    1   3, 4, 5,
    2   6, 7, 8]
    
    4 = [1, 1]
    
    """
    x_pos = index % SIZE
    y_pos = index // SIZE
    return [x_pos, y_pos]

def find_index(loc, SIZE):
    """
    Given x and y location in a square grid SIZE**2, returns an index
    """
    index = (loc[1] * SIZE - 1) + (loc[0] + 1)
    return index

def find_neighbors(loc):
    """
    Given x and y coordinates, returns compass points neighbors as list
    """
    N = loc[0], loc[1] - 1
    S = loc[0], loc[1] + 1
    W = loc[0] - 1, loc[1]
    E = loc[0] + 1, loc[1]
    NW = loc[0] - 1, loc[1] - 1
    NE = loc[0] + 1, loc[1] - 1
    SW = loc[0] - 1, loc[1] + 1
    SE = loc[0] + 1, loc[1] + 1
    return [N, S, W, E, NW, NE, SW, SE]

# Define the model and the agents as classes
class Agent():
    "Agents to populate the model"
    
    def __init__(self):
        self.greediness = rd.uniform(0, 1)
        self.money = rd.uniform(0, 1)
        #self.culture = [rd.choice(TRAITS) for i in range(FEATURES)]

    #def culture_share(self, target, model):
    #    similarity = 0
    #    for i in model.agents[target].culture:
    #        if i == self.culture[model.agents[target].culture.index(i)]:
    #            similarity += 1 
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
