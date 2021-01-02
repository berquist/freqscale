# This program is used to generate gaussian input files for the full model (with 15 molecules)

# read in functional, basis set, and path of the basis set
functional = str(input("Which method are you going to choose? "))
basis = str(input("Which basis set are you going to choose? "))
path = str(input("What is the path of your basis set? "))

with open("c2h2.com", "w") as fh:
    fh.write("%mem=420mb\n")  # memory needed for this job
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )  # commands for geometry optimization, self-consistent-field, frequency calculation, and integration grids
    fh.write(functional + "/" + basis + "\n")  # functional and basis set
    fh.write("\nt\n")
    fh.write("\n0,1\n")  # charge and multiplicity
    fh.write("C\n")  # geometries
    fh.write("C,1,CC\n")
    fh.write("X,2,1.,1,90.\n")
    fh.write("H,2,CH,3,90.,1,180.,0\n")
    fh.write("X,1,1.,2,90.,3,180.,0\n")
    fh.write("H,1,CH,5,90.,2,180.,0\n\n")
    fh.write("CC=1.203142\n")
    fh.write("CH=1.062605\n")
    fh.write("\n" + path + "\n")  # path of the basis set
    fh.write("\n")

with open("ch4.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("C\n")
    fh.write("H,1,RCH\n")
    fh.write("H,1,RCH,2,AHCH\n")
    fh.write("H,1,RCH,2,AHCH,3,AHCH,1\n")
    fh.write("H,1,RCH,2,AHCH,3,AHCH,-1\n\n")
    fh.write("RCH=1.08744517\n")
    fh.write("AHCH=109.471221\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("cl2.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("Cl\n")
    fh.write("Cl,1,R\n\n")
    fh.write("R=1.1\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("co.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("O\n")
    fh.write("C,1,RCO\n\n")
    fh.write("RCO=1.12960815\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("co2.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("C\n")
    fh.write("O,1,R\n")
    fh.write("X,1,1.000000,2,90.000000\n")
    fh.write("O,1,R,3,90.000000,2,180.000000,0\n\n")
    fh.write("R=1.1594846\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("f2.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("F\n")
    fh.write("F,1,FF\n\n")
    fh.write("FF=1.3952041\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("h2.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("H\n")
    fh.write("H,1,r\n\n")
    fh.write("r=0.74187646\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("h2co.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("O        0.000000    0.000000    0.674622\n")
    fh.write("C        0.000000    0.000000   -0.529707\n")
    fh.write("H        0.000000    0.935488   -1.109367\n")
    fh.write("H        0.000000   -0.935488   -1.109367\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("h2o.com", "w") as fh:
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("O\n")
    fh.write("H,1,OH\n")
    fh.write("H,1,OH,2,HOH\n")
    fh.write("\nOH=0.95691441\n")
    fh.write("HOH=104.51706026\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("hcn.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("C        0.000000    0.000000   -0.500365\n")
    fh.write("N        0.000000    0.000000    0.652640\n")
    fh.write("H        0.000000    0.000000   -1.566291\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("hf.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("F\n")
    fh.write("H,1,R\n")
    fh.write("\nR=0.91538107\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("n2.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("N\n")
    fh.write("N,1,NN\n")
    fh.write("\nNN=1.09710935\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("n2o.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("N\n")
    fh.write("N,1,r1\n")
    fh.write("O,2,r2,1,180.\n")
    fh.write("\nr1=1.12056262\n")
    fh.write("r2=1.1870483\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("nh3.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,1\n")
    fh.write("N        0.000000    0.000000    0.112890\n")
    fh.write("H        0.000000    0.938024   -0.263409\n")
    fh.write("H        0.812353   -0.469012   -0.263409\n")
    fh.write("H       -0.812353   -0.469012   -0.263409\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")

with open("oh.com", "w") as fh:
    fh.write("%mem=420mb\n")
    fh.write(
        "# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine\n"
    )
    fh.write(functional + "/" + basis + "\n")
    fh.write("\nt\n")
    fh.write("\n0,2\n")
    fh.write("O\n")
    fh.write("H,1,R\n")
    fh.write("\nR=0.967\n")
    fh.write("\n" + path + "\n")
    fh.write("\n")
