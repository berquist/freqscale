# This program is used to generate gaussian input files for the reduced model (with six molecules) 

import sys
import string
import os

#read in functional, basis set, and path of the basis set
functional = str(input("Which Method are you going to choose? "))
basis = str(input("Which basis set are you going to choose? "))
path = str(input("What is the path of your basis set? "))
#create input file for molecule c2h2  
file = open("c2h2.com","w")
file.write("%mem=420mb\n")  # memory needed for this job
file.write("# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n") # commands geometry optimization, self-consistent field, frequency calculation, and integration grids
file.write(functional + "/" + basis + "\n")  # functional and basis set 
file.write("\nt\n")
file.write("\n0,1\n")                        # charge and multiplicity 
file.write("C\n")                            # geometries
file.write("C,1,CC\n")
file.write("X,2,1.,1,90.\n")
file.write("H,2,CH,3,90.,1,180.,0\n")
file.write("X,1,1.,2,90.,3,180.,0\n")
file.write("H,1,CH,5,90.,2,180.,0\n\n")
file.write("CC=1.203142\n")
file.write("CH=1.062605\n")
file.write("\n" + path + "\n")               # path of the basis set
file.write("\n")
file.close()
#create input file for molecule ch4
file = open("ch4.com","w")
file.write("%mem=420mb\n")
file.write("# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n")
file.write(functional + "/" + basis + "\n")
file.write("\nt\n")
file.write("\n0,1\n")
file.write("C\n")
file.write("H,1,RCH\n")
file.write("H,1,RCH,2,AHCH\n")
file.write("H,1,RCH,2,AHCH,3,AHCH,1\n")
file.write("H,1,RCH,2,AHCH,3,AHCH,-1\n\n")
file.write("RCH=1.08744517\n")
file.write("AHCH=109.471221\n")
file.write("\n" + path + "\n")
file.write("\n")
file.close()
#create input file for molecule h2co
file = open("h2co.com","w")
file.write("%mem=420mb\n")
file.write("# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n")
file.write(functional + "/" + basis + "\n")
file.write("\nt\n")
file.write("\n0,1\n")
file.write("O        0.000000    0.000000    0.674622\n")
file.write("C        0.000000    0.000000   -0.529707\n")
file.write("H        0.000000    0.935488   -1.109367\n")
file.write("H        0.000000   -0.935488   -1.109367\n")
file.write("\n" + path + "\n")
file.write("\n")
file.close()
#create input file for molecule h2o
file = open("h2o.com","w")
file.write("# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n")
file.write(functional + "/" + basis + "\n")
file.write("\nt\n")
file.write("\n0,1\n")
file.write("O\n")
file.write("H,1,OH\n")
file.write("H,1,OH,2,HOH\n")
file.write("\nOH=0.95691441\n")
file.write("HOH=104.51706026\n")
file.write("\n" + path + "\n")
file.write("\n")
file.close()
#create input file for molecule n2o
file = open("n2o.com","w")
file.write("%mem=420mb\n")
file.write("# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n")
file.write(functional + "/" + basis + "\n")
file.write("\nt\n")
file.write("\n0,1\n")
file.write("N\n")
file.write("N,1,r1\n")
file.write("O,2,r2,1,180.\n")
file.write("\nr1=1.12056262\n")
file.write("r2=1.1870483\n")
file.write("\n" + path + "\n")
file.write("\n")
file.close()
#create input file for molecule nh3
file = open("nh3.com","w")
file.write("%mem=420mb\n")
file.write("# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n")
file.write(functional + "/" + basis + "\n")
file.write("\nt\n")
file.write("\n0,1\n")
file.write("N        0.000000    0.000000    0.112890\n")
file.write("H        0.000000    0.938024   -0.263409\n")
file.write("H        0.812353   -0.469012   -0.263409\n")
file.write("H       -0.812353   -0.469012   -0.263409\n")
file.write("\n" + path + "\n")
file.write("\n")
file.close()









