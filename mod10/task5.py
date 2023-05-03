def find_insert_position(arr, x):
    l = 0
    r = len(arr)

    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

array = [1, 2, 3, 3, 3, 5]
x = 4
assert find_insert_position(array, x) == 5
