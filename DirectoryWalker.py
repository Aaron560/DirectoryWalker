"""
Date: 3/23/2021
Program: File Walking with recursion.
"""

import os


def Main():
    walkfn(input("Enter File Directory To Walk: "), 1, input("What the max depth you want?: "))

#This is a function that sets a level, maxlevel, and userinputted directory.
def walkfn(dirname, level, maxlevel):
    output = os.path.join(dirname, 'output')
    if os.path.exists(output):
        with open(output) as file1:
            for line in file1:
                if line.startswith('Final value:'):
                    print (line)
    else:
        #checks to see if directory is empty and if so tell the user.
        if len(os.listdir(dirname)) == 1 and level == 1:
            print("This Directory is empty.")
        
        #walks through all directories and stops walking at max value given.
        for name in os.listdir(dirname):
            if int(maxlevel) == 0:
                
                #walks through directory and appends another '|' for each level.
                path = os.path.join(dirname, name)
                if os.path.isdir(path):
                    string = ""
                    for i in range(level):
                        string += ("|")
                    print (string, name, "'")
                    os.chdir(path)
                    walkfn(path, level + 1, maxlevel)
            
            elif int(level) >= int(maxlevel):
                break
Main()