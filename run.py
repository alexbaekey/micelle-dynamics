#! /bin/bash

import phospholipids
import grid
import numpy as np
import matplotlib as plt


# parameters

num_agents  = 500
max_x       = 300 
max_y       = 300
seed        = 100 #TODO figure out details of stability regulation
timestep    = 0.01 # TODO equivalence with seconds
max_step    = 1000
ts          = 0 # current timestep, initial t=0
radii = [5,10,15,20,25,30,35,40,45,50]
runs_per_rad = 10

def run(radius):
    # establish grid, create agents
    grid = grid(max_x,max_y,seed)
    for i in num_agents:
        pos = np.random.choice(max_x),np.random.choice(max_y)
        agents[i] = phopsholipids(i,pos) 

    grid.update_grid(agents)
    
    # run movement while wall is incomplete
    while(grid.assembled != 1 && ts < max_step):
        for i in num_agents:
            agents[i].update_pos()
            agents[i].update_state()
            grid.update_grid()
            grid.print_grid(ts,'radius'+str(radius))
            ts=ts+1
    if(grid.assembled == 1):
        start = ts
        grid.radiate()
        while(grid.assembled != 1 && ts < max_step):
            for i in num_agents:
                agents[i].update_pos()
                agents[i].update_state()
                grid.update_grid()
                grid.print_grid(ts,'radius'+str(radius))
                ts=ts+1
        if(grid.assembled == 1):
            end = ts
            print("completed!")
            reconstruct_time = end-start
            return(reconstruct_time)
    else:
        print("incomplete")


if __name__ == "__main__":
    # run each beam radius case 10 times, collect time to stable reconstruction, plot radius against reconstruction time
    total_runs = runs_per_rad*len(radii)
    results = np.zeros((len(radii),10))
    for i in range(len(radii)):
        for j in range(len(runs_per_rad)):
            results[i][j]=run(radius)
    plt.plot(results)
    plt.savefig(os.path.join('results'+'final_analysis.jpg')






