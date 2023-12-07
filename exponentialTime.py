# Exponential Time - O(2^n): The execution time doubles with each addition to the input data set.

def fibonacci(n):
    if n <= 1:
        return n 
    else:
        return fibonacci( n - 1 ) + fibonacci( n - 2 )

    
      