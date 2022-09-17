import re
from typing import Dict, List, Tuple
from utils import elapsed_time, print_results

def read_instructions(filename: str) -> List[str]:
    return [line.strip() for line in open(filename)]


def get_bags_data(instructions: List[str]) -> List[Tuple[str, str]]:
    bags_data = []
    for instruction in instructions:
        data = re.findall("(.*) contain (.*).", instruction)[0]
        bags_data.append(data)

    return bags_data


def get_inner_and_outer_bags(bags_data: List[Tuple[str, str]]) -> Dict[str, List]:
    inner_and_outer_bags = {}
    for bag in bags_data:
        outer_bag_string = bag[0]
        inner_bag_string = bag[1]
        if "," in inner_bag_string:
            inner_bags_string = inner_bag_string.split(",")
        else:
            inner_bags_string = [inner_bag_string]

        pattern = re.compile("[0-9 ]*(.*) bag[s]*")

        outer_bag = re.findall(pattern, outer_bag_string)[0]

        for inner_bag_s in inner_bags_string:
            inner_bag_s = inner_bag_s.strip()
            inner_bag = re.findall(pattern, inner_bag_s)[0]
            if inner_bag == "no other":
                continue
            elif inner_bag in inner_and_outer_bags:
                outer_bag_exists = inner_and_outer_bags[inner_bag]
                outer_bag_exists.append(outer_bag)
            else:
                inner_and_outer_bags[inner_bag] = [outer_bag]

    return inner_and_outer_bags


def get_possible_outer_bags(my_bag: str, inner_and_outer_bags: Dict[str, List]) -> List[str]:
    possible_outer_bags = []
    if my_bag in inner_and_outer_bags:
        possible_outer_bags += inner_and_outer_bags[my_bag]

    for bag in possible_outer_bags:
        if bag in inner_and_outer_bags:
            possible_outer_bags += inner_and_outer_bags[bag]

    return possible_outer_bags


def get_distinct_count(possible_outer_bags: List[str]) -> int:
    return len(set(possible_outer_bags))


def part1(filename: str, my_bag: str) -> int:
    instructions = read_instructions(filename)
    bags_data = get_bags_data(instructions)
    inner_and_outer_bags = get_inner_and_outer_bags(bags_data)
    possible_outer_bags = get_possible_outer_bags(my_bag, inner_and_outer_bags)
    count = get_distinct_count(possible_outer_bags)
    return count


def part2():
    pass


if __name__ == '__main__':
    puzzle_input = '7.txt'
    my_bag = "shiny gold"
    print_results(elapsed_time(part1, puzzle_input, my_bag))  #
                  # elapsed_time(part2, puzzle_input))  #
