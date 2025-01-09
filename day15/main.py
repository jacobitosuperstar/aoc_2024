import re

def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        s = f.read().strip()
        return s

def nums(line) -> list[int]:
    match = re.findall(r'\-\d+|\d+', line)
    numbers = [int(value) for value in match]
    return numbers

def main_pt1(file_path):
    mx, my = -1, -1
    grid: list[list[str]] = []
    instructions: list[str] = []
    s = read_file(file_path)

    # movement directions
    dirs: dict[str, list[int]] = {
        "^": [-1, 0],
        "v": [1, 0],
        "<": [0, -1],
        ">": [0, 1]
    }
    for i, l in enumerate(s.split("\n")):
        if l.startswith("#"):
            grid.append(list(l))
            for j, element in enumerate(list(l)):
                if element == "@":
                    mx, my = i, j
                    break
        elif l == "":
            continue
        else:
            for element in list(l):
                instructions.append(element)

    # # -> wall cannot do anything
    # O -> Box or boxes that moves with me
    # @ -> me

    """The main idea here is to start moving the robot in the direction of
    the instruction, but first we will check if there is a box that we need
    to move right next to us.

    If there is a box, we will check if within the same direction, we find
    another box right next to it, and we start to add those boxes to a list
    that will contain all the boxes that we will move when the robot moves.

    then we will check if there is an obstacle or wall (#), if that is the case
    we won't do anything and none of the instructions will be acted on.

    if we find an empty space (.) we will start moving the boxes from last to
    first, where we first make the current position of a box an empty space (.)
    and the we move it to the current direction of the robot, and so on with
    the other boxes. Then we move the robot in the same manner, making the
    current position an empty space (.) and then moving the robot (@) to the
    next position in the instruction direction.

    After all of that is done, we finish with a Grid that has all the correct
    positions of the robot(@) and the boxes(O). So we loop over it, finding
    all the occurrences of the boxes(O) and adding the GPS coordinates
    accordingly.
    """
    for inst in instructions:
        dx, dy = dirs[inst]
        x, y = mx + dx, my + dy

        # boxes to move
        b2m = []

        while grid[x][y] == "O":
            b2m.append([x,y])
            x += dx
            y += dy
        if grid[x][y] == "#":
            pass
        else:
            assert grid[x][y] == ".", f"grid: {grid[x][y]}, dir: {dx, dy}, coordinate: {x,y}"
            for bx, by in b2m[::-1]:
                grid[bx][by] = "."
                grid[bx+dx][by+dy] = "O"
            grid[mx][my] = "."
            grid[mx+dx][my+dy] = "@"
            mx, my = mx+dx, my+dy

    counter= 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                counter += i*100 + j
    return counter


def main(file_path):
    mx, my = -1, -1
    grid: list[list[str]] = []
    instructions: list[str] = []
    s = read_file(file_path)

    # movement directions
    dirs: dict[str, list[int]] = {
        "^": [-1, 0],
        "v": [1, 0],
        "<": [0, -1],
        ">": [0, 1]
    }
    for i, l in enumerate(s.split("\n")):
        row = []
        if l.startswith("#"):
            for j, char in enumerate(list(l)):
                if char == "#":
                    row.append("#")
                    row.append("#")
                if char == "O":
                    row.append("[")
                    row.append("]")
                if char == ".":
                    row.append(".")
                    row.append(".")
                if char == "@":
                    row.append("@")
                    row.append(".")
            grid.append(row)
        elif l == "":
            continue
        else:
            for element in list(l):
                instructions.append(element)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                mx, my = i, j
                break

    # -> wall cannot do anything
    # [] -> Box or boxes that moves with me
    # @ -> me
    for inst in instructions:
        dx, dy = dirs[inst]

        # boxes to move

        """For this parth two is needed a Breath First Search algorithm

        we need to collect all the coordinates that we can move within the grid
        and needs to be recursive in a way, as there is the posibility of 1
        box moving 2, like this

        ############
        ## . . . . #
        ## . [ ] [ ]
        ## . . [ ] .
        ## . . . @ .

        so level by level we are constructing all the objects that we are able
        to move.

        the iteration is something like this, following the example.

        first we add ourselves. Then we check in the up direction and find a
        "]", because of that, we add the other corner "[" to our list and
        continue with the next element of our list.

        we are here "]" and then we check above and find this "[" and we add
        "]" the other corner too. then we continue with the next element of
        the list, which is the "[" that was next to our first box bracked, and
        check up from there.

        if we find only empty spaces at the end of our tree, our i catches the
        lenght of the list and we can continue with the movement of those
        coordinates, if we find in any section of the tree a "#", the movement
        becomes impossible and we need to continue to the other instruction.

        after we have the list of all the coordinates that we can move, what
        we do is to copy the original grid and then we make the original
        positions "." and then we copy the value of the coordinates into the
        shifted values of our new grid.

        we make this new grid the old grid, and we add dx and dy to our current
        position because we moved, and then we continue with the cycle.
        """
        c2m = [(mx, my)]
        i = 0
        impossible: bool = False

        while i < len(c2m):
            x, y = c2m[i]
            nx, ny = x+dx, y+dy
            if grid[nx][ny] in "[]":
                if (nx, ny) not in c2m:
                    c2m.append((nx,ny))
                if grid[nx][ny] == "[":
                    if (nx, ny+1) not in c2m:
                        c2m.append((nx, ny+1))
                if grid[nx][ny] == "]":
                    if (nx, ny-1) not in c2m:
                        c2m.append((nx, ny-1))
            elif grid[nx][ny] == "#":
                impossible = True
                break
            i += 1

        if impossible:
            continue

        new_grid = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]

        for i,j in c2m:
            new_grid[i][j] = "."

        for i,j in c2m:
            new_grid[i+dx][j+dy] = grid[i][j]

        grid = new_grid
        mx += dx
        my += dy

    counter= 0
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            if grid[i][j] == "[":
                counter += i*100 + j
    return counter


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
