import numpy as np
import matplotlib.pyplot as plt
import os

class grid(object):

    def __init__(self, max_x,max_y,seed):
        self.max_x = max_x
        self.max_y = max_y
        self.Lwall = seed-1
        self.Rwall = seed+1
        self.assembled = 0
        self.Lassembled = 0
        self.Rassembled = 0
        self.seed = seed
        self.occupation = np.zeros((max_x,max_y),dtype=int)

    def reset(self):
        self.occupation = np.zeros((self.max_x,self.max_y))

    def update_grid(self,agents):
        self.reset()
        for i in range(len(agents)-1):
            # 5=L, 6=R, 7=B
            self.occupation[agents[i].Lpos[0]][agents[i].Lpos[1]] = 5
            self.occupation[agents[i].Rpos[0]][agents[i].Rpos[1]] = 6
            self.occupation[agents[i].Bpos[0]][agents[i].Bpos[1]] = 7

    def check_wall(self):
        #TODO replace pseudocode
        #if(self.occupation[Lwall] is filled (no 0 values)):
        #    self.Lassembled = 1
        #if(self.occupation[Rwall] is filled (no 0 values)):
        #    self.Rassembled = 1
        #if(self.Lassembled == 1 and self.Rassembled == 1):
        #    self.assembled = 1
        #    return current timestep
        #else:
        #    return
        pass

    def print_grid(self,timestep,name):
        filename = name+str(timestep)
        np.savetxt(os.path.join('results'+'/'+filename),self.occupation)
            

    def radiate(radius,agents):
        # radiation exposure in center of grid, square for simplicity, "radius" is just length of side
        radiation_x = (max_x/2)-radius, (max_x/2)+radius
        radiation_y = (max_y/2)-radius, (max_y/2)+radius
        for i in range(len(agents)-1):
            if( agents[i].pos[0]>radiation_x[0] and agents[i].pos[0]<radiation_x[1] and \
                agents[i].pos[1]>radiation_y[0] and agents[i].pos[1]<radiation_y[1]):
                    agents[i].disrupted=1




