# Linear Time - O(n): The execution time increases linearly with the input size.

def linearTime(data, target):
    for i, value in enumerate(data):
        if value == target:
            return i
    return None