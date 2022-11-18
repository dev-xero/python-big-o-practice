# This function runs in linear time, O(n)
def dumb_func(items: list[int]):
    mid = (len(items) // 2) - 1
    i = 0
    j = 1

    print(items[0])

    print('\n')

    # Runs n/2 times, but still linearly each time i.e. O(n)
    while i <= mid:
        print(items[i])
        i += 1

    print('\n')

    # Runs 100 times, not related to the input in any way
    # Regardless of the input size, this still runs 100 times i.e O(1) * 100
    while j <= 100:
        print('hi', j)
        j += 1


# Big O computation: O(1 + n/2 + 100)
# Standard Format: O(n)
arr = list(range(1, 101))
dumb_func(arr)
