from typing import Generator


def read_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line: str = line.strip()
            yield line


def main(file_path: str) -> int:
    # Creating the maps of the antenas
    antenas = {}
    for i, line in enumerate(read_file(file_path)):
        for j, char in enumerate(line):
            if char != ".":
                if char in antenas:
                    new_antena = antenas[char]
                    new_antena.append((i, j))
                    antenas[char] = new_antena
                else:
                    antenas[char] = [(i,j)]
    rows: int = i
    columns: int = j
    # processing each antena
    # antinodes positions
    antinode_pos = set()
    for _, value in antenas.items():
        if len(value) == 1:
            continue
        for i in range(0, len(value)-1):
            for j in range(i+1, len(value)):
                X = value[i][0] - value[j][0]
                Y = value[i][1] - value[j][1]
                antinode_pos.add(value[i])
                antinode_pos.add(value[j])
                antinode_0 = (value[i][0] + X, value[i][1] + Y)
                while antinode_0[0] >= 0 and antinode_0[0] <= rows and antinode_0[1] >= 0 and antinode_0[1] <= columns:
                    antinode_pos.add(antinode_0)
                    antinode_0 = (antinode_0[0]+X, antinode_0[1]+Y)

                antinode_1 = (value[j][0] - X, value[j][1] - Y)
                while antinode_1[0] >= 0 and antinode_1[0] <= rows and antinode_1[1] >= 0 and antinode_1[1] <= columns:
                    antinode_pos.add(antinode_1)
                    antinode_1 = (antinode_1[0]-X, antinode_1[1]-Y)
    return len(antinode_pos)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
