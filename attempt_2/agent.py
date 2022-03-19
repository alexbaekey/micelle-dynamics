# AGENT FILE
# ALEXANDER BAEKEY #
# Sat Mar 19 14:27:42 2022 #

import numpy
import mesa

class micelle(agent):
    """ Micelle agent """

    def __init__(self, ID, model):
        super().__init__(ID, model)
        # self.something = something

    def step(self) -> None:
        self.move()
        # if(condition):
        #   action related to state

    def action(self):
        
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
                



