from os import path
from time import perf_counter
from typing import Any, Callable


def puzzle_input(year: int, day: int):
    """
    Open a puzzle's input file, which should be saved under
    ``advent_of_code/y{year}/data/day{day}``
    """

    location = path.join("G://Coding//adventofcode//", f"{year}/data/{day}.txt")
    print(f"Day: {day}")
    with open(location, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


class Timer:
    def __enter__(self):
        self._start_time = perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.result_seconds = perf_counter() - self._start_time


def format_part(part: int, solver: Callable[[], Any]) -> str:
    """
    Format the solution to a part in a standardized way, with timing info
    """
    with Timer() as t:
        solution = solver()
    return f"Part {part!r}: {solution!r} ({t.result_seconds:.6f} sec)"


def format_solution(
    solver_p1: Callable[[], Any], solver_p2: Callable[[], Any]
) -> str:
    """
    Format the solutions to both parts of a puzzle in a standardized way,
    with timing info for each part individually
    """
    return "\n".join([format_part(1, solver_p1), format_part(2, solver_p2)])


# Ref : https://github.com/k2bd/advent-of-code/
# blob/7912691a08576fb12815110c2b073b4e794042d8/src/advent_of_code/util.py#L7
