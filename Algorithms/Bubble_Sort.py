"""
Author= Francisco Junior
"""

#Creating algorithm Bubble Sort

def bubblesort(arr):
    n = len(arr)

    #Checking and runner all values in array
    for x in range(n):
        for j in range(n-x-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


#Testing logical of algorithm

arr = [15,18,16,14,9,6,31,47]

#Calling method bubble sort with values
bubblesort(arr)

#Printing all values sorted
print("List sorted with algorithm bubble sort")

for x in range(len(arr)):
    print("%d" %arr[x])


