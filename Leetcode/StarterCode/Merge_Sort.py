import random
from typing import List


class Sort(object):
    """
    Divide and conquer implementation of merge sort.
    T : O(NLogN), S : O(N)
    Ref : https://developer.nvidia.com/blog/merge-sort-explained-a-data-scientists-algorithm-guide/
    Time Complexity : https://www.khanacademy.org/computing/computer-science
    /algorithms/merge-sort/a/analysis-of-merge-sort
    merge() is O(N) time.
    And at every level, there are k separate merges done, each are of N / k size.
    So time complexity of merge at every level is O(N), and there are LogN levels.
    """

    @staticmethod
    def merge_sort(array: List[int]) -> List[int]:
        n = len(array)
        if n == 1:
            return array

        mid = n // 2
        left, right = Sort.merge_sort(array[:mid]), Sort.merge_sort(array[mid:])
        return Sort.merge((left), (right))

    @staticmethod
    def merge(left: List[int], right: List[int]) -> List[int]:
        i = j = 0
        m, n = len(left), len(right)
        out = []
        while i < m and j < n:
            if left[i] <= right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1

        out.extend(left[i:])
        out.extend(right[j:])

        return out


if __name__ == "__main__":
    sort = Sort()
    A = [random.randint(1, 100) for _ in range(10)]
    out = sort.merge_sort(A)
    A.sort()
    assert out == A
    print(out)
