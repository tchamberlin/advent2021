from pathlib import Path


def get_input(path):
    with open(path, encoding="UTF-8") as file:
        return file.read().splitlines()


class SubmarinePart1:
    def __init__(self, lines):
        self.depth = 0
        self.hpos = 0

        for line in lines:
            self.parse_line(line)

    def parse_line(self, line):
        cmd, value = line.split(" ")
        value = int(value)
        if cmd == "forward":
            self.hpos += value
        elif cmd == "down":
            self.depth += value
        elif cmd == "up":
            self.depth -= value


class SubmarinePart2:
    def __init__(self, lines):
        self.depth = 0
        self.hpos = 0
        self.aim = 0

        for line in lines:
            self.parse_line(line)

    def parse_line(self, line):
        cmd, value = line.split(" ")
        value = int(value)
        if cmd == "forward":
            # forward X does two things:
            # It increases your horizontal position by X units.
            self.hpos += value
            # It increases your depth by your aim multiplied by X
            self.depth += self.aim * value
        elif cmd == "down":
            # down X increases your aim by X units
            self.aim += value
        elif cmd == "up":
            # up X decreases your aim by X units
            self.aim -= value


def part1(lines):
    sub = SubmarinePart1(lines)
    return sub.depth * sub.hpos


def part2(lines):
    sub = SubmarinePart2(lines)
    return sub.depth * sub.hpos


def main():
    lines = get_input(Path(__file__).resolve().parent / "input.txt")
    print(f"{part1(lines)=}")
    print(f"{part2(lines)=}")


if __name__ == "__main__":
    main()
