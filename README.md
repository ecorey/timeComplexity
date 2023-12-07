# Constant Time - O(1):

- Description: The execution time remains constant regardless of the size of the input data. This complexity indicates that the algorithm takes a fixed amount of time to run, irrespective of the input size. It's the ideal time complexity for any algorithm.

- Example: Accessing a specific element in an array.

# Logarithmic Time - O(log n):

- Description: The execution time increases logarithmically with the input size. Algorithms with this complexity are very efficient, especially for large datasets, as they typically involve dividing the problem in half at each step.

- Example: Binary search in a sorted array.

# Linear Time - O(n):

- Description: The execution time increases linearly with the size of the input. This means the time taken is directly proportional to the number of elements in the input.

- Example: Finding an item in an unsorted list.

# Linearithmic Time - O(n log n):

- Description: Combines linear and logarithmic complexities. Algorithms with this complexity are generally quite efficient for practical purposes. It is commonly seen in advanced sorting algorithms.

- Example: Merge sort or quicksort algorithms.

# Quadratic Time - O(n^2):

- Description: The execution time increases quadratically with the input size. These algorithms are less efficient, especially as the data size grows, since the time taken is proportional to the square of the number of elements.

- Example: Bubble sort or insertion sort.

# Exponential Time - O(2^n):

- Description: The execution time doubles with every addition to the input data set. These algorithms become impractical with a growing number of elements due to their very high rate of growth.

- Example: Certain recursive algorithms like the naive solution for the Fibonacci sequence.

# Factorial Time - O(n!):

- Description: The execution time grows factorially with the input size. This is the least efficient time complexity, becoming impractical even for relatively small input sizes.

- Example: Calculating all possible permutations of a given set.
