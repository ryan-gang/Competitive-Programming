import random


# Runtime: 1688 ms, faster than 8.82%.
# Memory Usage: 61.8 MB, less than 7.29%.
class RandomizedSetNaive:
    """
    list.remove() is amortised O(N) time complexity. So this violates the requirement.
    Instead of list.remove(), we need to use list.pop() which is O(1).
    """

    def __init__(self):
        self.dataSet = set()
        self.dataList = list()

    def insert(self, val: int) -> bool:
        if val in self.dataSet:
            return False
        self.dataSet.add(val)
        self.dataList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dataSet:
            return False
        self.dataSet.remove(val)
        self.dataList.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.dataList)


# Runtime: 521 ms, faster than 83.46%.
# Memory Usage: 61.4 MB, less than 57.51%.
class RandomizedSet:
    """
    Instead of using list.remove(), we use list.pop().
    As pop only works on the last element we swap the element to be removed,
    and the last element, and then pop the last one.
    We also update the index of the swapped element in the dict.
    The dict keeps a mapping of value -> index in the list, specifically for this purpose.
    """

    def __init__(self):
        self.Dict = dict()  # Mapping of -> Value : it's index in list.
        self.List = list()

    def insert(self, val: int) -> bool:
        if val in self.Dict:
            return False
        self.Dict[val] = len(self.List)
        self.List.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.Dict:
            return False
        idx = self.Dict[val]  # Element to be popped is in this index.
        swapped_val = self.List[-1]  # This is the element in the last index.
        self.List[idx] = swapped_val  # We bring the swapped val in the index.
        self.Dict[swapped_val] = idx  # And update its dict mapping.
        self.List.pop()  # Now we pop the last index, index is overwritten with this value.
        del self.Dict[val]  # Delete dict entry for val.
        return True

    def getRandom(self) -> int:
        return random.choice(self.List)


if __name__ == "__main__":
    sol = RandomizedSet()
    print(sol.insert(0))
    print(sol.insert(1))
    print(sol.Dict, sol.List)
    print(sol.remove(0))
    print(sol.Dict, sol.List)
    print(sol.insert(2))
    print(sol.Dict, sol.List)
    print(sol.remove(1))
    print(sol.Dict, sol.List)
    print(sol.getRandom())
