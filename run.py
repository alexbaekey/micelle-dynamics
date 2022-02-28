#! /bin/bash

import phospholipids
import grid

# parameters

num agents  = 500
max_x       = 300 
max_y       = 300
left_line   = 100
right line  = 104 #TODO figure out details of stability regulation
timestep    = 0.01 # TODO equivalence with seconds
steps       = 5000
ts          = 0 # current timestep, initial t=0


if __name__ == "__main__":
    grid = grid(max_x,max_y)
    for i in num_agents:
        agents[i] = phopsholipids(i)
    
    grid.place_agents(agents)

