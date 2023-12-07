# Logarithmic Time - O(log n)
# Common in algorithms that halve the input data at each step (like binary search).
def logarithimicTime(data, target):
    
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else: 
            high = mid -1
    
    return None