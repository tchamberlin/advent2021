from pathlib import Path

import bottleneck as bn
import numpy as np


def get_input(path):
    with open(path, encoding="UTF-8") as file:
        return file.read().splitlines()


def part1(numbers):
    return np.count_nonzero(np.diff(numbers) > 0)


def part2(numbers, window_size=3):
    return np.count_nonzero(
        np.diff(bn.move_sum(numbers, window_size)[window_size - 1 :]) > 0
    )


numbers = np.array(get_input(Path(__file__).resolve().parent / "input.txt")).astype(
    "int"
)
part_1_result = part1(numbers)
part_2_result = part2(numbers)

print(f"{part_1_result=}")
print(f"{part_2_result=}")
