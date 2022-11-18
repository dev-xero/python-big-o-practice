import time
st = time.time()


def find_nemo(arr: list[str]) -> None:
    # Find the nemo string in a list
    # Runs in linear time, O(N)
    # Break when we find the first instance
    for char in arr:
        if char == 'nemo':
            print('Found Nemo!')
            break

    # Constant time operation
    if 'nemo' not in arr:
        print("Couldn't Find Nemo")


# Large list
l_list: list[str] = ['hi'] * 100
# Create a nemo list
nemo: list[str] = ['nemo']
find_nemo(nemo)

et = time.time()
print(f'\nElapsed time: {round((et - st) * 1000, 2)}ms')
