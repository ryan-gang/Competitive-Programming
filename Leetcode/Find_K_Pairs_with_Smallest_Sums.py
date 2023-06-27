from heapq import heappush, heappop


class Solution:
    # T : O(MNLog(MN)), S : O(MN)
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[tuple[int, int]]:
        n1, n2 = len(nums1), len(nums2)
        i = j = 0

        heap: list[tuple[int, int, int]] = []
        visited: set[tuple[int, int]] = set()
        all_pairs: list[tuple[int, int]] = []

        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add(tuple((0, 0)))

        while k > 0 and heap:
            _, i, j = heappop(heap)
            all_pairs.append((nums1[i], nums2[j]))
            k -= 1
            if i + 1 < n1 and (t1 := (i + 1, j)) not in visited:
                entry1 = (nums1[i + 1] + nums2[j], i + 1, j)
                heappush(heap, entry1)
                visited.add(t1)
            if j + 1 < n2 and (t2 := (i, j + 1)) not in visited:
                entry2 = (nums1[i] + nums2[j + 1], i, j + 1)
                heappush(heap, entry2)
                visited.add(t2)
        print(all_pairs)
        return all_pairs


if __name__ == "__main__":
    sol = Solution()
    assert sol.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3) == [(1, 2), (1, 4), (1, 6)]
    assert sol.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2) == [(1, 1), (1, 1)]
    assert sol.kSmallestPairs(nums1=[1, 2], nums2=[3], k=3) == [(1, 3), (2, 3)]
    assert sol.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=10) == [
        (1, 1),
        (1, 1),
        (1, 2),
        (1, 2),
        (2, 1),
        (1, 3),
        (1, 3),
        (2, 2),
        (2, 3),
    ]
