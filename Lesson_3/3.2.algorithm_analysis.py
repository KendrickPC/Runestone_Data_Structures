import time

print("\nExample 1:")
def sumOfN2(n):
    start = time.time()

    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i

    end = time.time()

    return theSum,end-start

print(sumOfN2(10))
print(sumOfN2(10000))
print(sumOfN2(100000))
print(sumOfN2(1000000))


print("\nExample 2:")
# Without Iterating
def sumOfN3(n):
    start = time.time()
    answer = (n*(n+1))/2
    end = time.time()
    return answer, end-start

print(sumOfN3(10))
print(sumOfN3(10000))
print(sumOfN3(100000))
print(sumOfN3(1000000))
