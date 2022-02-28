# phospholipid agents class
import numpy as np

class lipid(object):\
    #states, 0=walking, 1=stable, 2=disrupted
    self.Lstate = 0
    self.Rstate = 0
    self.Bstate = 0

    def __init__(self, ID, pos):
        self.ID   = ID  # identifier of agent instance, int
        self.pos  = pos # position of center of agent, tuple (int, int) for x and y coordinates
        self.Lpos = pos # left node position, tuple
        self.Rpos = pos # right node position, tuple
        self.Bpos = pos # bottom node position, tuple

    def update_pos_state(self):
        #simultaneous movement of all three nodes when free/disrupted
        # update agent position
        if(self.Lstate==0 && self.Rstate==0 && self.Bstate==0):
            self.pos = \
            self.pos[0] + np.random.choice(-1,0,1), \
            self.pos[1] + np.random.choice(-1,0,1)

        # left node
        if(self.Lstate==0):
        
        if(self.Lstate==1):
            pass
        if(self.Lstate==2):

        # right node
        if(self.Rstate==0):

        if(self.Rstate==1):
            pass
        if(self.Rstate==2):

        # bottom node
        if(self.Bstate==0):

        if(self.Bstate==1):
            pass
        if(self.Bstate==2):







