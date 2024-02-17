#!/bin/bash
############!/bin/sh -l

# download and install srcml
ls
whoami

wget http://131.123.42.38/lmcrs/v1.0.0/srcml_1.0.0-1_ubuntu20.04.deb

dpkg -i srcml_1.0.0-1_ubuntu20.04.deb
# wget http://131.123.42.38/lmcrs/v1.0.0/srcml_1.0.0-1_ubuntu20.04.tar.gz


# tar xzf srcml_1.0.0-1_ubuntu20.04.tar.gz

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

python3 app/CatchIdentifiers.py

#install python dependencies
pip install pandas

#run categories algorithm
python3 app/setCategories.py




