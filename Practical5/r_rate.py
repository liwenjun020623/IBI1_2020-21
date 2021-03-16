n=84
r=float(input("the rate of reproduction of a virus is:")) #input the value of "r"
for i in range(0,5): #repeat the round for 5 times
    n=n*r+n
print("The total number of individuals infected after 5 generations is ",n)