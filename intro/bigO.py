#import modules
from time import time
from random import shuffle


#1.
# O(1) An algorithm that executes in the same amount of time regardless of data
# An example is adding an item to an array
# No matter how large the array is It would still take the algorithm the same time to add items to the array
myList = [1,2,3,4,5]

def pushToArray(arr, item):
    arr.append(item)
    print(arr)

#pushToArray(myList, 6)




#2.
# O(N) An algorithm whose completion time is directly proportional to the amount of data
# An example here is a linear search, if we had to find an element in an array we would have to look through each element in the array
# It would make a difference if we had a 10 item array or a 50,000 item array

def contains(myArray, searchItem):
    return searchItem in myArray
 

# As the size of our array increases we notice an increase in time
# Array Length , Time To Search
# (1024, 0.01811981201171875)
# (2048, 0.050067901611328125)
# (4096, 0.09894371032714844)
# (8192, 0.2560615539550781)
# (16384, 0.36597251892089844)
# (32768, 1.0979175567626953)
# (65536, 2.0399093627929688)
# (131072, 4.179954528808594)
# (262144, 5.028963088989258)
# (524288, 10.210990905761719)
# (1048576, 12.657880783081055)
# (2097152, 22.135019302368164)
# (4194304, 51.85198783874512)
# (8388608, 82.4270248413086)
# (16777216, 175.56500434875488)
# (33554432, 447.23987579345703)




#3.
# O(N^2) The time the algorithm takes to complete would be proportional to the square of the amount of data
# This usually happens with algorithms that have nested iterations
# every cycle through the outer loop requires a complete cycle of the inner loop
# an example is the bubble sort algorithm

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


# Array Size, Time To Sort
# (1024, 63.745975494384766)
# (2048, 146.10910415649414)
# (4096, 494.51398849487305)
# (8192, 2084.481954574585)
# (16384, 7821.044206619263)
# (32768, 29213.681936264038)
# (65536, 112555.25803565979)
# (131072, 474491.5862083435)
# (262144, 1941134.1590881348)
# (524288, 7969213.345050812)
# With the linear search we didnt see much difference btn the time as the array size grew
# With the bubble sort we see much greater difference
# The bubble sort is very slow as the amount of data increases
# O(N^2) is very bad and must be avoided




#4.
# O(log N) This occurs when data being used is decreased roughly by 50% each time we parse through using the algorithm
# An example of log N behaviour is the binary array search
# However we need to sort tthe items in our list first before we can do a binary array search
# We would use the bubble sort algorithm here because we already have it but it would be much effecient to use
# a selection sort or quick sort to improve performance

def bs_contains(myList, searchItem):
    # sortedList = bubbleSort(myList) We would need to sort but in our case our test data is already sorted
    length = len(myList)
    lowestPoint = 0
    highestPoint = length - 1

    while lowestPoint <= highestPoint:
        midpoint = (lowestPoint + highestPoint)/2
        if searchItem == myList[midpoint]:
            return midpoint
        elif searchItem < myList[midpoint]:
            highestPoint = midpoint - 1
        else:
            lowestPoint = midpoint + 1
    return -(lowestPoint + 1)

# Array Size, Time To Search
# (1024, 0.0059604644775390625)
# (2048, 0.0069141387939453125)
# (4096, 0.0059604644775390625)
# (8192, 0.0059604644775390625)
# (16384, 0.03600120544433594)
# (32768, 0.018835067749023438)
# (65536, 0.028133392333984375)
# (131072, 0.03910064697265625)
# (262144, 0.015020370483398438)
# (524288, 0.017881393432617188)
# (1048576, 0.012874603271484375)
# (2097152, 0.013828277587890625)
# (4194304, 0.014066696166992188)
# (8388608, 0.03504753112792969)
# (16777216, 0.01811981201171875)
# (33554432, 0.0171661376953125)
# The increase in data had very little effect on the time it took to search through the array
# All we had to do was take one extra step and we decreased the problem by half






#5.
# O(n log n) Most sorting algorithms we hav looked at so far have O(N), this is because to properly sort an array
# we need to go through each element at least once to properly sort our items 
# Algorithtms like tthe quick sort only compare values once unlike the bubblesort where values are compared over and over again
# Each parse reduces the possible final sorted list in half
# In other words O(log n!) => factorial of n on each parse
# log n + log n-1 ... + log 1 
# this is equal to n log n


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark




#Testing
def performance():
    # Determine performance of contains algorithm
    n = 1024
    while n < 50000000:
        sorted = range(n) # sorted array
        shuffle(sorted) # unsort array for quick sort
        
        now = time()

        # Code whose performance is to be evaluated
        #contains(sorted, -1)
        #bubbleSort(sorted)
        #bs_contains(sorted, -1)
        quickSort(sorted)
        
        done = time()

        print(n, (done - now)*1000)
        n *= 2


performance()