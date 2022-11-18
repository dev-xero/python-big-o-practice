# Print all numbers then all pair sums
# Big-O for this function: O(n + n²) -> O(n²)
def another_dumb_func(numbers: list[int]) -> None:
    print('\nThe Numbers')
    for num in numbers:
        print(num)

    print('\nThe Sums')

    i = 0
    while i < len(numbers):
        j = 0
        while j < len(numbers):
            print(numbers[i] + numbers[j])
            j += 1
        print('')
        i += 1


n_list: list[int] = [1, 2, 3, 4, 5]
another_dumb_func(n_list)
