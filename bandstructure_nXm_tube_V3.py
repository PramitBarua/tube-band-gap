#!/usr/bin/env python3

__author__ = "Pramit Barua"
__copyright__ = "Copyright 2018, INT, KIT"
__credits__ = ["Pramit Barua"]
__license__ = "INT, KIT"
__version__ = "3"
__maintainer__ = "Pramit Barua"
__email__ = ["pramit.barua@student.kit.edu", "pramit.barua@gmail.com"]

# band structure of (N, N) armchair CNT
# this code matches with wolfram CDF player therefore we should follow this

import numpy
import math
import argparse
import matplotlib.pyplot as plt

def tube_band_gap(n, m):
    fig, ax = plt.subplots(1, 1)
    a0 = 1.42e-10
    a = math.sqrt(3)*a0
#     n = 9
#     m = 8
    abs_ch = math.sqrt(math.pow(n,2)+math.pow(m,2)+m*n) # a is not multiplied
    
    dR = math.gcd(2*m+n, 2*n+m)
    t_cap = abs_ch*numpy.sqrt(3)/dR
    nPos = (n+m)
    nNeg = (n-m)
    
    theta = math.atan(-(nNeg/(math.sqrt(3)*nPos)))
    
    N = 2*(math.pow(m,2)+math.pow(n,2)+(n*m))/math.gcd((2*m)+n, (2*n)+m)
    qBuf=numpy.arange(1,N+1)
    # qBuf=numpy.array([0])
    
    kt = numpy.linspace(-1*math.pi/t_cap, 1*math.pi/t_cap, num=1000)
    
    color=iter(plt.cm.rainbow(numpy.linspace(0,1,len(qBuf))))
    
    for idx1, q in enumerate(qBuf):
        E1 = numpy.ones(len(kt))*numpy.NaN
        kx = numpy.ones(len(kt))*numpy.NaN
        for idx2, itemKt in enumerate(kt):
            kc = 2*math.pi*q/abs_ch #kc means a*kc
            itemKx = itemKt*math.cos(theta)-kc*math.sin(theta)
            kx[idx2] = itemKx
            A = (2*math.pi*q/nPos)-((nNeg*itemKx)/(2*nPos))
            B = itemKx/2
            E1[idx2] = math.sqrt(1+4*math.cos(A)*math.cos(B)+4*math.pow(math.cos(B),2))
        c=next(color)
        line1 = ax.plot(kt/math.pi, E1, color=c, label=q)
        line2 = ax.plot(kt/math.pi, -E1, color=c)
    ax.grid(True)
    plt.title(str(n)+','+str(m)+' tube')
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Shows the band diagram for any tube chirality')
    parser.add_argument("n", type=int, 
                        help='Integer that defines the chirality "n"')
    parser.add_argument("m", type=int, 
                        help='Integer that defines the chirality "m"')
    args = parser.parse_args()
    print('tube chirality: '+str(args.n)+' '+str(args.m))
    
    if args.n >= args.m:
        tube_band_gap(args.n, args.m)
    else:
        print("'n' must be bigger than 'm'")                        