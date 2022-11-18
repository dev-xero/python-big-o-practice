# Log all pairs of the array
# The function runs in quadratic time, i.e. O(n²)
def log_pairs(arr: list):
    i = 0
    while i < len(arr):
        # reset j to 0 when it's done with we finish the loop before starting again
        j = 0
        while j < len(arr):
            print(f'({arr[i]}, {arr[j]})')
            j += 1

        print('\n')
        i += 1


boxes = ['a', 'b', 'c', 'd', 'e']
log_pairs(boxes)
