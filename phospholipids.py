

# phospholipid agents class

import numpy as np
choice = np.random.choice


class lipid(object):\
    #states, 0=walking, 1=stable
    Lstate = 0
    Rstate = 0
    Bstate = 0
    disrupted = 0

    def __init__(self, ID, pos):
        self.ID   = ID  # identifier of agent instance, int
        self.pos  = pos # position of center of agent, tuple (int, int) for x and y coordinates
        self.Lpos = pos[0]+choice((-1,0,1)),pos[1]+choice((-1,0,1)) # left node position, tuple
        self.Rpos = pos[0]+choice((-1,0,1)),pos[1]+choice((-1,0,1)) # right node position, tuple
        self.Bpos = pos[0]+choice((-1,0,1)),pos[1]+choice((-1,0,1)) # bottom node position, tuple
        #self.grid = grid
        return

    def disrupt(self):
        self.disrupted = 1
        return

    def update_pos(self,grid):
        #simultaneous movement of all three nodes when free/disrupted

        # create movement values
        jump_x = choice(np.arange(-int(grid.max_x/3),int(grid.max_x/3),1))
        jump_y = choice(np.arange(-int(grid.max_y/3),int(grid.max_y/3),1))

        # center
        move_posx = choice((-1,0,1))
        move_posy = choice((-1,0,1))

        # left node
        move_Lx = choice((-1,0,1))
        move_Ly = choice((-1,0,1))

        # right node
        move_Rx = choice((-1,0,1))
        move_Ry = choice((-1,0,1))

        # bottom node
        move_Bx = choice((-1,0,1))
        move_By = choice((-1,0,1))


        #TODO delete prints 

        # - WORKS
        #print("jump_x: "+ str(jump_x))
        #print("jump_y: "+ str(jump_y))

        # - ?
        #print("move_posx: "+ str(move_posx))
        #print("move_posy: "+ str(move_posy))

        # - ?
        #print("move_Lx: "+ str(move_Lx))
        #print("move_Ly: "+ str(move_Ly))

        # - ?
        #print("move_Rx: "+ str(move_Rx))
        #print("move_Ry: "+ str(move_Ry))

        # - ?
        #print("move_Bx: "+ str(move_Bx))
        #print("move_By: "+ str(move_By))

        #update positions
        if(self.disrupted==1):
            self.pos =(
                self.pos[0] + jump_x,
                self.pos[1] + jump_y
                )
            #TODO make sure jump doesn't go off screen
            self.Lpos = self.pos+self.Lpos
            self.Rpos = self.pos+self.Rpos
            self.Bpos = self.pos+self.Bpos
            self.disrupted=0
        elif(self.disrupted==0 and self.Lstate==0 and self.Rstate==0 and self.Bstate==0):
            self.pos =(
                self.pos[0] + move_posx, 
                self.pos[1] + move_posy
            )
            self.Lpos =(
                self.Lpos[0] + move_posx, 
                self.Lpos[1] + move_posy
            )
            self.Rpos =(
                self.Rpos[0] + move_posx, 
                self.Rpos[1] + move_posy
            )
            self.Bpos =(
                self.Bpos[0] + move_posx, 
                self.Bpos[1] + move_posy
            )
        elif(self.disrupted==0 and self.Lstate==1 or self.Rstate==1 or self.Bstate==1):

            # move relative to agent's center position

            # LEFT NODE #############################

            # walking state 0
            if(self.Lstate==0):
                if(
                    (self.Lpos[0]+move_Lx < grid.max_x and self.Lpos[0]+move_Lx > 0) and  
                    (self.Lpos[1]+move_Ly < grid.max_y and self.Lpos[1]+move_Ly > 0) and  
                    (abs(self.Lpos[0]+move_Lx - self.pos[0])<=2 and abs(self.Lpos[1]+move_Ly - self.pos[1])<=2)
                    ):
                        self.Lpos[0] = self.Lpos[0]+move_Lx
                        self.Lpos[1] = self.Lpos[1]+move_Ly

            # stable state, no movement
            if(self.Lstate==1):
                pass
            
            # RIGHT NODE ############################

            if(self.Rstate==0):
                if(
                (self.Rpos[0]+move_Rx < grid.max_x and self.Rpos[0]+move_Rx > 0) and 
                (self.Rpos[1]+move_Ry < grid.max_y and self.Rpos[1]+move_Ry > 0) and  
                (abs(self.Rpos[0]+move_Rx - self.pos[0])<=2 and abs(self.Rpos[1]+move_Ry - self.pos[1])<=2)
                ):
                    self.Rpos[0] = self.Rpos[0]+move_Rx
                    self.Rpos[1] = self.Rpos[1]+move_Ry
            
            if(self.Rstate==1):
                pass

            # BOTTOM NODE ###########################
            if(self.Bstate==0):
                if(
                (self.Bpos[0]+move_Bx < grid.max_x and self.Bpos[0]+move_Bx > 0) and 
                (self.Bpos[1]+move_By < grid.max_y and self.Bpos[1]+move_By > 0) and  
                (abs(self.Bpos[0]+move_Bx - self.pos[0])<=1 and abs(self.Bpos[1]+move_By - self.pos[1])<=2)
                ):
                    self.Bpos[0] = self.Bpos[0]+move_Bx
                    self.Bpos[1] = self.Bpos[1]+move_By
            
            if(self.Bstate==1):
                pass

        #TODO CLUSTERED MOVEMENT GOES HERE



    def update_state(self,grid):
        #check if an L is above/beneath an R on wall, check if B is left/right of B on wall
        # *note* commented out positions for surrounding spots that aren't considered
        if(self.Lstate ==0):
            #if(grid.occupation[self.Lpos[0]-1][self.Lpos[1]-1] == 6): # hit for L/R match
            #    pass
            #if(grid.occupation[self.Lpos[0]-1][self.Lpos[1]] == 6 # hit for L/R match
            #    pass
            #if(grid.occupation[self.Lpos[0]-1][self.Lpos[1]+1] == 6 # hit for L/R match
            #    pass
            if(grid.occupation[self.Lpos[0]][self.Lpos[1]-1] == 6): # hit for L/R match
                if(self.Lpos[0]==grid.Lwall):
                    self.Lstate = 1
            if(grid.occupation[self.Lpos[0]][self.Lpos[1]+1] == 6): # hit for L/R match
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
            if(grid.occupation[self.Rpos[0]][self.Rpos[1]-1] == 5): # hit for L/R match
                if(self.Rpos[0]==grid.Rwall):
                    self.Rstate = 1
            if(grid.occupation[self.Rpos[0]][self.Rpos[1]+1] == 5): # hit for L/R match
                if(self.Rpos[0]==grid.Lwall):
                    self.Rstate = 1
        
        # B check
        #TODO include once one wall is formed




