import numpy
import re
import glob
from IPython.core.display import Image
import sys

Att = 30

fsSNE = 1/6.8e-6

print ("fsSNE = ", fsSNE)

ts =[25.0e-3, 12.5e-3, 10.0e-3]

for i in ts:
    NsSNE =numpy.round(i*fsSNE)
    print ("NsSNE =", NsSNE)

Pdmin = 0.9

Pfa = 0.1

Np = 1000

def get_ccdf(x):
    
    xs = numpy.array(x)
    xs.sort()
    N = float(len(xs))
    P = numpy.arange((N)/N)
    
    print (xs, P)
    return xs, P

def get_gamma0(gammaN):
    
    gammaN, Pd = get_ccdf(gammaN)
    gamma0 = numpy.interp(1. - Pfa, Pd, gammaN)
    
    return gamma0


gammaN = numpy.loadtxt(r'C:\Users\MWORIA\Desktop\spectrum\spectrum\spectrum\measurements\pd\usrp\data.dat')
gamma0 = get_gamma0(gammaN)

gammaNs, Pd = get_ccdf(gammaN)
plot(gammaNs, 1.-Pd)
plot([gamma0, gamma0], [0, 1], 'b--')
plot([2e-5, 3e-5], [Pfa, Pfa], 'b--')
axis([2e-5, 3e-5, 0, 1])
title("CCDF")
xlabel("$\gamma_0$")
ylabel("$P_{fa}$")
grid()