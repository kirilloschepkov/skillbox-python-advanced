import sys
from typing import TextIO


def decrypt(data: TextIO) -> str:
    st = list()
    ls = list(data.read())
    if ls[-1] == '\n':
        ls = ls[:-1]
    last_char_is_dot = False
    for char in ls[1:-1]:
        if last_char_is_dot and char == '.':
            if len(st) > 0:
                st.pop()
            last_char_is_dot = False
        elif char == '.':
            last_char_is_dot = True
        else:
            st.append(char)
            last_char_is_dot = False
    return ''.join(st)


if __name__ == '__main__':
    print(decrypt(sys.stdin))
