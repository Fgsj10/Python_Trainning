"""
Author = Francisco Junior
"""

#Creating algorithm of Selection sort

import sys

#Creating array with values
array = [5,32,12,10,9,58]

for i in range(len(array)):
    minimun_idx = i
    for j in range(i+1, len(array)):
        if array[minimun_idx] > array[j]:
            minimun_idx = j

    array[i], array[minimun_idx] = array[minimun_idx], array[i]


#Printing array values sorted

print("Array sorted")

for x in range(len(array)):
    print("%d" %(array[x]))
