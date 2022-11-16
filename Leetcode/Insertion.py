# CTCI 5.1
class Solution:
    @staticmethod
    def insertion(M, N, i, j):
        # The ith bit to jth bit in N has to be set to 1s.
        length = 8  # Get length.
        mask = (1 << (length + 1) - 1) - ((1 << (i)) - 1)
        N_masked = N & mask  # 10111100
        M_mask = M << i
        final = N_masked & M_mask
        print(bin(final))
        return final


if __name__ == "__main__":
    sol = Solution()
    assert bin(sol.insertion(M=1001, N=10010100, i=2, j=5)) == "0b10100100"
