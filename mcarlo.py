import blum;

blumgen=blum.BlumBlumShub(128);

def main():
    print(blumgen.next(4));


def pitest():
    searchsquare=1;
    maxrays=1000;
    hit=0;
    for x in range(0,maxrays):
        rx=random.random();
        ry=random.random();

        if rx*rx+ry*ry<1:
            hit+=1;

    print((hit/maxrays)*searchsquare*4);

if __name__=="__main__":
    main();