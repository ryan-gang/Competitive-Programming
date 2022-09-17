from collections import Counter, defaultdict
from utils import format_solution, puzzle_input
import time


def LanternfishGrowthGrouped(fishes, days):
    d = Counter(fishes)
    count = days

    a = time.time()
    count_of_fishes = len(fishes)

    while count > 0:
        fish_dict = defaultdict(int)
        for key in d:
            if key == 0:
                fish_dict[8] += d[0]
                fish_dict[6] += d[0]
                count_of_fishes += d[0]
            else:
                fish_dict[key - 1] += d[key]

        d = fish_dict

        count -= 1
        b = time.time()
        # print(
        #     f"After {days - count} Days: {count_of_fishes}, Elapsed:"
        #     f" {round((b - a), 4)}s"
        # )

    return count_of_fishes


def lanternfish_growth(fishes, days):
    NEW_FISH = 8
    count = days

    while count > 0:
        a = time.time()
        count_of_new_fish = 0
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] += 6
                count_of_new_fish += 1
            else:
                fishes[i] -= 1

        fishes.extend([NEW_FISH] * count_of_new_fish)
        # print(fishes)
        b = time.time()
        # print(
        #     f"After {days - count + 1} Days: {len(fishes)}, Elapsed:"
        #     f" {round((b - a), 4)}s"
        # )
        count -= 1

    return len(fishes)


if __name__ == "__main__":
    instructions = [int(line) for line in puzzle_input(2021, 6)[0].split(",")]
    # X = [3,4,3,1,2]
    # solutions = format_solution(
    #     solver_p1=lambda: LanternfishGrowthGrouped(X, days=80),
    #     solver_p2=lambda: LanternfishGrowthGrouped(X, days=256),
    # )
    # print(solutions)
    solutions = format_solution(
        solver_p1=lambda: LanternfishGrowthGrouped(instructions, days=80),
        solver_p2=lambda: LanternfishGrowthGrouped(instructions, days=256),
    )
    print(solutions)
