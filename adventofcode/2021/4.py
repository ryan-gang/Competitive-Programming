from utils import format_solution, puzzle_input

arepl_filter = ["A", "bingo_tables", "instructions", "random_draw", "d"]


def get_data(instructions):
    numbers_drawn = instructions[0]
    bingo_tables = []
    count = 0
    inner = []
    for row in instructions[1:]:
        if row == "":
            continue
        else:
            inner.append(row)
            count += 1

        if count % 5 == 0:
            bingo_tables.append(inner)
            inner = []
    return bingo_tables, numbers_drawn


def get_bingo_points(tables, draw, index_of_answer):
    # tables, draw = bingo_tables, random_draw

    out = {}
    # out_count = float("Inf")
    # out_val = 0
    for table in tables:
        d = {}
        rows, cols = [0] * 5, [0] * 5
        count = 0
        all_val_sum = 0
        for row_index, row in enumerate(table):
            for col_index, col in enumerate(row.strip().split()):
                if col.strip() == "":
                    continue
                else:
                    d[col] = (row_index, col_index % 5)
        for _ in draw.split(","):
            count += 1
            try:
                r, c = d[_]
                d.pop(_)
            except KeyError:
                continue
            rows[r] += 1
            cols[c] += 1
            if max(rows) == 5 or max(cols) == 5:
                break

        for key in d:
            all_val_sum += int(key)

        out[count] = all_val_sum * int(_)
        # if count < out_count:
        #     out_val = all_val_sum * int(_)

    # 1st part : print(sorted(out.items())[0][1])
    # 2nd part : print(sorted(out.items())[-1][1])
    return sorted(out.items())[index_of_answer][1]


if __name__ == "__main__":
    instructions = puzzle_input(2021, 4)
    bingo_tables, random_draw = get_data(instructions)

    solutions = format_solution(
        solver_p1=lambda: get_bingo_points(
            bingo_tables, random_draw, index_of_answer=0
        ),
        solver_p2=lambda: get_bingo_points(
            bingo_tables, random_draw, index_of_answer=-1
        ),
    )
    print(solutions)
