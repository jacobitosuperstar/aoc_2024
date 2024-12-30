from typing import Generator
from itertools import repeat


def read_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line: str = line.strip()
            yield line


def main(file_path: str) -> int:
    # Creating the maps of the antenas
    for line in read_file(file_path):
        disk: list[str] = list(line)

    disk_map = []
    id = 0
    # DISK EXPANSION
    for i, char in enumerate(disk):
        # File
        if i % 2 == 0:
            file_repr = repeat(id, int(char))
            for element in file_repr:
                disk_map.append(element)
            id += 1
        # Free scape
        else:
            empty_space_repr = repeat(".", int(char))
            for element in empty_space_repr:
                disk_map.append(element)

    # DATA MOVEMENT
    # print(disk_map)
    consecutive_values = []
    consecutive = []

    val = None
    for i in range(len(disk_map)-1, -1, -1):
        if disk_map[i] == ".":
            continue
        val = disk_map[i]
        break

    for i in range(len(disk_map)-1, -1, -1):
        # print(disk_map[i])
        # print(i)
        if disk_map[i] == ".":
            continue
        if disk_map[i] == val:
            consecutive.append((i, val))
        else:
            val = disk_map[i]
            consecutive_values.append(consecutive)
            consecutive = []
            consecutive.append((i,val))
    consecutive_values.append(consecutive)

    # print(consecutive_values)

    for consecutive in consecutive_values:
        dot_counter = 0
        idx_saver = []
        for j in range(0, len(disk_map), 1):
            if disk_map[j] != ".":
                dot_counter = 0
                idx_saver = []
                continue
            if disk_map[j] == ".":
                dot_counter += 1
                idx_saver.append(j)
            if dot_counter == len(consecutive):
                for i, idx in enumerate(idx_saver):
                    if idx > consecutive[i][0]:
                        continue
                    disk_map[idx] = consecutive[i][1]
                    disk_map[consecutive[i][0]] = "."
                break
            # print(disk_map)
    # print(disk_map)

    # CHECK SUM
    check_sum = 0
    for i, value in enumerate(disk_map):
        if value == ".":
            continue
        check_sum += i*int(value)
    return check_sum


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
