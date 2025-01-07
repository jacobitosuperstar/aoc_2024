from typing import Generator


def read_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line: str = line.strip()
            yield line


def main(file_path):
    # this is where the guard is standing
    grid = []
    cx, cy = -1, -1
    for i, line in enumerate(read_file(file_path)):
        row = list(line)
        grid.append(row)
        for j, element in enumerate(row):
            if element == "^":
                cx, cy = i, j

    init_cx, init_cy = cx, cy
    rows = len(grid)
    cols = len(grid[0])

    """For the first part what we do is we do a while loop that only breaks
    when we step away from the grid area, and we move through the directions
    vector when we encounter an obstacle in our next step in that direction.

    Because for the first part we know that we won't be stuck in an infinite
    loop, is ok for us not check if we already took those steps to break the
    while loop. We just continue until we leave the grid area.
    """
    seen = set()
    directions = [(-1, 0),(0,1),(1,0),(0,-1)]
    i = 0
    seen.add((cx, cy))
    while cx >= 0 or cx < rows or cy >= 0 or cy < cols:
        nx, ny = cx + directions[i][0], cy + directions[i][1]
        if nx < 0 or nx > rows-1 or ny < 0 or ny > cols-1:
            break
        if grid[nx][ny] == "#" :
            i += 1
            if i == 4:
                i = 0
            continue
        cx, cy = nx, ny
        seen.add((cx, cy))

    """For the second part we need to be able to add an obstacle to our path
    current path, in a way that we get stuck in an infinite loop. For this
    while loop we will add an obstacle to each position that we already walked
    on, and try to check if we get stuck in an infinite loop.

    if we are stuck in an infinite loop, we return 1, if not, we return 0.
    """
    def looper(grid, me, new_obstacle):
        """This is where I will run the paths many times and check if I am
        stuck as the loopers.
        """
        cx = me[0]
        cy = me[1]
        loop_eval = set()

        if new_obstacle == me:
            return 0

        # adding a new obstacle to our path
        grid[new_obstacle[0]][new_obstacle[1]] = "#"

        i = 0
        # we add not only that we passed there, but the direction on which
        # we passed. We can pass for a same position several times, but
        # we shouldn't do it with the same direction, unless we are in a loop.
        loop_eval.add((cx, cy, directions[i]))
        while cx >= 0 or cx < rows or cy >= 0 or cy < cols or (cx, cy):
            nx, ny = cx + directions[i][0], cy + directions[i][1]

            # if the next position is outside of the grid we should return
            if nx < 0 or nx > rows-1 or ny < 0 or ny > cols-1:
                break

            # if an obstacle is in out path we should turn clock wise and
            # continue with the new direction.
            if grid[nx][ny] == "#" :
                i += 1
                if i == 4:
                    i = 0
                continue

            # we make the next step our current position.
            cx, cy = nx, ny

            # we check that the new position is not already part of the
            # main path.
            if (cx, cy, directions[i]) in loop_eval:
                # returning the grid back to normal
                grid[new_obstacle[0]][new_obstacle[1]] = "."
                return 1
            loop_eval.add((cx, cy, directions[i]))
        # returning the grid back to normal
        grid[new_obstacle[0]][new_obstacle[1]] = "."
        return 0

    loop_counter = 0
    for ox, oy in seen:
        loop_counter += looper(grid, (init_cx,init_cy), (ox,oy))

    print("looper: ", loop_counter)
    return len(seen)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
