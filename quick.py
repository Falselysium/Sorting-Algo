import time
import random

def quicksort(A,p,r):
    if (p<r) :
        #Taking the partition
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r) 
    return A
        
def partition(A,p,r):
    #pivot is last value
    pivot = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= pivot:
            i += 1
            A[i],A[j] = A[j],A[i] 
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

#Setting the N by changing the exponent for 10**
for i in range(1,7):
    maxvalue = 10**i
    print("N: ",maxvalue)
    list = [random.randint(1, maxvalue) for x in range(0, maxvalue)]
    start_time = time.time_ns()
    quicksort(list,0,len(list)-1)
    print(time.time_ns()-start_time, "nanoseconds")

        