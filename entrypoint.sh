#!/bin/bash
############!/bin/sh -l

# download and install srcml


#setup directory
mkdir fold
shopt -s extglob
mv !(fold) fold/
# mv java1.java fold/

#convert files to srcml
srcml --verbose fold -o master.xml 2> logs.txt

#generate a file with the identifiers within the project
cd ..
cd ..
mv /github/workspace/master.xml /


# python3 CatchIdentifiers.py > output.txt 2> logs.txt
python3 CatchIdentifiers.py >&2 


python3 results.py


cat results.txt




