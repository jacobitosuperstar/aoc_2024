import re

def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        s = f.read().strip()
        return s

def nums(line) -> list[int]:
    match = re.findall(r'\-\d+|\d+', line)
    numbers = [int(value) for value in match]
    return numbers

def mainpt1(file_path):
    """We take each element of the file and parse it. Then we multiply the
    time for the velocity and add it to the initial position just to divide by
    the module. That residual value is the final position of the robot at the
    tiles knowing that they can wrap around the map.

    Because they tell us about the cuadrants, on which we delete the middle
    line of the grid, we do the (tx-1)//2 to know row before the middle, and
    then we clasify the robots within the cuadrants
    """
    # Creating the maps of the antenas
    s: str = read_file(file_path)
    counter: int = 1
    # dimentions of the map
    tx: int = 101 # 11 # 101
    ty: int = 103 # 7 # 103
    time: int = 100 # 100 seconds is what we need to simulate
    ans: list[int]= [0, 0 , 0, 0]
    for l in s.split("\n"):
        px, py, vx, vy = nums(l)

        px = (px + vx*time) % tx
        py = (py + vy*time) % ty

        if px < (tx-1)//2 and py < (ty-1)//2:
            ans[0] += 1
        elif px > (tx-1)//2 and py < (ty-1)//2:
            ans[1] += 1
        elif px < (tx-1)//2 and py > (ty-1)//2:
            ans[2] += 1
        elif px > (tx-1)//2 and py > (ty-1)//2:
            ans[3] += 1

    for element in ans:
        counter *= element
    return counter


def main(file_path):
    """For the part two, we need to find the point on which the robots create
    a christmas tree. Because we don't know the shape we just eye bolled that
    all the positions of the robots must be different.

    To do this, we create a set of seen positions and compare it to the length
    of the positions of the robots, and we simulate the time passing by. If
    they are the same, we break the loop and return the amount of time passed.
    """
    # Creating the maps of the antenas
    s: str = read_file(file_path)
    # dimentions of the map
    tx: int = 101 # 11 # 101
    ty: int = 103 # 7 # 103
    for time in range(1000000):
        robots = 0
        seen = set()
        for l in s.split("\n"):
            px, py, vx, vy = nums(l)

            px = (px + vx*time) % tx
            py = (py + vy*time) % ty
            seen.add((px, py))
            robots += 1
        if len(seen) == robots:
            break
    return time


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
