''' Making folders with the same name of files in a directory
    then moving them in the Matching folder
    Warning: this is a powerful moving tool!, use it responsibly by copying
    the files to a new folder and then running the python file!
    Somar-tfr 07.03.2021
'''
#importing libraries for Commandline operations and regular expressions
import os
import re
import shutil


#making a list of filenames
filenames = os.listdir(path='.')

#looping in the names list
for file in filenames:
    #ignring the excution file
    if file == 'edit_univ.py':
        continue
    else:
        #using regular expressions to delet exerything after "."
        fileo = re.findall('(.+)\.', file)
        try:
            #trying ofly for files and not for folders
            filedir = ".\\"+fileo[0]
        except:
            continue
        try:
            # trying only non existing names
            os.mkdir(filedir)
        except:
            continue
        shutil.move((".\\"+file), filedir)
