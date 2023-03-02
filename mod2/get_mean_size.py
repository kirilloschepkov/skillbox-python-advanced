import sys
from typing import TextIO


def get_mean_size(data: TextIO) -> int:
    size = [int(line.split()[4]) for line in data.readlines()[1:]]
    return sum(size) / len(size)


if __name__ == '__main__':
    print(get_mean_size(sys.stdin))