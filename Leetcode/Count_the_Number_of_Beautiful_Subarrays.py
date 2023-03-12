class Solution:
    # T : O(N^2), S : O(1)
    # TLE. 99/114.
    def beautifulSubarrays1(self, nums: list[int]) -> int:
        """
        For a subarray to be beautiful, it has to have an even number of 1's.
        And from there we can XOR the values, and check if the XOR-ed value is 0.
        Iterate over the array, over all possible subarrays, and find XOR.
        If it is 0, increment the result.
        """
        n = len(nums)
        count = 0

        # Iterate over all possible subarrays
        for i in range(n):
            xor_sum = 0
            for j in range(i, n):
                # Calculate the XOR sum of the subarray
                xor_sum ^= nums[j]
                if xor_sum == 0:
                    count += 1

        return count

    # T : O(N), S : O(N)
    def beautifulSubarrays(self, nums: list[int]) -> int:
        """
        Instead of iterating over the array in 2 nested loops.
        We cache the XOR-ed value upto an index i.
        if XOR is 0, then we can directly add 1 to our output.
        Or, at another index j (j > i), if XORj == XORi,
        we can create a subarray from i to j, such that the XOR is 0.
        We can add all these subarrays (All subarrays with the XORj) to our result.
        """
        count = xor = 0
        xors: dict[int, int] = {0: 1}
        for val in nums:
            xor ^= val
            if xor in xors:
                count += xors[xor]
                xors[xor] += 1
            else:
                xors[xor] = 1

        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.beautifulSubarrays(nums=[4, 3, 1, 2, 4]) == 2
    assert sol.beautifulSubarrays(nums=[0, 0]) == 3
