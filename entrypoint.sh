#!/bin/bash
############!/bin/sh -l

# download and install srcml
ls
pwd

# wget http://131.123.42.38/lmcrs/v1.0.0/srcml_1.0.0-1_ubuntu20.04.deb
# dpkg -i srcml_1.0.0-1_ubuntu20.04.deb

#setup directory
mkdir tempActionFolderIdAnalyzer_v1
shopt -s extglob
mv !(tempActionFolderIdAnalyzer_v1) tempActionFolderIdAnalyzer_v1/
# mv java1.java tempActionFolderIdAnalyzer_v1/


ls
whoami
#convert files to srcml
srcml --verbose tempActionFolderIdAnalyzer_v1 -o master.xml

#generate a file with the identifiers within the project
ls
pwd

ls -la /github/workspace

ls -la /app

echo primeiro cd 
cd .. 
pwd
ls
echo segundo cd
cd ..
pwd
ls

python3 CatchIdentifiers.py

#install python dependencies
pip install pandas

#run categories algorithm
python3 setCategories.py




