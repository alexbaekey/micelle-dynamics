

# phospholipid agents class

import numpy as np
choice = np.random.choice


class lipid(object):
    """
    #states, 0=walking, 1=stable
    """
    stable = 0
    disrupted = 0

    def __init__(self, ID, pos):
        self.ID   = ID  # identifier of agent instance, int
        # tuples of positions for all 
        # 4 courners of the agent
        #  
        #  L  R
        #  p  B
        #
        # p is "pos"
        #
        self.pos  = pos # "center"
        self.Lpos = pos[0],pos[1]+1 # left
        self.Rpos = pos[0]+1,pos[1]+1 # right
        self.Bpos = pos[0]+1,pos[1] # bottom
        self.orientation = 0 #0,1,2,3
        #
        # 0:      1:      2:     3:
        # LR      pL      Bp     RB
        # pB      BR      RL     Lp
        #
        return

    def disrupt(self):
        self.disrupted = 1
        return

    def update_pos(self,grid):
        """
        #simultaneous movement of all three nodes when free/disrupted
        """
        # create movement values
        jump_x = choice(np.arange(-int(grid.max_x/3),int(grid.max_x/3),1))
        jump_y = choice(np.arange(-int(grid.max_y/3),int(grid.max_y/3),1))

        # center
        move_posx = choice((-1,0,1))
        move_posy = choice((-1,0,1))

        #update positions
        if(self.disrupted==1):
            self.rotate()
            self.pos =(
                self.pos[0] + jump_x,
                self.pos[1] + jump_y
                )
            #TODO make sure jump doesn't go off screen
            self.Lpos = self.pos+self.Lpos
            self.Rpos = self.pos+self.Rpos
            self.Bpos = self.pos+self.Bpos
            self.disrupted=0
        elif(self.disrupted==0 and 
                self.stable==0 and
                self.Lpos[0]+move_posx<grid.max_x
                and
                self.Lpos[0]+move_posy>=0
                and
                self.Lpos[1]+move_posy<grid.max_y
                and
                self.Lpos[1]+move_posy>=0
                and
                self.Rpos[0]+move_posx<grid.max_x
                and
                self.Rpos[0]+move_posy>=0
                and
                self.Rpos[1]+move_posy<grid.max_y
                and
                self.Rpos[1]+move_posy>=0
                and
                self.Bpos[0]+move_posx<grid.max_x
                and
                self.Bpos[0]+move_posy>=0
                and
                self.Bpos[1]+move_posy<grid.max_y
                and
                self.Bpos[1]+move_posy>=0            
        ):
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
            self.rotate()
        elif(self.disrupted==0 and self.stable==1):
            pass

        #TODO CLUSTERED MOVEMENT GOES HERE



    def update_state(self,grid):
        """
        # idea to fix orientation issue
        # make agents into a 3square L shape
        # need to account for all 4 orientations
        # this would fix self-identification problem
        #
        # LR
        # B
        #
        # self assembly (right wall)would then look like:
        #
        # 
        #  
        #  BL
        #   R
        #  BL 
        #   R
        #
        #
        """
        pass
        # B check
        #TODO include once one wall is formed



    def rotate(self):
        """x = choice(0,1,2,3)
        def rot1():
            self.pos[1] = self.pos[1]+1
            self.Lpos[0] = self.Lpos[0]+1
            self.Rpos[1] = self.Rpos[1]-1
            self.Bpos[0] = self.Bpos[0]-1
        def rot2():
            self.pos[0] = self.pos[0]+1
            self.pos[1] = self.pos[1]+1
            self.Lpos[0] = self.Lpos[0]+1
            self.Lpos[1] = self.Lpos[1]-1
            self.Rpos[0] = self.Rpos[0]-1
            self.Rpos[1] = self.Rpos[1]-1
            self.Bpos[0] = self.Bpos[0]-1
            self.Bpos[1] = self.Bpos[1]+1
        def rot3():
            self.pos[0] = self.pos[0]+1
            self.Lpos[1] = self.Lpos[1]+1
            self.Rpos[0] = self.Rpos[0]-1
            self.Bpos[1] = self.Bpos[1]+1
            """
        def gen_rot(ax,ay,bx,by,cx,cy,dx,dy,ori):
            x = choice((0,1,2,3))
            if(x==0):
                pass
            if(x==1):
                ay=ay+1
                bx=bx+1
                cy=cy-1
                dx=dx-1
                #TODO replace with mod
                if(ori != 3):
                    ori = ori+1
                else:
                    ori = 0
            if(x==2):
                ax=ax+1
                ay=ay+1
                bx=bx+1
                by=by-1
                cx=cx-1
                cy=cy-1
                dx=dx-1
                dy=dy+1
                if(ori==0,1):
                    ori=ori+2
                elif(ori==2):
                    ori=0
                elif(ori==3):
                    ori=1

            if(x==3):
                ax=ax+1
                by=by+1
                cx=cx-1
                dy=dy+1
                if(ori==0):
                    ori=3
                if(ori==1):
                    ori=0
                if(ori==2):
                    ori=1
                if(ori==3):
                    ori=2
        if(self.orientation==0):
            gen_rot(
                ax = self.pos[0],
                ay = self.pos[1],
                bx = self.Lpos[0],
                by = self.Lpos[1],
                cx = self.Rpos[0],
                cy = self.Rpos[1],
                dx = self.Bpos[0],
                dy = self.Bpos[1],
                ori=self.orientation
            )
        elif(self.orientation==1):
            gen_rot(
                ax = self.Bpos[0],
                ay = self.Bpos[1],
                bx = self.pos[0],
                by = self.pos[1],
                cx = self.Lpos[0],
                cy = self.Lpos[1],
                dx = self.Rpos[0],
                dy = self.Rpos[1],
                ori=self.orientation
            )
        elif(self.orientation==2):
            gen_rot(
                ax = self.Rpos[0],
                ay = self.Rpos[1],
                bx = self.Bpos[0],
                by = self.Bpos[1],
                cx = self.pos[0],
                cy = self.pos[1],
                dx = self.Lpos[0],
                dy = self.Lpos[1],
                ori=self.orientation
            )
        elif(self.orientation==3):
            gen_rot(
                ax = self.Lpos[0],
                ay = self.Lpos[1],
                bx = self.Rpos[0],
                by = self.Rpos[1],
                cx = self.Bpos[0],
                cy = self.Bpos[1],
                dx = self.pos[0],
                dy = self.pos[1],
                ori=self.orientation
            )


            
