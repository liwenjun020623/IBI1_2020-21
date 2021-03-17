import numpy as np
import matplotlib.pyplot as plt
dict = {"USA": 29862124, "India": 11285561,"Brazil": 11205972, "Russia": 4360823,"UK": 4234924}
# output the dictionary
print(dict)
# change the keys and values of the dictionary into 2 arrays
labels = np.array([i for i in dict.keys()])
data = np.array([j for j in dict.values()])
plt.pie(data, labels=labels, shadow=True, autopct='%1.1f%%')
plt.title("Coronavirus Infection Rates across 5 Countries")
plt.show()# draw and output the pie chart