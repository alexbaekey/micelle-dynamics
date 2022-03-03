#! /bin/bash

# run.py, main script utilizing agents and environment



from phospholipids import lipid
from grid import grid
import numpy as np
import matplotlib as plt
import time

# parameters

num_agents  = 500 
max_x       = 40 
max_y       = 40
seed        = 20 #TODO figure out details of stability regulation
timestep    = 0.01 # TODO equivalence with seconds, minutes, whatever
max_step    = 200
radii = [1]
#radii = [5,10,15,20,25,30,35,40,45,50]
runs_per_rad = 1
#runs_per_rad = 10
agents = []

def run(radius):
    ts=0 # current timestep starting at 0
    # establish grid, create agents
    grid_ = grid(max_x,max_y,seed)
    for i in range(num_agents):
        pos = np.random.choice(np.arange(2,max_x-2,1,int)),np.random.choice(np.arange(2,max_y-2,1,int))
        agents.append(lipid(i,pos))

    grid_.update_grid(agents)
    
    # run movement while wall is incomplete
    while(grid_.assembled != 1 and ts < max_step):
        for i in range(num_agents):
            agents[i].update_pos(grid_)
            agents[i].update_state(grid_)
            grid_.update_grid(agents)
            grid_.print_grid(ts,'radius'+str(radius))
            time.sleep(0.2)
            ts=ts+1*timestep
    if(grid_.assembled == 1):
        start = ts
        grid_.radiate()
        while(grid_.assembled != 1 and ts < max_step):
            for i in range(num_agents):
                agents[i].update_pos(grid_)
                agents[i].update_state(grid_)
                grid_.update_grid(agents)
                grid_.print_grid(ts,'radius'+str(radius))
                ts=ts+1*timestep
        if(grid_.assembled == 1):
            end = ts
            print("completed!")
            reconstruct_time = end-start
            return(reconstruct_time)
    else:
        print("incomplete")


if __name__ == "__main__":
    # run each beam radius case 10 times, collect time to stable reconstruction, plot radius against reconstruction time
    total_runs = runs_per_rad*len(radii)
    results = np.zeros((len(radii),runs_per_rad))
    for i in range(len(radii)):
        for j in range(runs_per_rad):
            results[i][j]=run(radii[i])
    x = radii
    y = np.mean(results,axis=1)
    #plt.plot(x,y)
    #plt.save_fig(os.path.join('results'+'final_analysis.jpg'))
