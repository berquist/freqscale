#This program is used to run all the subrutines including input or input6, pbs or pbs6, and Freqscale  

#!/bin/bash
s1="yes"
s2="no"
s3="reduced model"
s4="full model"
echo -n "Do you have access to Gaussian software on your machine (yes or no)? > "
read text1
if [ "$text1" == "$s1" ]
then
        echo -n "Download the Gaussian software using proper command on your machine > "
        read text2
        $text2 
        # module load gaussian (command on MSI)
        echo -n "Download the python3/3.4 or higher using proper command on your machine > " 
        read text3
        $text3
        # module load python3/3.4 (command on MSI)
        echo -n "reduced model or full model? > "
        read text4
        if [ "$text4" == "$s3" ]
        then
              echo "Use Reduced Scale Factor Optimization Model"
              python input6.py  # generate the input files for Gaussian 09 or 03
              echo -n "Do you have a PBS job queue system (yes or no)? > "
              read text5
              if [ "$text5" == "$s1" ]
              then
                        python pbs6.py    # generate the pbs files for the following 15 moleucles
                        for f in c2h2 ch4 h2co h2o n2o nh3
                        do
                                qsub "$f".pbs     # using the command to submit your jobs
                        done
                        sleep 0.2h                # adjust the time according to the time needed to finish all 15 jobs on your machine
                        for f in c2h2 ch4 h2co h2o n2o nh3
                        do
                                grep "Kcal/Mol"  "$f".out| awk '{print $1}'  >> freqcom.txt
                        done
                fi
                if [ "$text5" == "$s2" ]
                then
                        echo -n "Type in the command for running gaussian calculations on your machine > "
                        read text6
                        for f in c2h2 ch4 h2co h2o n2o nh3
                        do
                                echo "Running $text6 $f..."
                                $text6 $f & 
                        done
                        sleep 0.2h
                        for f in c2h2 ch4 h2co h2o n2o nh3
                        do
                                grep "Kcal/Mol"  "$f".out| awk '{print $1}'  >> freqcom.txt
                        done
                fi
        fi
        if  [ "$text4" == "$s4" ]
        then
              echo "Use Full Scale Factor Optimization Model"
              python input.py
              echo -n "Do you have a PBS job queue system (yes or no)? > "
              read text5
              if [ "$text5" == "$s1" ]
              then
                        python pbs.py    # generate the pbs files for the following 15 moleucles
                        for f in c2h2  ch4 co2 co f2 h2co h2o h2 hcn hf n2o n2 nh3 oh cl2
                        do
                                qsub "$f".pbs     # using the command to submit your jobs
                        done
                        sleep 0.2h                # adjust the time according to the time needed to finish all 15 jobs on your machine
                        for f in c2h2  ch4 co2 co f2 h2co h2o h2 hcn hf n2o n2 nh3 oh cl2
                        do
                                grep "Kcal/Mol"  "$f".out| awk '{print $1}'  >> freqcom.txt
                        done
                fi
                if [ "$text5" == "$s2" ]
                then
                        echo -n "Type in the command for running gaussian calculations on your machine > "
                        read text6
                        for f in c2h2  ch4 co2 co f2 h2co h2o h2 hcn hf n2o n2 nh3 oh cl2
                        do
                                echo "Running $text6 $f..."
                                $text6 $f & 
                        done
                        sleep 0.2h
                        for f in c2h2  ch4 co2 co f2 h2co h2o h2 hcn hf n2o n2 nh3 oh cl2
                        do
                                grep "Kcal/Mol"  "$f".out| awk '{print $1}'  >> freqcom.txt
                        done
                fi
        fi
python Freqscale.py # calculating the optimized frequency 
rm -f freqcom.txt # cleaning the input file
fi
if [ "$text1" == "$s2" ]
then
        echo -n "Download the python3/3.4 or higher using proper command on your machine > "
        read text3
        $text3 
        echo -n "reduced model or full model? > "
        read text4
        if [ "$text4" == "$s3" ]
        then
                echo -n "Reading ZPEs from a pre-created file (yes or no)? > "
                read text6 
                if [ "$text6" == "$s1" ]
                then
                    echo -e "Reading ZPEs from file freqcom.txt"
                fi
                if [ "$text6" == "$s2" ]
                then    
                    echo -e "Please enter the calculated ZPE for the following molecules: c2h2 ch4 h2co h2o n2o nh3"
                    read ZPE1                   # read in ZPEs from keyboard     
                    read ZPE2
                    read ZPE3
                    read ZPE4
                    read ZPE5
                    read ZPE6
                    echo $ZPE1 >> freqcom.txt
                    echo $ZPE2 >> freqcom.txt
                    echo $ZPE3 >> freqcom.txt
                    echo $ZPE4 >> freqcom.txt
                    echo $ZPE5 >> freqcom.txt
                    echo $ZPE6 >> freqcom.txt
                fi
        fi
        if [ "$text4" == "$s4" ] 
        then
                echo -n "Reading ZPEs from a pre-created file (yes or no)? > "
                read text6
                if [ "$text6" == "$s1" ]
                then
                    echo -e "Reading ZPEs from file freqcom.txt"
                fi
                if [ "$text6" == "$s2" ]
                then
                    echo -e "Please enter the calculated ZPE for the following molecules: c2h2  ch4 co2 co f2 h2co h2o h2 hcn hf n2o n2 nh3 oh cl2"
                    read ZPE1                   # read in ZPEs from keyboard
                    read ZPE2
                    read ZPE3
                    read ZPE4
                    read ZPE5
                    read ZPE6
                    read ZPE7
                    read ZPE8
                    read ZPE9
                    read ZPE10
                    read ZPE11
                    read ZPE12
                    read ZPE13
                    read ZPE14
                    read ZPE15
                    echo $ZPE1 >> freqcom.txt
                    echo $ZPE2 >> freqcom.txt
                    echo $ZPE3 >> freqcom.txt
                    echo $ZPE4 >> freqcom.txt
                    echo $ZPE5 >> freqcom.txt
                    echo $ZPE6 >> freqcom.txt
                    echo $ZPE7 >> freqcom.txt
                    echo $ZPE8 >> freqcom.txt
                    echo $ZPE9 >> freqcom.txt
                    echo $ZPE10 >> freqcom.txt
                    echo $ZPE11 >> freqcom.txt
                    echo $ZPE12 >> freqcom.txt
                    echo $ZPE13 >> freqcom.txt
                    echo $ZPE14 >> freqcom.txt
                    echo $ZPE15 >> freqcom.txt
                fi
        fi
python Freqscale.py
rm -f freqcom.txt 
fi




