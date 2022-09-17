from utils import format_solution, puzzle_input

arepl_filter = ["A", "bingo_tables", "instructions", "random_draw", "data"]


def get_data(instructions):
    all_data = []
    x_max, y_max = 0, 0
    for row in instructions:
        inner = []
        data = row.split(" -> ")
        for _ in data:
            _ = _.split(",")
            inner.extend(_)
        x1, y1, x2, y2 = (
            int(inner[0]),
            int(inner[1]),
            int(inner[2]),
            int(inner[3]),
        )
        x_max, y_max = max(x_max, x1, x2), max(y_max, y1, y2)
        all_data.append([x1, y1, x2, y2])
    return all_data, [x_max, y_max]


def check_equation(x1, y1, x2, y2, X, Y):
    m = (y2 - y1) / (x2 - x1)
    equation = (Y - y2) - m * (X - x2)
    return equation == 0


def intersections_horizontal_vertical(instructions):
    data, dims = get_data(instructions)
    x_max, y_max = dims
    grid = [[0] * (x_max + 1)] * (y_max + 1)
    grid = []
    for i in range(y_max + 1):
        inner = []
        for i in range(x_max + 1):
            inner.append(0)
        grid.append(inner)

    for coordinates in data:
        x1, y1, x2, y2 = coordinates
        if x1 == x2:
            for _ in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][_] += 1
        elif y1 == y2:
            for _ in range(min(x1, x2), max(x1, x2) + 1):
                grid[_][y1] += 1
        else:
            # Not horizontal or vertical line
            continue

    intersections = 0
    for row in grid:
        for cell in row:
            if cell > 1:
                intersections += 1

    return intersections


def b():
    pass


if __name__ == "__main__":
    instructions = puzzle_input(2021, 5)
    # bingo_tables, random_draw = get_data(instructions)

    solutions = format_solution(
        solver_p1=lambda: intersections_horizontal_vertical(instructions),
        solver_p2=lambda: b(),
    )
    print(solutions)

A = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split(
    "\n"
)


data, dims = get_data(instructions)
x_max, y_max = dims
grid = []
for i in range(y_max + 1):
    inner = []
    for i in range(x_max + 1):
        inner.append(0)
    grid.append(inner)

for coordinates in data:
    x1, y1, x2, y2 = coordinates
    if x1 == x2:
        for _ in range(min(y1, y2), max(y1, y2) + 1):
            # print(x1, _)
            # print(grid[x1][_])
            grid[x1][_] += 1
    elif y1 == y2:
        # print(coordinates)
        for _ in range(min(x1, x2), max(x1, x2) + 1):
            # print(_, y1)
            # print(grid[_][y1])
            grid[_][y1] += 1
    else:
        # find out if slope 45 degrees, then process
        if abs(y2 - y1) == abs(x2 - x1):
            for x_ in range(min(x1, x2), max(x1, x2) + 1):
                for y_ in range(min(y1, y2), max(y1, y2) + 1):
                    # This loop spits out all numbers in the range
                    # But we need only the numbers lying on the straight line
                    # So we check if it lies on the equation on this line
                    eq = check_equation(x1, y1, x2, y2, x_, y_)
                    if eq:
                        # print(x_, y_)
                        grid[x_][y_] += 1
            pass
        else:
            continue

intersections = 0
for row in grid:
    for cell in row:
        if cell > 1:
            intersections += 1

print(intersections)
