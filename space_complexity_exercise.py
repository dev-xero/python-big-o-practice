# Time Complexity: O(n)
# Space Complexity: O(1)
def boo(n: list[int]):
    i = 0
    while i < len(n):
        print('boo!')
        i += 1


# Time Complexity: O(n)
# Space Complexity: O(n)
def dumb_func(n: int) -> list:
    hi_arr: list[str] = []  # new dynamic array
    i = 0
    while i < n:
        hi_arr.append('hi')  # happens n times
        i += 1

    return hi_arr


n_list: list[int] = [1, 2, 3, 4, 5]
boo(n_list)
print(dumb_func(6))
