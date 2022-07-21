from heapq import heapify
import random
import time


maxvalue = 10

list = [random.randint(1, maxvalue) for x in range(0, maxvalue)]
# print(list)

def heap_sort(A):
    size = len(A)
    max_heap(A,size)
    
    #Decrease the heap/array by one after every sort
    for i in range(size-1 , 0, -1):
        swap(A, i, 0)
        heapify(A, i, 0)
    return A

#Build Max_heap
def max_heap(A,size):
    for i in range ((size//2) -1 , -1, -1):
        heapify(A, size, i) 

#Heapify the heap after remove/swapping the biggest number.
def heapify(A, size, r):
    largest = r
    left = 2*r+1
    right = 2*r+2
    #Finds the largest value's index 
    if left < size and A[r] < A[left]:
        largest = left
    if right < size and A[largest] < A[right]:
        largest = right
    if largest != r:
        swap(A, r, largest)
        heapify(A, size, largest)

def swap(A, r, largest):
    temp = A[r]
    A[r] = A[largest]
    A[largest] = temp


#Setting the N by changing the exponent for 10**
for i in range(1,7):
    maxvalue = 10**i
    print("N: ",maxvalue)
    list = [random.randint(1, maxvalue) for x in range(0, maxvalue)]
    start_time = time.time_ns()
    heap_sort(list)
    print(time.time_ns()-start_time, "nanoseconds")



