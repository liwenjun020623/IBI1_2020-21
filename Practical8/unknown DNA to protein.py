import os
import numpy as np
import re
import pandas as pd
os.chdir("C:/Users/86135/Desktop/pythonProject/Practical 8")
code = {
    "TTT": 'F', "TTC": 'F', "TTA": 'L', "TCT": 'S',
    "TTG": 'L', "TCC": 'S', "TCA": 'S', "TCG": 'S',
    "TAT": 'Y', "TAC": 'Y', "TAA": 'O', "TAG": 'U',
    "TGT": 'C', "TGC": 'C', "TGA": 'X', "TGG": 'W',
    "CTT": 'L', "CTC": 'L', "CTA": 'L', "CTG": 'L',
    "CCT": 'P', "CCC": 'P', "CCA": 'P', "CCG": 'P',
    "CAT": 'H', "CAC": 'H', "CAA": 'Q', "CAG": 'Z',
    "CGT": 'R', "CGC": 'R', "CGA": 'R', "CGG": 'R',
    "ATT": 'I', "ATC": 'I', "ATA": 'J', "ATG": 'M',
    "ACT": 'T', "ACC": 'T', "ACA": 'T', "ACG": 'T',
    "AAT": 'N', "AAC": 'B', "AAA": 'K', "AAG": 'K',
    "AGT": 'S', "AGC": 'S', "AGA": 'R', "AGG": 'R',
    "GTT": 'V', "GTC": 'V', "GTA": 'V', "GTG": 'V',
    "GCT": 'A', "GCC": 'A', "GCA": 'A', "GCG": 'A',
    "GAT": 'D', "GAC": 'D', "GAA": 'E', "GAG": 'E',
    "GGT": 'G', "GGC": 'G', "GGA": 'G', "GGG": 'G',
}
file2 = open('unknown_function.fa', 'r')
file_result = input()
file3 = open(file_result, 'w')
s = 0
a = ''
r = ''
for line in file2:
    if line.startswith('>'):
        name = re.findall('>(.+?)\s', line)
        n = name[0]
    else:
        seq = re.findall('...',line)
        for i in range(len(seq)):
            if code[seq[i]] != (r'O|U|X'):
                r = r + code[seq[i]]
            else:
                break
        lenth = len(r)
        a = a + ('>' + n + '     ' + str(lenth) + '\n' + r + '\n')
        r = ''
file2.close()
file3.write(a)
file3.close()
file3 = open(file_result, 'r')
print(file3.read())
