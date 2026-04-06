def bubble_sort(arr):
    # Bubble Sort
    n = len(arr)
    # Iterate through the array, skipping if we can't sort all the way
    for i in range(n - 1):
        # Compare current element with i+1
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If the largest element didn't bubble up, swap it with the first element
        # to ensure it bubbles up
        if not swapped:
            break
    # Return the sorted version of the array
    return arr

if __name__ == '__main__':
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = bubble_sort(numbers)

    print("Original Array:", numbers)
    print("Sorted Array:", sorted_numbers)
    
    # This is boilerplate testing code that I give to every one
    from random import randint
    print("")
    for i in range(10):
        arr = [randint(-100, 100) for i in range(20)]
        print("Original list:", arr)
        sorted_arr = bubble_sort(arr)
        print("Is it sorted?:", sorted_arr == sorted(arr))
        print("")
    
'''
## Performance Comparison

| Method    | Best Case         | Worst Case      | Average Time     |
|-----------|-------------------|------------------|------------------|
| Bubble    | T(n) = 0          | T(n) = n²        | T(n) = 0.5      |
| Insertion | T(n) = 0          | T(n) = n²        | T(n) = 1.25    |
| Merge Sort| T(n) = n log n    | T(n) = 2.56      | T(n) = 3.0     |

## Time Complexity

- **Bubble Sort** is a simple algorithm that sorts the entire array in place using comparisons.
- **Best Case** time complexity: T(n) = 0 (when array is already sorted)
- **Worst Case** time complexity: T(n) = n² (unsorted array)
- **Average** time complexity: T(n) = n²

## Space Complexity

- O(1) for Bubble Sort (no auxiliary space used)

## Summary

- Time Complexity: O(n²)
- Space Complexity: O(1)
- Used for small, fast sorting in simple algorithms
- Suitable when memory constraints are not an issue
'''