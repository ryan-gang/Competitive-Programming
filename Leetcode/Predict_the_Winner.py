from functools import cache


class Solution:
    """
    At every index, we run simulations of what would happen if player takes
    first and player takes last index. In Player1's turn he will win if any of
    the last or first index moves make his final score higher. But in player2's
    turn player1 will win iff his score is higher from both moves.
    """
    # ToDo : NEEDS IMPROVEMENT. DP implementation.

    # T : O(2^N), S: O(N)
    # But as we are @cache-ing T goes down to O(N^2).
    def PredictTheWinner(self, nums: list[int]) -> bool:
        @cache
        def predict(i: int, j: int, score_1: int, score_2: int, turn: int) -> bool:
            # Predict if person 1 can win.
            # Array elements from i to j are allowed.
            # turn can be only 1 or 2.
            if i > j:
                return score_1 >= score_2
            if turn == 1:
                front = predict(i + 1, j, score_1 + nums[i], score_2, 2)
                back = predict(i, j - 1, score_1 + nums[j], score_2, 2)
                return front or back
            else:
                front = predict(i + 1, j, score_1, score_2 + nums[i], 1)
                back = predict(i, j - 1, score_1, score_2 + nums[j], 1)
                return front and back

        X = predict(i=0, j=len(nums) - 1, score_1=0, score_2=0, turn=1)
        return X


if __name__ == "__main__":
    sol = Solution()
    assert not sol.PredictTheWinner(nums=[1, 5, 2])
    assert sol.PredictTheWinner(nums=[1, 5, 233, 7])
