from typing import List


# 9/15 TC passed for naive implementation, TLE.
class NumArrayNaive:
    def __init__(self, nums: List[int]):
        self.array = nums

    def update(self, index: int, val: int) -> None:
        self.array[index] = val

    def sumRange(self, left: int, right: int) -> int:
        val = 0
        for i in range(left, right + 1):
            val += self.array[i]

        return val


# 8/15 TC passed for prefix_sum implementation, TLE.
class NumArrayPrefixSum:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.prefix_sum = []
        self.n = len(nums)
        val = 0
        for i in nums:
            val += i
            self.prefix_sum.append(val)

    def update(self, index: int, val: int) -> None:
        diff = val - self.array[index]
        for idx in range(index, self.n):
            self.prefix_sum[idx] += diff
        self.array[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            left_val = 0
        else:
            left_val = self.prefix_sum[left - 1]
        return self.prefix_sum[right] - left_val


# 9/15 TC passed for prefix_sum plus a separate diff array, TLE.
class NumArray:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.prefix_sum = []
        self.n = len(nums)
        self.diff = [0 for _ in range(self.n)]
        val = 0
        for i in nums:
            val += i
            self.prefix_sum.append(val)

    def update(self, index: int, val: int) -> None:
        diff = val - self.array[index]
        self.diff[index] += diff
        self.array[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            left_val = 0
        else:
            left_val = self.prefix_sum[left - 1]
        total_diff = 0
        for idx in range(left, right + 1):
            total_diff += self.diff[idx]
        return self.prefix_sum[right] - left_val + total_diff


# obj = NumArray(nums=[1, 3, 5])
# print(obj.sumRange(0, 2))
# obj.update(1, 2)
# print(obj.sumRange(0, 2))

obj = NumArray(nums=[7, 2, 7, 2, 0])
obj.update(4, 6)
obj.update(0, 2)
obj.update(0, 9)
print(obj.sumRange(4, 4))
obj.update(3, 8)
print(obj.sumRange(0, 4))
obj.update(4, 1)
print(obj.sumRange(0, 3))
print(obj.sumRange(0, 4))
obj.update(0, 4)
# print(obj.array)
# print(obj.prefix_sum)
# print(obj.diff)
