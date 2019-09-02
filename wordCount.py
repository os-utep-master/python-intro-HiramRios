import re
import csv
import sys
import os
from typing import List
'''Hiram Rios 80552404 the purpose of this lab is to practice using pyhton and get a feel for it 
 we are to make a program that receives the text file and prints out how many times all the occuring words come out
 in a out put file '''

#print("Please enter the text fle name ")
count: int = 0
temp = []
inputFname= sys.argv[1]
outputFname = sys.argv[2]


hash = {}


key = 0





with open(inputFname) as textFile:
    # this method splits the text file into words removing punctuation  and storing it into a 2d array
    text = [[word.strip(".,!?:;'- |\"-") for line in textFile for word in line.lower().replace('-',' ').replace('\'',' ').split()]]

# I transformed the 2d array into a 1d array so it could be easier to hash
for i in range(len(text)):
    for j in range(len(text[i])):

        temp.append(text[i][j])

#here i implemented a hash table so it can be easier to count the values
for i in range(len(temp)):
    key = temp[i]

# if the has id is already in the hash table it increases the value by 1
    if key in hash:
        hash[key] += 1
    else:
        hash[key] = 1


for key in sorted(hash.keys()) :
    print(key, hash[key])

#
with open("output.txt", 'w') as f:
    for key, value in sorted(hash.items()):
        f.write('%s %s\n' % (key, value))

