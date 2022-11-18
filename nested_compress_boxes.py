# The outer loop runs the inner loop a times while in turn running b times
# These are different inputs too
# Big O: O(ab)
def compress_boxes_twice(boxes: list, boxes2: list):
    # This is a nested loop
    for item in boxes:
        for item2 in boxes2:
            print(item, item2)


a = list(range(6))
b = list(range(13))
compress_boxes_twice(a, b)
