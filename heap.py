from heapq import heapify
import math
import random

maxvalue = 10

list = [random.randint(1, maxvalue) for x in range(0, maxvalue)]
print(list)

def heap_sort(A):
    size = len(A)
    max_heap(A,size)
    for i in range(size-1 , 0, -1):
        swap(A, i, 0)
        heapify(A, i, 0)
      
def max_heap(A,size):
    for i in range ((size//2) -1 , -1, -1):
        heapify(A, size, i) 
        
def heapify(A, size, r):
    largest = r
    left = 2*r+1
    right = 2*r+2
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


heap_sort(list)
print(list)



