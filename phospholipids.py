# phospholipid agents class
import numpy as np

class lipid(object):\
    #states, 0=walking, 1=stable
    self.Lstate = 0
    self.Rstate = 0
    self.Bstate = 0
    self.disrupted = 0


    def __init__(self, ID, pos, grid):
        self.ID   = ID  # identifier of agent instance, int
        self.pos  = pos # position of center of agent, tuple (int, int) for x and y coordinates
        self.Lpos = pos[0]+np.choice((-1,0,1)),pos[1]+np.choice((-1,0,1)) # left node position, tuple
        self.Rpos = pos[0]+np.choice((-1,0,1)),pos[1]+np.choice((-1,0,1)) # right node position, tuple
        self.Bpos = pos[0]+np.choice((-1,0,1)),pos[1]+np.choice((-1,0,1)) # bottom node position, tuple
        self.grid = grid
        return

    def disrupt(self):
        self.disrupted = 1
        return

    def update_pos(self,grid):
        #simultaneous movement of all three nodes when free/disrupted
        # update agent position
        if(self.disrupted==1):
            self.pos = \
            self.pos[0] + np.random.choice(np.arange(-30,30,1,dtype=int), \
            self.pos[1] + np.random.choice(np.arange(-30,30,1,dtype=int)
            return
        if(self.Lstate==0 && self.Rstate==0 && self.Bstate==0):
            self.pos = \
            self.pos[0] + np.random.choice(-1,0,1), \
            self.pos[1] + np.random.choice(-1,0,1)
        else:
            # move relative to agent's center position

            # left node
            randx = np.random.choice((-1,0,1))
            randy = np.random.choice((-1,0,1))
            # walking state 0
            if(self.Lstate==0):
                if((self.Lpos[0]+randx < grid.max_x && self.Lpos[0]+randx > 0) && \ 
                    (self.Lpos[1]+randy < grid.max_y && self.Lpos[1]+randy > 0) && \  
                    (abs(self.Lpos[0]+randx - self.pos[0])<=1 && abs(self.Lpos[1]+randy - self.pos[1])<=1):
                        self.Lpos[0] = self.Lpos[0]+randx
                        self.Lpos[1] = self.Lpos[1]+randy
            # stable state, no movement
            if(self.Lstate==1):
                pass
            
            # right node
            randx = np.random.choice((-1,0,1))
            randy = np.random.choice((-1,0,1))
            if(self.Rstate==0):
                if((self.Rpos[0]+randx < grid.max_x && self.Rpos[0]+randx > 0) && \ 
                    (self.Rpos[1]+randy < grid.max_y && self.Rpos[1]+randy > 0) && \  
                    (abs(self.Rpos[0]+randx - self.pos[0])<=1 && abs(self.Rpos[1]+randy - self.pos[1])<=1):
                        self.Rpos[0] = self.Rpos[0]+randx
                        self.Rpos[1] = self.Rpos[1]+randy
            
            if(self.Rstate==1):
                pass

            # bottom node
            randx = np.random.choice((-1,0,1))
            randy = np.random.choice((-1,0,1))
            if(self.Bstate==0):
                if((self.Bpos[0]+randx < grid.max_x && self.Bpos[0]+randx > 0) && \ 
                    (self.Bpos[1]+randy < grid.max_y && self.Bpos[1]+randy > 0) && \  
                    (abs(self.Bpos[0]+randx - self.pos[0])<=1 && abs(self.Bpos[1]+randy - self.pos[1])<=1):
                        self.Bpos[0] = self.Bpos[0]+randx
                        self.Bpos[1] = self.Bpos[1]+randy
            
            if(self.Bstate==1):
                pass


    def update_state(self):
        #check if an L is above/beneath an R on wall, check if B is left/right of B on wall
        if(self.Lstate ==0):
            #if(grid.occupation[self.Lpos[0]-1][self.Lpos[1]-1] == 6): # hit for L/R match
            #    pass
            #if(grid.occupation[self.Lpos[0]-1][self.Lpos[1]] == 6 # hit for L/R match
            #    pass
            #if(grid.occupation[self.Lpos[0]-1][self.Lpos[1]+1] == 6 # hit for L/R match
            #    pass
            if(grid.occupation[self.Lpos[0]][self.Lpos[1]-1] == 6 # hit for L/R match
                if(self.Lpos[0]==grid.Lwall):
                    self.Lstate = 1
            if(grid.occupation[self.Lpos[0]][self.Lpos[1]+1] == 6 # hit for L/R match
                if(self.Lpos[0]==grid.Rwall):
                    self.Lstate = 1
            #if(grid.occupation[self.Lpos[0]+1][self.Lpos[1]-1] == 6 # hit for L/R match
            #    pass
            #if(grid.occupation[self.Lpos[0]+1][self.Lpos[1]] == 6 # hit for L/R match
            #    pass
            #if(grid.occupation[self.Lpos[0]+1][self.Lpos[1]+1] == 6 # hit for L/R match
            #    pass

        # R check
        if(self.Rstate ==0):
            if(grid.occupation[self.Rpos[0]][self.Rpos[1]-1] == 5 # hit for L/R match
                if(self.Rpos[0]==grid.Rwall):
                    self.Rstate = 1
            if(grid.occupation[self.Rpos[0]][self.Rpos[1]+1] == 5 # hit for L/R match
                if(self.Rpos[0]==grid.Lwall):
                    self.Rstate = 1
        
        # B check
        




