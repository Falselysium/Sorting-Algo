from math import inf
from math import floor, ceil
import random
import time

# Get the RunTime
start_time = time.time_ns()

maxvalue = 100

# Gives me a Random list of numbers to be sorted
list = [random.randint(1, maxvalue) for x in range(0, maxvalue)]
print(list)

def MergeSort(array, left, right):
    if len(array) > 1:
        mid = floor(len(array)//2)
        
        L1 = MergeSort(array[:mid], 0, mid)
        L1.append(inf)
        L2 = MergeSort(array[mid:], mid, len(array))
        L2.append(inf)
        # print(array,L1,L2)
        # index for L1 and L2
        i1 = 0
        i2 = 0
        for _ in range(len(array)):
            if L1[i1] <= L2[i2]:
                array[_] = L1[i1]
                i1 += 1
            else:
                array[_] = L2[i2]
                i2 += 1
        print("ARRAY----", array,"\n")
    return array


MergeSort(list, 0, len(list)-1)

print("--- ",time.time_ns() - start_time," nanoseconds ---")
