from time import time
from efficientSearching import bs_contains

def contains(collection, target):
    return target in collection

def performance():
    # Determine performance of contains algorithm
    n = 1024
    while n < 50000000:
        sorted = range(n)
        now = time()

        # Code whose performance is to be evaluated
        bs_contains(sorted, -1)
        #contains(sorted, -1)
        
        done = time()

        print(n, (done - now)*1000)
        n *= 2


performance()