from collections import deque

d = {}


def sequence(n):
    if n == 1:
        return 1
    else:
        if n % 2:
            return (3 * n) + 1
        else:
            return n // 2


while 1:
    inputData = input()
    if inputData == "":
        break
    A, B = [int(i) for i in inputData.split(" ")]
    maxCycleLength = -1
    for n in range(A, B + 1):
        setFlag = False
        stack = deque()
        stack.append(n)
        cycleLength = 1
        while n != 1:
            if n in d:
                # print(f"Got it : {n}, saved : {d[n] } iterations")
                cycleLength += d[n] - 1
                setFlag = True
                break
            else:
                val = sequence(n)
                # print(val)
                n = val
                stack.append(n)
                cycleLength += 1

        if not setFlag:
            count = 1
            while stack:
                val = stack.pop()
                d[val] = count
                count += 1
        else:
            count = cycleLength - len(stack) + 1
            while stack:
                val = stack.pop()
                d[val] = count
                count += 1

        maxCycleLength = max(maxCycleLength, cycleLength)
    print(A, B, maxCycleLength)
