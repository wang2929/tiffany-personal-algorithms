def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.
    """

    # Get the length of the array
    n = len(arr)

    # Repeat the process until the entire array is sorted
    for i in range(n):

        # Initialize a flag to track if any swaps were made
        swapped = False

        # Iterate through each element in the array
        for j in range(0, n - i - 1):

            # If the current element is greater than the next one, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps were made in the inner loop, the array is sorted
        if not swapped:
            break

    return arr

if __name__ == '__main__':
    # Example usage
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)
    
    from random import randint

    # This is boilerplate testing code that I give to every one
    print("")
    for i in range(10):
        arr = [randint(-100, 100) for i in range(20)]
        print("Original list:", arr)
        sorted_arr = bubble_sort(arr)
        print("Sorted array:", sorted_arr)
        print("Is it sorted?:", sorted_arr == sorted(arr))
        print("")

''' hk-devbrain explanation
### Overview

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong
order. The pass through the list is repeated until the list is sorted.

### Explanation

1. The `bubble_sort` function takes an input array `arr` and returns the sorted array.
2. We start by getting the length of the array `n`.
3. We then enter a loop that repeats until the entire array is sorted.
4. Inside the outer loop, we iterate through each element in the array using the inner loop.
5. If the current element is greater than the next one, we swap them using tuple assignment.
6. After each iteration of the inner loop, we check if any swaps were made. If not, it means the array is already sorted and we can break out of the
outer loop.
7. Finally, we return the sorted array.

### Time Complexity

The time complexity of Bubble Sort is O(n^2), where n is the number of elements in the array. This makes it less efficient than other sorting
algorithms like QuickSort or MergeSort for large datasets. However, it has the advantage of being simple to implement and understand.
'''