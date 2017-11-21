import math;
import random;
import rgeners;

rgener=rgeners._rgener();

_twopi=1/math.sqrt(2*math.pi); #the constant 1/sqrt(2pi)
_wolfamAnswer=.99730020393673981094; #integral of The Function gotten from wolff fam
_searchSpace=6*.4; #area to randomly monte-carlo in. -3->-3, 0->.4

def main():
    hits=0;
    maxrays=10;
    raw=1;

    if not raw:
        print("{:>8} {:>10} {:>10} {:>10} {:>10} {:>12} {:>12} {:>10} {:>10}".format(
            "iters","answer","error","mean x","mean y","variance x","variance y","sd x","sd y"
        ));

    for x in range(maxrays):
        rv=rgener.pyRandom();
        # rv=rgener.blumRandom();
        # rv=rgener.lcgRandom();

        if hitfunction(rv[0],rv[1]):
            hits+=1;

        fv=finalvalue(hits,maxrays,_searchSpace,_wolfamAnswer);
        rngStats=rgener.getStats(0);

        mainPrint(x,fv[0],fv[1],rngStats[0],rngStats[1],rngStats[2],raw);

    # fv=finalvalue(hits,maxrays,_searchSpace,_wolfamAnswer);
    # print(fv);

def mainPrint(iter,answer,error,mean,variance,sd,raw=0):
    if not raw:
        print("{:8} {:10.6f} {:10.6f} {:10.6f} {:10.6f} {:12.6f} {:12.6f} {:10.6f} {:10.6f}".format(
            iter,answer,error,mean[0],mean[1],variance[0],variance[1],sd[0],sd[1]
        ));
        return;

    print("{} {} {} {} {} {} {} {} {}".format(
        iter,answer,error,mean[0],mean[1],variance[0],variance[1],sd[0],sd[1]
    ));

# give it number of hit rays, number of fired rays,
# the search area, and the actual value
# returns [monte carlo computed value, difference of the
# actual answer and approximated answer]
def finalvalue(hitrays,firedrays,searchArea,actual):
    fv=(hitrays/firedrays)*searchArea;
    return [fv,abs(actual-fv)];

# give an x, returns a y
def TheFunction(x):
    return _twopi*(math.e**(-((x**2)/2)));

# give an x and y, tests if x and y are inside The Function
# (1 for inside the function)
def hitfunction(rx,ry):
    if ry<TheFunction(rx):
        return 1;
    return 0;

def otherrngtest():
    # print(blumgen.next(4));

    rnum=12;
    for x in range(12):
        rnum=lcg(134775813,1,rnum,2**32);
        print(rnum);

def pitest():
    searchsquare=1;
    maxrays=1000;
    hit=0;
    for x in range(0,maxrays):
        rx=random.random();
        ry=random.random();

        if rx*rx+ry*ry<1:
            hit+=1;

    print((hit/maxrays)*searchsquare);

if __name__=="__main__":
    main();