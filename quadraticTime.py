# Quadratic Time - O(n^2): Common in algorithms with nested iterations over the data.

def quadraticTime(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and data[i] == data[j]:
                return True
            
    return False

