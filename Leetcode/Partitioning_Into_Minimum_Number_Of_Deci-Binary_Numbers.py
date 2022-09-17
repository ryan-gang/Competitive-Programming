from typing import List


# Assume max digit in n is x.
# Because deci-binary only contains 0 and 1,
# we need at least x numbers to sum up a digit x.
# Can do with more numners also, addition will generate a carry, but we will not get any benefits.
# So the earlier concept is optimal.
class Solution:
    # Runtime: 70 ms, faster than 89.12% of Python3 online submissions...
    # Memory Usage: 14.7 MB, less than 50.25% of Python3 online submissions...
    def minPartitions(self, n: str) -> int:
        return int(max(n))

    def getAllDeciBinaries(self, n: str) -> List[str]:
        deciBinaries = []
        while int(n) > 0:
            # For every iteration create a new deciBinary
            deciBinary = ""
            # For every digit in our number
            for i in n:
                # If the digit is > 0
                # We set the corresponding digit in our deciBinary as 1
                if i > "0":
                    deciBinary += "1"
                # else if it is 0, then we don't need to subtract anything more from it
                # Even if we try, the digit will go back around to 9
                # and we will have to subtract even more numbers
                # Which will not be optimal
                else:
                    deciBinary += "0"
            deciBinaries.append(deciBinary)
            n = str(int(n) - int(deciBinary))

        return deciBinaries


sol = Solution()
print(sol.minPartitions(n="27346209830709182346"))
