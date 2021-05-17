import os
import numpy as np
import re
import pandas as pd
os.chdir("C:/Users/86135/Desktop/pythonProject/Practical 8")
file1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
file2 = open('unknown_function.fa', 'w')
a = ''
s = ''
Bool = False
for line in file1:
    if line.startswith(r'>'):
        if Bool == True:
            a = a + ('>' + name + "      " + str(len(s)) + '\n' + s + '\n')
            s = ''
        if 'unknown function' in line:
            name = re.findall(r'.+gene:(.+?)\s', line)
            name = name[0]
            Bool = True
        else:
            Bool = False
    else:
        if Bool == True:
            s = s + line.strip()
file1.close()
file2.write(a)
file2.close()
file2 = open('unknown_function.fa', 'r')
print(file2.read())