import time

st = time.time()


# Log the first item in a list
def compress_first_box(arr: list[int]):
    if len(arr) == 0:
        print('that is an empty box')
    else:
        print(arr[0])


# Log the first two boxes
def log_first_two_boxed(arr: list[int]):
    # This is a constant time algorithm, O(1)
    i = 0
    j = i + 1
    if len(arr) == 0:
        print('That box is empty')
    elif len(arr) >= 2:
        print(arr[i], arr[j])
    else:
        print(arr[i])


sp = time.time()
box_list = list(range(1, 11000000))  # This is however a linear time operation, O(N)
esp = time.time()
print(f'\nSpecial time: {round((esp - sp) * 1000, 2)}ms')
compress_first_box(box_list)
log_first_two_boxed(box_list)

et = time.time()
print(f'\nElapsed time: {round((et - st) * 1000, 2)}ms')
print('Subtracting special time from the elapsed time, '
      'we can see that the OP time takes roughly 0ms\nthat is in constant time, O(1)')
