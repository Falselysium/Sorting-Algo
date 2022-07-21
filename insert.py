import random
import time



def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A


#Setting the N by changing the exponent for 10**
for i in range(1,7):
    maxvalue = 10**i
    print("N: ",maxvalue)
    list = [random.randint(1, maxvalue) for x in range(0, maxvalue)]
    start_time = time.time_ns()
    insertion_sort(list)
    print(time.time_ns()-start_time, "nanoseconds")
