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
    for l in s.split("\n\n"):
        a, b, p = l.split("\n")
        a = nums(a)
        b = nums(b)
        p = nums(p)

        # this is for part 2
        p = [10000000000000+value for value in p]


        """The problem is a system of linear equations. Eventhough the first
        part can be brute force, we will solve the system entirelly as it
        should be solved.

        BUTTOM A == i
        BUTTOM B == j

        i*ax+j*bx=px
        i*ay+j*by=py

        i+j*(bx/ax)=(px/ax)
        i+j*(by/ay)=(py/ay)

        solving for j

        i+j*(bx/ax)-i-j*(by/ay)=(px/ax)-(py/ay)
        j*(bx/ax)-j(by/ay)=(ay*px-ax*py)/(ax*ay)
        j(bx/ax - by/ay)=(ay*px-ax*py)/(ax*ay)
        j((bx*ay-by*ax)/(ax*ay))=(ay*px-ax*py)/(ax*ay)

        -------------------------------------
        | j = ((ay*px-ax*py)/(bx*ay-by*ax)) |
        -------------------------------------

        solving for i

        i*ax+((ay*px-ax*py)/(bx*ay-by*ax))*bx = px
        i*ax = px - ((ay*px-ax*py)/(bx*ay-by*ax))*bx
        i*ax = px - ((bx*ay*px-bx*ax*py)/(bx*ay-by*ax))
        i*ax = (px*bx*ay-px*by*ax-bx*ay*px+bx*ax*py)/(bx*ay-by*ax)
        i*ax = (-px*by*ax+bx*ax*py)/(bx*ay-by*ax)

        -------------------------------------
        | i = ((bx*py-by*px)/(bx*ay-by*ax)) |
        -------------------------------------
        """
        A = int(((b[0]*p[1]-b[1]*p[0])/(b[0]*a[1]-b[1]*a[0])))
        B = int(((a[1]*p[0]-a[0]*p[1])/(b[0]*a[1]-b[1]*a[0])))

        if A*a[0] + B*b[0] == p[0] and A*a[1] + B*b[1] == p[1]:
            counter += (A*3 + B*1)

    return counter


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
