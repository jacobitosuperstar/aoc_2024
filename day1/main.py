from typing import List, Tuple

def read_file(file_path: str) -> Tuple[List[int], List[int]]:
    a: List[int] = []
    b: List[int] = []
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line_list: List[str] = line.split()
            a.append(int(line_list[0]))
            b.append(int(line_list[1]))
    return a, b

def main_pt1(file_path: str) -> int:
    left, rigth = read_file(file_path)
    left.sort(); rigth.sort();
    difference = 0
    for i in range(0, len(left)):
        difference += abs(left[i] - rigth[i])
    return difference

def main_pt2(file_path:str) -> int:
    left, rigth = read_file(file_path)
    similarity_dict = {}
    for i in left:
        if i not in similarity_dict:
            counter: int = 0
            for j in rigth:
                if i == j:
                    counter += 1
            similarity_dict[i] = counter
    similarity_score: int = 0
    for i in left:
        similarity_score += i * similarity_dict[i]
    return similarity_score


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main_pt1(args.path))
    print(main_pt2(args.path))
