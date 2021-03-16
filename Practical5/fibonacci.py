x,y=1,1 # The first two number of the sequence
print(x)
print(y)
for i in range(1,12):  # Make sure that the amount of numbers output is 13.
    if(i%2==1): # x and y are assigned alternately so we need to specify their order by using "if".
        x=x+y
        print(x)
    else:
        y=x+y
        print(y)

