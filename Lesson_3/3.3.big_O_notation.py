"""
Self Check

Write two Python functions to find the minimum number in a list.
    
    The first function should compare each number to every other number
    on the list. 𝑂(𝑛^2).

    The second function should be linear 𝑂(𝑛).
"""
import time
from random import randrange


def findMin_1(alist):
    overallMin = alist[0]

    for i in alist:
        isSmallest = True
        for j in alist:
            if i > j:
                isSmallest = False
        if isSmallest:
            overallMin = i

    return overallMin

# print(findMin([15, 42, 21, 71, 8]))

'''
Why is this O(n^2)? Because of the nested loops. 

'''

'''
for listSize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin_1(alist))
    end = time.time()
    print("Size: %d, Time: %f" % (listSize, end-start))
'''

# Linear Function
def findMin_2(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar


for listSize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin_2(alist))
    end = time.time()
    print("Size: %d, Time: %f" % (listSize, end-start))

