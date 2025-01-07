from typing import Generator


def read_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line: str = line.strip()
            yield line

def dfs1(seen, seen_en, grid, cx, cy):
    """Depth first searh.

    Have to sets, one for all the visited points in general, the other, for all
    the nodes that I am visiting in this current iteration from the grid loop.

    move around the grid searching for all the nodes that have equal value to
    the one I am currently in. If there is another, we should do a recursive
    call, if not, we just one unit of value to the perimeter for each direction
    that we check and it qualifies.

    Finally, we return the len of the perimeter.
    """
    # checking if the element has already been visited.
    if (cx, cy) in seen:
        return 0
    # Adding the position to the seen set
    seen.add((cx, cy))
    seen_en.add((cx, cy))
    # DIRECTIONS = 0: up, 1: down, 2: left, 3: right
    # Never forget that the directions should be clock or counter clock wise
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    perimeter = 0
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if nx > len(grid)-1 or nx < 0 or ny > len(grid[0])-1 or ny < 0:
            perimeter += 1
            continue
        if grid[cx][cy] != grid[nx][ny]:
            perimeter += 1
            continue
        if grid[cx][cy] == grid[nx][ny]:
            perimeter += dfs1(seen, seen_en, grid, nx, ny)
    return perimeter

def valid(grid, coordinatesA, coordinatesB):
    """Checks if the given coordinates are inside the grid and if the values
    of the two coordinates pairs are the same. Else false.
    """
    if coordinatesB[0] > len(grid)-1 or coordinatesB[0] < 0 or coordinatesB[1] > len(grid[0])-1 or coordinatesB[1] < 0:
        return False
    if grid[coordinatesA[0]][coordinatesA[1]] == grid[coordinatesB[0]][coordinatesB[1]]:
        return True
    return False

def dfs2(seen, seen_en, grid, cx, cy):
    """Depth first searh.

    For this we will use a theorem that says that a polygon has the same number
    of sides as of corners. Therefore we should only be counting the corners
    within the different areas.

    Just check if there are concave or convex corners.
    -------------------------
    | * A | A * | A A | A A |
    | A A | A A | A * | * A | => Concave corners
    -------------------------
    | * * | A * | * A | * * |
    | * A | * * | * * | A * | => Convex corners
    -------------------------

    for the convex corners remember that

    -------------
    | A * | * A |
    | * A | A * | => each A is a corner
    -------------

    becuse of that, I don't have to check the diagonal to see if I am a corner
    or not, the two wrong values at the sides are enough.

    In all polygons, the number of corners is the number of sides.
    """
    # checking if the element has already been visited.
    if (cx, cy) in seen:
        return 0
    # Adding the position to the seen set
    seen.add((cx, cy))
    seen_en.add((cx, cy))
    # DIRECTIONS = 0: up, 1: down, 2: left, 3: right
    # Never forget that the directions should be clock or counter clock wise
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    corners = 0
    for i in range(len(directions)):
        nx, ny = cx + directions[i][0], cy + directions[i][1] # UP/DOWN
        mx, my = cx + directions[i-1][0], cy + directions[i-1][1] # LEFT/RIGHT

        # DIAGONALS
        zx = cx + directions[i][0] + directions[i-1][0]
        zy = cy + directions[i][1] + directions[i-1][1]

        if not valid(grid,(cx,cy),(nx,ny)) and not valid(grid,(cx,cy),(mx,my)):
            corners += 1
        # here i have to check the diagonal to see that I am not inside the
        # fenced area when the up/down and left/right values are valid.
        if valid(grid,(cx,cy),(nx,ny)) and valid(grid,(cx,cy),(mx,my)) and not valid(grid,(cx,cy),(zx,zy)):
            corners += 1
        if valid(grid,(cx,cy),(nx,ny)):
            corners += dfs2(seen, seen_en, grid, nx, ny)
    return corners

def main(file_path):
    # Creating the maps of the antenas
    grid = []
    for line in read_file(file_path):
        grid.append(list(line))

    rows = len(grid)
    cols = len(grid[0])

    seen = set()
    cost = 0
    for i in range(rows):
        for j in range(cols):
            seen_en = set()
            perimeter = dfs1(seen, seen_en, grid, i, j)
            if perimeter > 0:
                cost += len(seen_en) * perimeter
                # print(grid[i][j])
                # print("perimeter: ", perimeter)
                # print("area: ", len(seen_en))
    if not len(seen) == rows * cols:
        raise ValueError("Check me")

    seen = set()
    discounted_cost = 0
    for i in range(rows):
        for j in range(cols):
            seen_en = set()
            corners = dfs2(seen, seen_en, grid, i, j)
            if corners > 0:
                discounted_cost += len(seen_en) * corners
                # print(grid[i][j])
                # print("corners: ", corners)
                # print("area: ", len(seen_en))
    if not len(seen) == rows * cols:
        raise ValueError("Check me")
    return cost, discounted_cost


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
