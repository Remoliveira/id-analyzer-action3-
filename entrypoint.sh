#!/bin/bash
############!/bin/sh -l

# download and install srcml
ls
pwd




#setup directory
mkdir tempActionFolderIdAnalyzer_v1
shopt -s extglob
mv !(tempActionFolderIdAnalyzer_v1) tempActionFolderIdAnalyzer_v1/
# mv java1.java tempActionFolderIdAnalyzer_v1/



#convert files to srcml
srcml --verbose tempActionFolderIdAnalyzer_v1 -o master.xml

#generate a file with the identifiers within the project
cd ..
cd ..
mv /github/workspace/master.xml /


python3 CatchIdentifiers.py

#run categories algorithm
python3 setCategories.py

python3 results.py


cat results.txt




