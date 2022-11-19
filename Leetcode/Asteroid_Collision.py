from collections import deque
from typing import List


class Solution:
    """
    Take note, that the sign denotes which way the asteroid is moving.
    Push all asteroids into a stack, compare with topmost value in stack, if moving in different
    direction, pop the smaller one. If both equal pop both.
    """

    # Runtime: 162 ms, faster than 72.88%.
    # Memory Usage: 15.2 MB, less than 27.61%.
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()

        for asteroid in asteroids:
            while stack:
                if stack[-1] > 0 > asteroid:
                    if abs(stack[-1]) > abs(asteroid):
                        break
                    elif abs(stack[-1]) < abs(asteroid):
                        stack.pop()
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(asteroid)
                    break
            else:
                stack.append(asteroid)

        return list(stack)

    def asteroidCollisionConcise(self, asteroids: List[int]) -> List[int]:
        stack = deque()

        for asteroid in asteroids:
            while stack and stack[-1] > 0 > asteroid:
                if (stack[-1]) < -(asteroid):
                    stack.pop()
                    continue
                elif (stack[-1]) == -(asteroid):
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return list(stack)


if __name__ == "__main__":
    sol = Solution()
    assert sol.asteroidCollision(asteroids=[-2, -1, 1, 2]) == [-2, -1, 1, 2]
    assert sol.asteroidCollision(asteroids=[5, 10, -5]) == [5, 10]
    assert sol.asteroidCollision(asteroids=[8, -8]) == []
    assert sol.asteroidCollision(asteroids=[10, 2, -5]) == [10]
    assert sol.asteroidCollision(asteroids=[4, 2, -5]) == [-5]
