from collections import defaultdict


# Variable length sliding window.
def func(arr: list[int]) -> int:
    d: dict[int, int] = defaultdict()
    lo = hi = max_num = 0
    K = 2

    while hi < len(arr):
        # 1) add a new value to the sliding window
        d[arr[hi]] += 1
        hi += 1
        # 1.1) increase hi immediately
        # 2) 'repair' the window if it violates the constraints
        while len(d) > K:
            d[arr[lo]] -= 1
            # remove a value from the sliding window
            if d[arr[lo]] == 0:
                del d[arr[lo]]
            lo += 1
        # 3) at this point you know that your sliding window is always valid
        # check condition min/max/whatever
        # here you already have proper count

        max_num = max(max_num, hi - lo)

    return max_num


# Fixed length sliding window.
def func1(arr: list[int]) -> int:
    def handle(char: int, addition: bool = True):
        # For every element in arr, this method will be called. Can be as simple
        # as just d[char] += 1, but also can be very complex. Useful to keep the
        # complexity separate.
        condition = 1 if addition else -1
        d[char] += 1 * condition

    d: dict[int, int] = defaultdict()
    K = 2
    lo, hi = 0, K

    for i in range(K):
        handle(arr[i])

    max_num = d[arr[0]]

    while hi < len(arr):
        # 1) add a new value to the sliding window
        handle(arr[hi])
        handle(arr[lo], addition=False)
        lo, hi = lo + 1, hi + 1
        # 1.1) increase hi immediately
        # 3) at this point you know that your sliding window is always valid
        # check condition min/max/whatever
        # here you already have proper count

        max_num = max(max_num, hi - lo)

    return max_num
