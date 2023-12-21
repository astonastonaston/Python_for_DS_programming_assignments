def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''
    assert type(fname)==str
    assert type(n)==int

    f = open(fname, "r")
    fsize = f.seek(0, 2)
    csize = fsize//n + 1
    breakpts = [i * (csize) for i in range(n)]
    breakpts.append(fsize)

    f.seek(0)
    # find till line beginning
    print(breakpts)
    for i in range(len(breakpts)): 
        pt = breakpts[i]
        if (pt != 0):
            f.seek(pt)
            c = f.read(1)
            while (c != '\n'):
                # print(pt)
                c = f.read(1)
                pt -= 1 # one more decrement when reading '\n'
                f.seek(pt)
                # print(c)
            # print("Finish ite!")
            pt += 2 # f (f.tell()) changed but pt unchanged! So increment pt by 1! and another one for the decrement caused by the in-loop reading
        breakpts[i] = pt
    print(breakpts)

    # output file chunks
    for i in range(n):
        with open("{}_{:03d}.txt".format(fname, i), "wt") as g:
            f.seek(breakpts[i])
            print("read {} bytes from starting point {}".format(breakpts[i+1]-breakpts[i], breakpts[i]))
            g.write(f.read(breakpts[i+1]-breakpts[i]))

    
    # if (fsize-breakpts[-1] > csize): # remaining larger than chunk: split one more
    #     breakpts.append((breakpts[-1]+fsize)//2)
    # breakpts.append(fsize-1)

    return 0

def main():
    split_by_n("pg5200.txt", 3)
    return 0

main()