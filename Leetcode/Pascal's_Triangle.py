class Solution:
    # T : O(N), S : O(1)
    def generate(self, numRows: int) -> list[list[int]]:
        triangle: list[list[int]] = []
        for i in range(numRows):  # For each row
            elements = i + 1
            if elements < 3:  # If less than 3 elements, add only 1's
                triangle.append([1] * elements)
            else:
                prev = triangle[i - 1]  # Else take previous row
                curr = [1]  # Add starting 1
                for b in range(1, len(prev)):
                    a = b - 1  # for every pair of elements add the sum to curr
                    curr.append(prev[a] + prev[b])
                curr.append(1)  # Add ending 1
                triangle.append(curr)  # Add current row
        return triangle
