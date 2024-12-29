from typing import Generator, List, Tuple
# import re
from itertools import product

"""
jacobo
012345
"""

def generate_permutations(string, replacements=("+", "*", "||")):
    indexes = [i for i, value in enumerate(string) if value == "!"]
    all_combinations = product(replacements, repeat=len(indexes))
    results = []
    for combination in all_combinations:
        list_str = list(string)
        for i, replacement in zip(indexes, combination):
            # print("i: ", i)
            # print("replacement: ", replacement)
            list_str[i] = replacement
        results.append("".join(list_str))
    return results


def read_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line: str = line.strip()
            yield line

def main(file_path: str) -> int:
    full_values: List[Tuple[int, List[str]]] = []
    for line in read_file(file_path):
        init_split = line.split(": ")
        result: int = int(init_split[0])
        test_values: List[str] = [value.strip() for value in init_split[1].split(" ")]
        full_values.append((result, test_values))
    print("FULL VALUES")
    print(len(full_values))
    print("\n")

    total_sum = 0

    for key, value in full_values:
        eval_string = "!".join(value)
        for eval_xpre in generate_permutations(eval_string):
            a = 0
            b = ""
            operator = "+"
            list_eval_xpre = list(eval_xpre)
            for i, v in enumerate(list_eval_xpre):
                if v.isdigit():
                    b += v
                else:
                    if operator == "+" or operator == "*":
                        a = eval(f"{a}{operator}{b}")
                    if operator == "|" and b == "":
                        continue
                    if operator == "|" and b != "":
                        a = int(f"{a}{b}")
                    b = ""
                    operator = v
            if operator == "+" or operator == "*":
                a = eval(f"{a}{operator}{b}")
            if operator == "|" and b != "":
                a = int(f"{a}{b}")
            if a == key:
                print("matching_exp", eval_xpre)
                print("matching result: ", key)
                total_sum += key
                break
    return total_sum


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
