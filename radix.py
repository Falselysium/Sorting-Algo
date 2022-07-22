import random
import time

def radix_sort(A):
    #Find the largest number in the list
    max_digit = max(A)
    #Find the number of digits in the largest number
    for i in range(len(str(max_digit))):
        #Sort the list using the 10**nith place digit
        A = counting(A,10**i)
    return A

def counting(A,n):
    sorted = [0 for i in range(len(A))]
    count = [0 for i in range(max(A)+1)]

    #Counting the number of times each number appears in the list
    for x in A:
        count[(x//n)%10]+=1

    #Adding the previous count to the next number
    for x in range(1,len(count)):
        count[x] += count[x-1]

    #Reverse A
    A = A[::-1]
    
    #print sorted list using the count list
    for x in A:
        sorted[count[(x//n)%10]-1] = x
        count[(x//n)%10] -=1
    return sorted
        
#Setting the N by changing the exponent for 10**
for i in range(1,7):
    maxvalue = 10**i
    print("N: ",maxvalue)
    list = [random.randint(1, maxvalue) for x in range(0, maxvalue)]
    start_time = time.time_ns()
    radix_sort(list)
    print(time.time_ns()-start_time, "nanoseconds")