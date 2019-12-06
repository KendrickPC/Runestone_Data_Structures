# 3.11 Programming Exercises
'''
1. Devise an experiment to verify that the list index operator is 𝑂(1).

2. Devise an experiment to verify that get item and set item are 𝑂(1) for dictionaries.

3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.

4. Given a list of numbers in random order, write an algorithm that works in 𝑂(𝑛log(𝑛)) to find the kth smallest number in the list.

5. Can you improve the algorithm from the previous problem to be linear? Exp
'''

import time
from matplotlib import pyplot as plt
import random

def empty(*args):
    pass

def list_index_operation(alist, index):
    alist[index]

def dictionary_get_operation(adict, index):
    adict.get(index)

def del_in_list(alist, index):
    del alist[index]

def del_in_dict(alist, key):
    del adict[key]

if __name__ == '__main__':
    maxN = []
    y1 = []
    y2 = []
    for i in range(1, 100000, 100):
        maxN.append(i)


# 1. Devise an experiment to verify that the list index operator is 𝑂(1).
# for n in maxN:
#     alist = range(n)
#     random_index = random.randint(0, n-1)
#     start1 = time.time()
#     for repeat in range(100):
#         list_index_operation(alist, random_index)
#     end1 = time.time()

#     start2 = time.time()
#     for repeat in range(100):
#         empty(alist, random_index)
#     end2 = time.time()

#     y1.append(end1-start1-(end2-start2))

# plt.plot(maxN, y1)
# plt.show()

# 2. Devise an experiment to verify that get item and set item are 𝑂(1) for dictionaries.

# for n in maxN:
#     adict = {}
#     for j in range(n):
#         adict[j] = None

#     random_index = random.randint(0, n-1)
#     start1 = time.time()
#     for repeat in range(100):
#         dictionary_get_operation(adict, random_index)
#     end1 = time.time()

#     start2 = time.time()
#     for repeat in range(100):
#         empty(adict, random_index)
#     end2 = time.time()

#     y1.append(end1 - start1 - (end2 - start2))

# plt.plot(maxN, y1)
# plt.show()


# 3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.

# for n in maxN:
#     alist = range(n)
#     adict = {}
#     for j in xrange(n):
#         adict[j] = None
#     random_index = random.randint(0, n-1)

#     start1 = time.time()
#     del_in_list(alist, random_index)
#     end1 = time.time()

#     start2 = time.time()
#     del_in_dict(adict, random_index)
#     end2 = time.time()

#     start3 = time.time()
#     empty(adict, random_index)
#     end3 = time.time()

#     y1.append(end1 - start1 - (end3 - start3))
#     y2.append(end1 - start1 - (end3 - start3))

# plt.plot(maxN, y1, "r--", maxN, y2)
# plt.show()

# 4. Given a list of numbers in random order, write an algorithm that works in 𝑂(𝑛log(𝑛)) to find the kth smallest number in the list.

import heapq

def getsmallest(arr, k):
    m = [-x for x in l[:k]]
    heapq.heapify(m)
    for num in arr[5:]:
        print(num, m)
        heapq.heappush(m, max(-num, heapq.heappop(m)))
    return m


if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    print(getsmallest(l, 5))

# 5. Can you improve the algorithm from the previous problem to be linear? Exp

# No, I cannot.















