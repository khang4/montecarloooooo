# rgeners - random generators
# custom module for use with The Function. generates random [x,y] pairs
# between a specific range for The Function and tracks various
# statistics

import random;
import math;
import blum;

class _rgener:
    def __init__(self):
        self.datalength=[0,0,0];
        self.sums=[[0,0],[0,0],[0,0]];
        self.squaresums=[[0,0],[0,0],[0,0]];
        self.means=[[0,0],[0,0],[0,0]];
        self.variances=[[0,0],[0,0],[0,0]];
        self.sd=[[0,0],[0,0],[0,0]];

        self.blum=blum.BlumBlumShub(128);

        self.lastLCG=[12,13]; #stores un scaled value of lcg for use in generating more numbers
        self.returnLCG=[0,0]; #return value lcg

    # randomly generate with python's normal random Function
    # i believe it uses the twister method (maybe)
    def pyRandom(self):
        rv=[random.uniform(-3,3),random.uniform(0,.4)];
        # print("{} {}".format(rv[0],rv[1]));

        self.updateTracks(rv,0);
        return rv;

    def blumRandom(self):
        rv=[-3+((self.blum.next(128)*6)/(2**128)),(self.blum.next(128)*.4)/(2**128)];
        # print("{} {}".format(rv[0],rv[1]));

        self.updateTracks(rv,1);
        return rv;

    def lcgRandom(self):
        self.lastLCG[0]=self.lcg(1103515245,12345,self.lastLCG[0],(2**31)-1);
        self.lastLCG[1]=self.lcg(1103515245,12345,self.lastLCG[1],(2**31)-1);

        rv=[((self.lastLCG[0]*6)/((2**31)-1))-3,(self.lastLCG[1]*.4)/((2**31)-1)];

        # print("{} {}".format(rv[0],rv[1]));

        self.updateTracks(rv,2);
        return rv;

    # give constants a,b,s (seed) and m (mod)
    # use constants that people say are good for a,b,m
    # use the last generated number as the seed for another
    # random number
    def lcg(self,a,b,s,m):
        return ((a*s)+b)%m;

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

    # returns [mean,variances,standard dev] for specified generator index
    # all stats are [x,y] arrays, as both values are tracked seperately
    def getStats(self,generatorNo):
        return [self.means[generatorNo],self.variances[generatorNo],self.sd[generatorNo]];