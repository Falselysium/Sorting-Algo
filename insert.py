import random
import time

start_time = time.time_ns()
maxvalue = 100

# Gives me a Random list of numbers to be sorted
list = [random.randint(1, maxvalue) for x in range(0, maxvalue)]
print(list)

def insertion(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A

print(insertion(list))

print(time.time_ns()-start_time, "nanoseconds")