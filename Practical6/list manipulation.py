import numpy as np
import matplotlib.pyplot as plt
gene_lengths = [9410, 394141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 15981]
exon_counts = [51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523]
# create 2 lists
lengths_array = np.array(gene_lengths)
counts_array = np.array(exon_counts)
# change the lists to 2 arrays
sorted_average_length_array = sorted(lengths_array/counts_array)
# calculate the average length and store in a new array
print(list(sorted_average_length_array))
plt.boxplot(sorted_average_length_array, labels="X")
plt.title("Exon Lengths")
plt.show()# draw and output the boxplot