import heapq

nums = [3, 2, 1, 5, 6, 4]
k = 2


def findKthLargest(nums, k):
    return sorted(nums)[-k]


heapq.heapify(nums)
for _ in range((len(nums) - k)):
    heapq.heappop(nums)
A = heapq.heappop(nums)
  