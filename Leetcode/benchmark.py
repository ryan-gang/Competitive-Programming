import copy
import random
import time
from statistics import mean

copytimes = []
splicetimes = []
for _ in range(10):
    start = time.time()
    loops = 1000
    array_size = 100
    for i in range(loops):
        A = [random.randint(0, array_size) for i in range(array_size)]
        B = copy.deepcopy(A)
    end = time.time()
    time_val = (end - start) * 1000
    print(f"Time taken : {time_val} ms for {loops} loops")
    copytimes.append(time_val)

    start = time.time()
    for i in range(loops):
        A = [random.randint(0, array_size) for i in range(array_size)]
        B = A[::]
    end = time.time()
    time_val = (end - start) * 1000
    print(f"Time taken : {time_val} ms for {loops} loops")
    splicetimes.append(time_val)

print(copytimes)
print(splicetimes)
print(mean(copytimes))
print(mean(splicetimes))

# A[::] is faster than copy.deepcopy
# 139ms compared to 209ms.
# 50% higher times on average.
