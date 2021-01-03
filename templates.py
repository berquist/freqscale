header_gaussian = """%mem=420mb
# opt=(vtight,Maxcycle=200) scf=(xqc,maxcycle=400,tight) Freq integral=ultrafine
"""

molecule_blocks = {
    "c2h2": {
        "charge": 0,
        "multiplicity": 1,
        "block": """C
C,1,CC
X,2,1.,1,90.
H,2,CH,3,90.,1,180.,0
X,1,1.,2,90.,3,180.,0
H,1,CH,5,90.,2,180.,0

CC=1.203142
CH=1.062605
""",
    },
    "ch4": {
        "charge": 0,
        "multiplicity": 1,
        "block": """C
H,1,RCH
H,1,RCH,2,AHCH
H,1,RCH,2,AHCH,3,AHCH,1
H,1,RCH,2,AHCH,3,AHCH,-1

RCH=1.08744517
AHCH=109.471221
""",
    },
    "cl2": {
        "charge": 0,
        "multiplicity": 1,
        "block": """Cl
Cl,1,R

R=1.1
""",
    },
    "co": {
        "charge": 0,
        "multiplicity": 1,
        "block": """O
C,1,RCO

RCO=1.12960815
""",
    },
    "co2": {
        "charge": 0,
        "multiplicity": 1,
        "block": """C
O,1,R
X,1,1.000000,2,90.000000
O,1,R,3,90.000000,2,180.000000,0

R=1.1594846
""",
    },
    "f2": {
        "charge": 0,
        "multiplicity": 1,
        "block": """F
F,1,FF

FF=1.3952041
""",
    },
    "h2": {
        "charge": 0,
        "multiplicity": 1,
        "block": """H
H,1,r

r=0.74187646
""",
    },
    "h2co": {
        "charge": 0,
        "multiplicity": 1,
        "block": """O        0.000000    0.000000    0.674622
C        0.000000    0.000000   -0.529707
H        0.000000    0.935488   -1.109367
H        0.000000   -0.935488   -1.109367
""",
    },
    "h2o": {
        "charge": 0,
        "multiplicity": 1,
        "block": """O
H,1,OH
H,1,OH,2,HOH

OH=0.95691441
HOH=104.51706026
""",
    },
    "hcn": {
        "charge": 0,
        "multiplicity": 1,
        "block": """C        0.000000    0.000000   -0.500365
N        0.000000    0.000000    0.652640
H        0.000000    0.000000   -1.566291
""",
    },
    "hf": {
        "charge": 0,
        "multiplicity": 1,
        "block": """F
H,1,R

R=0.91538107
""",
    },
    "n2": {
        "charge": 0,
        "multiplicity": 1,
        "block": """N
N,1,NN

NN=1.09710935
""",
    },
    "n2o": {
        "charge": 0,
        "multiplicity": 1,
        "block": """N
N,1,r1
O,2,r2,1,180.

r1=1.12056262
r2=1.1870483
""",
    },
    "nh3": {
        "charge": 0,
        "multiplicity": 1,
        "block": """N        0.000000    0.000000    0.112890
H        0.000000    0.938024   -0.263409
H        0.812353   -0.469012   -0.263409
H       -0.812353   -0.469012   -0.263409
""",
    },
    "oh": {
        "charge": 0,
        "multiplicity": 2,
        "block": """O
H,1,R

R=0.967
""",
    },
}
