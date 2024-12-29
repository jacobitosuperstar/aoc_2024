from typing import Generator


def base_number(number, base) -> str:
    """This is how to code to binary, trinary or any base of number that
    we desire.
    """
    coded_value = ""
    while number > 0:
        residue = number % base
        coded_value = str(residue) + coded_value
        number = number // base
    return coded_value


def read_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as f:
        f.seek(0)
        for line in f.readlines():
            line: str = line.strip()
            yield line


def main(file_path: str) -> int:
    total_sum = 0
    for line in read_file(file_path):
        init_split = line.split(": ")
        exp_result: int = int(init_split[0])
        test_values: list[int] = [int(value.strip()) for value in init_split[1].split(" ")]
        num_operations: int = len(test_values) - 1

        # Here we take all the possibilities (3, that are the +, *, |) and do
        # the permutations of them, which are 3 to the number of operations
        # that we can fit between the numbers.

        # after that, we encode each permutation to their trinary encoding, and
        # we start evaluating each one of the permutations until we reach the
        # one that we need (where the expected result is equal to the actual
        # result).

        # If we find the value, we break the loop, and continue with the next
        # list of values.

        for permutation in range(3**num_operations):
            result = test_values[0]
            trinary = base_number(permutation, 3).zfill(num_operations)
            for i in range(num_operations):
                if trinary[i] == "0":
                    result += test_values[i+1]
                if trinary[i] == "1":
                    result *= test_values[i+1]
                if trinary[i] == "2":
                    result = int(str(result) + str(test_values[i+1]))
            if result == exp_result:
                total_sum += exp_result
                break
    return total_sum


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AOC txt file.")
    parser.add_argument("path", type=str, help="path of the file.")
    args = parser.parse_args()
    print(main(args.path))
