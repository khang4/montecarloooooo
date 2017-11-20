# rgeners - random generators
# custom module for use with The Function. generates random [x,y] pairs
# between a specific range for The Function and tracks various
# statistics

import random;
import math;

class _rgener:
    def __init__(self):
        self.datalength=[0,0,0];
        self.sums=[[0,0],[0,0],[0,0]];
        self.squaresums=[[0,0],[0,0],[0,0]];
        self.means=[[0,0],[0,0],[0,0]];
        self.variances=[[0,0],[0,0],[0,0]];
        self.sd=[[0,0],[0,0],[0,0]];

    # randomly generate with python's normal random Function
    # i believe it uses the twister method (maybe)
    def pyRandom(self):
        rv=[random.uniform(-3,3),random.uniform(0,.4)];
        self.updateTracks(rv,0);
        return rv;

    # give generated x,y array value and
    # the generator index to update data for
    def updateTracks(self,value,gi):
        self.sums[gi][0]+=value[0];
        self.sums[gi][1]+=value[1];

        self.datalength[gi]+=1;

        self.means[gi][0]=self.sums[gi][0]/self.datalength[gi];
        self.means[gi][1]=self.sums[gi][1]/self.datalength[gi];

        self.squaresums[gi][0]+=(value[0]-self.means[gi][0])**2;
        self.squaresums[gi][1]+=(value[1]-self.means[gi][1])**2;

        self.variances[gi][0]=self.squaresums[gi][0]/self.datalength[gi];
        self.variances[gi][1]=self.squaresums[gi][1]/self.datalength[gi];

        self.sd[gi][0]=math.sqrt(self.variances[gi][0]);
        self.sd[gi][1]=math.sqrt(self.variances[gi][1]);