# This program is used to calculate the Scale Factors for Zero-Point Energies, Harmonic Frequencies, and Fundamental Frequencies. 

import random
import sys
import os

NUMER = 0.0   # numerator in eq. 5 of the main paper
DENOM = 0.0   # denominator in eq. 5 of the main paper
LAMBDA = 0.0  # lamda_ZPE on the left side of eq. 5 of the main paper

#read in calculated and experimental frequencies
with open('freqcom.txt') as f:
    f=[x.strip() for x in f if x.strip()]
    data=[tuple(map(float,x.split())) for x in f[0:]]
    zpecom=[x[0] for x in data]
if len(zpecom) == 15:
#calculate scale factor for Zero-Point Energies for the full model
        zpeexp = (16.490, 27.710, 7.3, 3.0929144, 1.302, 16.1, 13.26, 6.231, 10.000, 5.864, 6.770, 3.3618, 21.200, 5.2915, 0.7983)
        for i in range(0,15):
                NUMER = NUMER + zpecom[i]*zpeexp[i]
                DENOM = DENOM + zpecom[i]**2.0
else:
#calculate scale factor for Zero-Point Energies for the reduced model        
        zpeexp = (16.490, 27.710, 16.1, 13.26, 6.770, 21.200)
        for i in range(0,6):
                NUMER = NUMER + zpecom[i]*zpeexp[i]
                DENOM = DENOM + zpecom[i]**2.0
LAMBDA = NUMER/DENOM

#print the results to the screen

print('FREQ: A PROGRAM FOR OPTIMIZING SCALE FACTORS (Version 1)\n')
print('                 written by                 \n')
print('Haoyu S. Yu, Lucas J. Fiedler, I.M. Alecu, and Donald G. Truhlar\n')
print('Department of Chemistry and Supercomputing Institute\n')
print('University of Minnesota, Minnesota 55455-0431\n')
print('Scale Factor for Zero-Point Energies     =',LAMBDA,'\n')
print('Scale Factor for Harmonic Frequencies    =',LAMBDA*1.014,'\n')
print('Scale Factor for Fundamental Frequencies =',LAMBDA*0.974,'\n')
print('CITATIONS:\n')
print('1. Alecu, I.M., Zheng, J., Zhao, Y., and Truhlar, D.G. J. Chem. Theory Comput. 2010, 6, 2872\n')
print('2. Yu, S.H., Fiedler, L.J., Alecu, I.M., and Truhlar, D.G. Comput. Phys.Commun. submittted 2016\n')


