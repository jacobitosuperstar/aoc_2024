import re

def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        s = f.read().strip()
        return s

def nums(line) -> list[int]:
    match = re.findall(r'\d+', line)
    numbers = [int(value) for value in match]
    return numbers


def main(file_path):
    # Creating the maps of the antenas
    s = read_file(file_path)
    counter = 0
    # dimentions of the map
    t_x = 11
    t_y = 7
    time = 100 # 100 seconds is what we need to simulate
    positions = {}
    for l in s.split("\n"):
        # print(l)
        p, v = l.split(" ")
        p = nums(p)
        v = nums(v)
        # p = [2,4]
        # v = [2,-3]
        print(p, v)

        p[0] = (v[0]*time + p[0]) % t_x
        p[1] = (v[1]*time + p[1]) % t_y

        if tuple(p) in positions:
            positions[tuple(p)] += 1
        else:
            positions[tuple(p)] = 1
        break
    print(positions)
    return counter


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
