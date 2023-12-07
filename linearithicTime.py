# Linearithmic Time - O(n log n): Often seen in efficient sorting algorithms like mergesort and quicksort.

def linearithmicTime(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data // 2)]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return linearithmicTime(left) + middle + linearithmicTime(right)



