from typing import List
from utils import format_solution, puzzle_input


def planned_course_2D(instructions: List[int]) -> int:
    x, y = (0, 0)
    directions = {"forward": (+1, 0), "down": (0, +1), "up": (0, -1)}

    for instruction in instructions:
        commands = instruction.split(" ")
        command = directions[commands[0]]
        value = int(commands[1])
        u, v = tuple([value * i for i in command])
        x, y = x + u, y + v

    return x * y


def planned_course_3D(instructions: List[int]) -> int:
    x, y, aim = (0, 0, 0)
    for instruction in instructions:
        directions = {
            "forward": (+1, aim, 0),
            "down": (0, 0, +1),
            "up": (0, 0, -1),
        }
        commands = instruction.split(" ")
        command = directions[commands[0]]
        value = int(commands[1])
        u, v, w = tuple([value * i for i in command])
        x, y, aim = x + u, y + v, aim + w

    return x * y


if __name__ == "__main__":
    instructions = [line for line in puzzle_input(2021, 2)]

    solutions = format_solution(
        solver_p1=lambda: planned_course_2D(instructions),
        solver_p2=lambda: planned_course_3D(instructions),
    )
    print(solutions)
