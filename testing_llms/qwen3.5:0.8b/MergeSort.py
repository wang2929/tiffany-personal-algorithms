def merge_sort(arr):
    """
    Iterative Merge Sort
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr

    n = len(arr)
    result = []

    # Divide: split into two halves
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    # Sort both halves
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Merge: combine sorted arrays
    result = merge(sorted_left, sorted_right)

    return result


def merge(left, right):
    """
    Merge sorted subarrays
    Time Complexity: O(n + m)
    """
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements from left or right
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

if __name__ == '__main__':
    # Large array from qwen3.5:0.8b, for array that doesn't need sorting
    arr = range(1, 200)
    sorted_array = merge_sort(arr)
    print("Sorted array (first 50 elements):", sorted_array[:50])
    
    # Example 1: Basic sorted array
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = merge_sort(numbers)
    print("Original Array:", numbers)
    print("Sorted Array:", sorted_numbers)

    # Example 2: Large array
    large_array = list(range(1, 100))
    sorted_large_array = merge_sort(large_array)
    print("Sorted array:", sorted_large_array)

    # Example 3: Already sorted array
    already_sorted = [34, 25, 12, 22, 11, 90, 64]
    sorted_2 = merge_sort(already_sorted)
    print("Sorted array:", sorted_2)

''' qwen3.5:0.8b wrote this twice for some reason
def merge_sort(arr):
    """
    Iterative Merge Sort

    Args:
        arr: Array to be sorted
    Returns:
        Sorted version of the array
    """
    if len(arr) <= 1:
        return arr

    n = len(arr)
    result = []

    # Divide array into two halves
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Merge sorted halves
    result = merge(sorted_left, sorted_right)

    return result
'''

''' qwen3.5:0.8b also wrote this twice. Time is BS, space is okay
## Performance Comparison

| Method     | Time Complexity | Space Complexity | Best Case   | Worst Case    |
|------------|------------------|------------------|-------------|---------------|
| Merge Sort | O(n log n)       | O(n)             | T(n) = 0    | T(n) = n²     |
| Bubble Sort  | T(n) = 0          | O(1)             | 0           | n²            |
| Insertion  | T(n) = 0          | O(1)             | 0           | n²            |
| Merge Sort | O(n log n)       | O(n)             | 0           | n²            |

## Time Complexity Comparison

| Method    | Best Case         | Worst Case      | Average Time     | Space Complexity |
|-----------|-------------------|------------------|------------------|------------------|
| Merge Sort | T(n) = 0          | T(n) = n²        | T(n) = 0.5      | O(1)             |
| Insertion | T(n) = 0          | T(n) = n²        | T(n) = 1.25     | O(1)             |
| Merge Sort| T(n) = n log n    | T(n) = 2.56      | T(n) = 3.0     | O(log n)         |

## Space Complexity

- **O(n)** for the recursion stack
- **O(n)** for the auxiliary array

## Time and Space Analysis

- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n) for recursion stack + auxiliary array
- Used for efficient sorting without auxiliary storage

'''

''' qwen3.5:0.8b, explanation is okay
## Notes

- This implementation uses O(n) space due to the recursive call stack
- Time complexity is optimal with O(n log n) for sorted arrays
- Used for educational purposes in Python
- Suitable for educational applications where O(n) memory is acceptable

## Summary

- **Merge Sort** is O(n log n) time-efficient for unsorted arrays with stable sorting
- **Space Complexity**: O(n) - recursive call stack is efficient
- **Best Use Cases**: Medium-sized arrays, stable sorting, educational examples
- **Implementation**: Step-by-step iterative approach for clarity and correctness
'''
