"""
Timeit module.
"""
import random
import timeit


# Test method will be executed by timeit cli and api both.
def sample_func(n: int):
    for _ in range(n):
        random.randint(1, 100)


if __name__ == "__main__":
    # While executing file as py script.
    print(timeit.timeit("sample_func(10000)", setup="from __main__ import sample_func", number=10))

    # From CLI.
    # python -m timeit -v -n 10 -s "from meta import sample_func" "sample_func(100000)"
    # -s "setup statement" "test statement"
    # -n is optional. Python automatically adjusts n.
