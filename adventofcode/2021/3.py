from collections import Counter, defaultdict
from typing import List
from utils import format_solution, puzzle_input


def binary_diagnostic(instructions: List[int]) -> int:
    N, n = len(instructions), len(instructions[0])
    totalCounter = Counter(
        dict(zip([_ for _ in range(n)], [0 for j in range(n)]))
    )

    for i in instructions:
        innerCounter = Counter(
            dict(
                zip(
                    [_ for _ in range(n)],
                    [int(j) for j in i],
                )
            )
        )
        totalCounter += innerCounter

    gamma = [0] * n
    epsilon = [0] * n

    for key in totalCounter:
        index, digit = key, totalCounter[key]
        if digit > N // 2:
            gamma[index] = "1"
            epsilon[index] = "0"
        else:
            gamma[index] = "0"
            epsilon[index] = "1"
    return (int("".join(gamma), 2)) * (int("".join(epsilon), 2))


def oxy_gen_rating(instructions):
    n = len(instructions[0])
    index_in_consideration = 0

    while index_in_consideration < n and len(instructions) > 1:
        counter = defaultdict(list)
        for i in instructions:
            counter[i[index_in_consideration]].append(i)

        if len(counter["0"]) > len(counter["1"]):
            instructions = counter["0"]
        else:
            instructions = counter["1"]

        index_in_consideration += 1

    if len(instructions) > 1:
        raise IndexError("More than 1 element.")
    oxy_gen_rating = int(instructions[0], 2)
    return oxy_gen_rating


def co2_scrub_rating(instructions):
    n = len(instructions[0])
    index_in_consideration = 0

    while index_in_consideration < n and len(instructions) > 1:
        val = defaultdict(list)
        for i in instructions:
            val[i[index_in_consideration]].append(i)

        if len(val["0"]) <= len(val["1"]):
            instructions = val["0"]
        else:
            instructions = val["1"]

        index_in_consideration += 1

    if len(instructions) > 1:
        raise IndexError("More than 1 element.")
    c02_scrub_rating = int(instructions[0], 2)
    return c02_scrub_rating


def life_support_rating(instructions: List[int]) -> int:
    return oxy_gen_rating(instructions) * co2_scrub_rating(instructions)


if __name__ == "__main__":
    instructions = [line for line in puzzle_input(2021, 3)]

    solutions = format_solution(
        solver_p1=lambda: binary_diagnostic(instructions),
        solver_p2=lambda: life_support_rating(instructions),
    )
    print(solutions)
