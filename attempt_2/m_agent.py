# AGENT FILE
# ALEXANDER BAEKEY #
# Sat Mar 19 14:27:42 2022 #

import numpy
from mesa import Agent

class micelle(Agent):
    """ Micelle agent """

    def __init__(self, ID, model):
        super().__init__(ID, model)

    def step(self):
        print("agent #" + str(self.ID))
        self.move()

        # if(condition):
        #   action related to state

    def action(self):
        x = self.model.grid.get_cell_list_contents([self.pos])

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
                self.pos, 
                moore=True, 
                include_center = False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)


