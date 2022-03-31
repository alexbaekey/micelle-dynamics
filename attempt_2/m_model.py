# MODEL FILE
# ALEXANDER BAEKEY #
# Sat Mar 19 14:36:48 2022 #

from mesa import Model
from mesa.time import RandomActivation
from meds.space import SingleGrid

class micelle_model(Model):

    def __init__(self, N):
        self.num_agents = N
        #scheduler assignment
        self.schedule = RandomActivation(self)
        # agent creation
        for i in range(self.num_agents):
            a = micelle_agent(i, self)
            self.schedule.add(a)

            #place agent on grid
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x,y))



    def step(self):
        # advance model by one step
        self.scedule.step()





