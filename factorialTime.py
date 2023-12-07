# Factorial Time - O(n!): Execution time grows factorially with the input size, often seen in problems involving permutations.

def factorialTime(n):
    if n == 0:
        return[[]]
    result = []
    for i in range(n):
        rest = factorialTime( n - 1 )
        for r in rest:
            result.append([i] + r)
    return result