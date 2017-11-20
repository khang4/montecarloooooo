import blum;
import math;

blumgen=blum.BlumBlumShub(128); #blum blum generator
_twopi=1/math.sqrt(2*math.pi); #the constant 1/sqrt(2pi)
_wolfamAnswer=.99730020393673981094; #integral of The Function gotten from wolff fam
_searchSpace=6*_twopi; #area to integrate in (-3->3,0->1/2pi)=(3+3)*1/2pi=6*1/2pi.
                       #and by 1/2pi i mean whatever it's supposed to be

def main():
    pass;

# give it number of hit rays, number of fired rays,
# the search area, and the actual value
# returns [monte carlo computed value, difference of the
# actual answer and approximated answer]
def finalvalue(hitrays,firedrays,searchArea,actual):
    fv=(hitrays/firedrays)*searchArea;
    return [fv,actual-fv];

# give constants a,b,s (seed) and m (mod)
# use constants that people say are good for a,b,m
# use the last generated number as the seed for another
# random number
def lcg(a,b,s,m):
    return ((a*s)+b)%m;

# give an x, returns a y
def TheFunction(x):
    return _twopi*(math.e**(-((x**2)/2)));

# give an x and y, tests if x and y are inside The Function
def hitfunction(rx,ry):
    if ry<TheFunction(rx):
        return 1;
    return 0;

def otherrngtest():
    print(blumgen.next(4));

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