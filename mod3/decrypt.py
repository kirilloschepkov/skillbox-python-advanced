import sys


def decrypt(data: str) -> str:
    st = list()
    ls = list(data.replace("’", '').replace("‘", '').replace('\n', ''))
    last_char_is_dot = False
    for char in ls:
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
    print(decrypt(sys.stdin.read()))
