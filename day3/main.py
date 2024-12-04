from typing import List, Generator
import re

def read_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line: str = line.strip()
            yield line

def main(file_path: str) -> int:
    sum: int = 0
    enabled: bool = True
    for line in read_file(file_path):
        x: List[str] = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        for element in x:
            if element == "do()":
                enabled = True
                continue
            if element == "don't()":
                enabled = False
                continue
            if enabled:
                a, b = nums(element)
                sum += a * b
    return sum

def nums(s: str) -> List[int]:
    """from a string it gets all the numbers.
    """
    numbers: List = re.findall(r"\d+", s)
    numbers: List = [int(num) for num in numbers]
    return numbers


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
