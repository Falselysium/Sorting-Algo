from math import inf
from math import floor, ceil
import random
import time


def MergeSort(array, left, right):
    if len(array) > 1:
        mid = floor(len(array)//2)
        L1 = MergeSort(array[:mid], 0, mid)
        L1.append(inf)
        L2 = MergeSort(array[mid:], mid, len(array))
        L2.append(inf)
        
        # index for L1 and L2
        i1, i2 = 0, 0
        for _ in range(len(array)):
            if L1[i1] <= L2[i2]:
                array[_] = L1[i1]
                i1 += 1
            else:
                array[_] = L2[i2]
                i2 += 1
    return array


#Setting the N by changing the exponent for 10**
for i in range(1,7):
    maxvalue = 10**i
    print("N: ",maxvalue)
    list = [random.randint(1, maxvalue) for x in range(0, maxvalue)]
    start_time = time.time_ns()
    MergeSort(list, 0, len(list))
    print(time.time_ns()-start_time, "nanoseconds")