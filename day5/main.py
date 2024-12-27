from typing import List, Generator, Dict, Tuple
import re

def read_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line: str = line.strip()
            yield line

def main(file_path: str) -> Tuple[int, int]:
    sumpt1: int = 0
    sumpt2: int = 0
    ordering_rules: List[List[int]] = []
    update_list: List[Dict[int, int]] = []
    for line in read_file(file_path):
        if line == "":
            continue
        if "|" in line:
            line_list = line.split("|")
            line_list = [int(num) for num in line_list]
            ordering_rules.append(line_list)
        else:
            line_list = line.split(",")
            line_list = [int(num) for num in line_list]
            data_dict: Dict[int, int] = {}
            # create a dictionary that will encapsulate the value and the index
            # that we need to save.
            for i, number in enumerate(line_list):
                data_dict[number] = i
            update_list.append(data_dict)

    correct_pages: List[Dict[int, int]] = []
    incorrect_pages: List[Dict[int, int]] = []
    for pages in update_list:
        # filter the rules that apply to our current page
        filtered_rules: List[List[int]] = []
        for rule in ordering_rules:
            if rule[0] in pages and rule[1] in pages:
                filtered_rules.append(rule)

        rule_check = 0
        for rule in filtered_rules:
            if pages[rule[0]] < pages[rule[1]]:
                rule_check += 1
            else:
                a: int = pages[rule[0]]
                b: int = pages[rule[1]]
                pages[rule[0]] = b
                pages[rule[1]] = a

        for rule in filtered_rules:
            if pages[rule[0]] < pages[rule[1]]:
                pass
            else:
                a: int = pages[rule[0]]
                b: int = pages[rule[1]]
                pages[rule[0]] = b
                pages[rule[1]] = a

        for rule in filtered_rules:
            if pages[rule[0]] < pages[rule[1]]:
                pass
            else:
                a: int = pages[rule[0]]
                b: int = pages[rule[1]]
                pages[rule[0]] = b
                pages[rule[1]] = a

        for rule in filtered_rules:
            if pages[rule[0]] < pages[rule[1]]:
                pass
            else:
                a: int = pages[rule[0]]
                b: int = pages[rule[1]]
                pages[rule[0]] = b
                pages[rule[1]] = a

        if len(filtered_rules) == rule_check:
            correct_pages.append(pages)
        else:
            incorrect_pages.append(pages)

    for page in correct_pages:
        half_positon: int = int((len(page)-1) / 2)
        for key, value in page.items():
            if value == half_positon:
                sumpt1 += key

    for page in incorrect_pages:
        half_positon: int = int((len(page)-1) / 2)
        for key, value in page.items():
            if value == half_positon:
                sumpt2 += key

    return sumpt1, sumpt2

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
