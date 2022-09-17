from typing import List
from utils import format_solution, puzzle_input


def count_increases(depths: List[int]) -> int:
    """
    Count the number of times the value increases
    between two consecutive measurements
    """

    count = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            count += 1

    return count


def count_sliding_increases(depths: List[int]) -> int:
    """
    Count the number of times the value increases
    between two consecutive measurements, where the
    measurement is the sum of 3 consecutive values.
    """
    # * Comparing (A + B + C) with (B + C + D) is the same as comparing A and D.
    count = 0
    for i in range(3, len(depths)):
        if depths[i] > depths[i - 3]:
            count += 1

    return count


if __name__ == "__main__":
    depths = [int(line) for line in puzzle_input(2021, 1)]

    solutions = format_solution(
        solver_p1=lambda: count_increases(depths),
        solver_p2=lambda: count_sliding_increases(depths),
    )
    print(solutions)
