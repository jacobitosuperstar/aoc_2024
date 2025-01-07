from typing import Generator


def read_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line: str = line.strip()
            yield line

def transformator(input_list):
    modified_list = []
    for i, element in enumerate(input_list):
        if element == 0:
            modified_list.append(1)
        elif len(str(element)) % 2 == 0:
            value = str(element)
            half_len = int(len(value)/2)
            modified_list.append(int(value[:half_len]))
            modified_list.append(int(value[half_len:]))
        else:
            modified_list.append(element*2024)
    return modified_list


cache = {}
def multiplier(number, steps):
    if (number, steps) in cache:
        return cache[(number, steps)]
    value = 0
    if steps == 0:
        return 1
    if number == 0:
        value += multiplier(1, steps-1)
    elif len(str(number)) % 2 == 0:
        half_len = int(len(str(number))/2)
        value += multiplier(int(str(number)[:half_len]), steps-1)
        value += multiplier(int(str(number)[half_len:]), steps-1)
    else:
        value += multiplier(number * 2024, steps-1)
    cache[(number, steps)] = value
    return value  

def power_of_two(input_list):
    return 0


def main(file_path: str) -> int:
    # Creating the maps of the antenas
    blinks = 75
    input = []
    for i, line in enumerate(read_file(file_path)):
        row = []
        for j, element in enumerate(line.split(" ")):
            row.append(int(element))

        for element in row:
            input.append(element)

    # new_list = input
    # for i in range(1, blinks+1):
    #     new_list = transformator(new_list)
    #     print(new_list)
    # return len(new_list)

    total_values = 0
    for element in input:
        total_values += multiplier(element, blinks)
    return total_values


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
