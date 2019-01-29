#import modules
from time import time


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






#Testing
def performance():
    # Determine performance of contains algorithm
    n = 1024
    while n < 50000000:
        sorted = range(n)
        now = time()

        # Code whose performance is to be evaluated
        #contains(sorted, -1)
        bubbleSort(sorted)
        
        done = time()

        print(n, (done - now)*1000)
        n *= 2


performance()