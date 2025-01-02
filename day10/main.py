from typing import Generator


def read_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line: str = line.strip()
            yield line

def dfs1(seen, grid, cx, cy):
    """
    Depth first searh.

    the main idead of the algorithm is that when we are in a grid
    we can move in four directions (Up, Down, Left, Right). And 
    if the counter increases by one within the grid, we can move
    into the next position until we find a 9.

    In the part 1 of the excersive, we can only reach a 9 in a 
    singular way, thus, we should add that position in a set and
    check, if several paths are leading into the same 9, they should
    be avoided, as in the excersice all the paths to count should each
    of the lead to a different 9.

    first of all, we need the grid, to know the values of the value in
    the current position, and the current position. For this excersice
    we created a list with all the starts of the trail heads (where
    cx, cy are equals to 0 within the grid). And to each of those
    positions we apply the DFS algorithm.

    for the DFS algorith we have the directions of movement, in this case,
    there are 4 (Up, Down, Left, Right). Then we take the initial 
    cx, cy positons and evaluate if those positions are equals to a 9. If
    they are return 0, and there are no points to add, if not, we should 
    move to a different position where we add one of the directions.

    If the new position is still within the range of the grid, we check
    that if the value is equals to the current value of the element in the 
    grid plus the increment, in this case would be 1.

    If that is the case, we should call again the DFS algorithm until we 
    close the iterative calls, being that we get to the goal value of 1 or
    if the value is already in the set of seen 9 positions.
    """
    # DIRECTIONS = 0: up, 1: down, 2: left, 3: right
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # seen = set()
    if (cx, cy) in seen:
        return 0
    if grid[cx][cy] == 9:
        seen.add((cx, cy))
        return 1
    result = 0
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if nx in range(len(grid)) and ny in range(len(grid[0])):
            if grid[nx][ny] == 1 + grid[cx][cy]:
                result += dfs1(seen, grid, nx, ny)
    return result

def dfs2(grid, cx, cy):
    """
    Depth first searh.

    For the second part, the score changes in a way where all
    the to reach a 9 count. So we don't need a set to trach the 9s
    that we already visited.
    """
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    if grid[cx][cy] == 9:
        return 1
    result = 0
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if nx in range(len(grid)) and ny in range(len(grid[0])):
            if grid[nx][ny] == 1 + grid[cx][cy]:
                result += dfs2(grid, nx, ny)
    return result


def main(file_path: str) -> int:
    # Creating the maps of the antenas
    pathways_pt1 = 0
    pathways_pt2 = 0
    trailheads = []
    grid = []
    for i, line in enumerate(read_file(file_path)):
        row = []
        for j, element in enumerate(line):
            row.append(int(element))
            if int(element) == 0: 
                trailheads.append((i,j))
        grid.append(row)

    rows = i
    cols = j
    # sorting the map so we always start by 0

    for head in trailheads:
        # Different trailheads can reach the same 9, but the same trail
        # head cannot reach the same 9.
        seen = set()
        pathways_pt1 += dfs1(seen, grid, head[0], head[1]) 
        pathways_pt2 += dfs2(grid, head[0], head[1]) 
    return pathways_pt1, pathways_pt2


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
