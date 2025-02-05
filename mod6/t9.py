from typing import List
import os
import re


letters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}
with open(os.path.join(os.sep, *'usr share dict words'.split())) as data:
    words: str = data.read()


def my_t9(line: str) -> List[str]:
    return re.findall(f'\\b{"".join(["[" + "".join(letters[char]) + "]" for char in line])}\\b', words)

if __name__ == '__main__':
    print(my_t9(input()))
