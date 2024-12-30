from typing import Generator


def read_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line: str = line.strip()
            yield line


def main(file_path: str) -> int:
    # Creating the maps of the antenas
    pathways = 0
    map = {}
    # DIRECTIONS = 0: up, 1: down, 2: left, 3: right
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i, line in enumerate(read_file(file_path)):
        for j, element in enumerate(line):
            if element in map:
                positions = map[element]
                positions.append((i,j))
                map[element] = positions
            else:
                map[int(element)] = [(i,j)]
    rows = i
    cols = j
    # sorting the map so we always start by 0
    map = dict(sorted(map.items()))
    print(map)
    return pathways


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
