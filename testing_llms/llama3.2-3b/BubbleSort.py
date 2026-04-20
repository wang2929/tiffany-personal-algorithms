def bubble_sort(arr):
    """
    Sorts an array in ascending order using bubble sort.

    Args:
        arr (list): The input list to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)

    for i in range(n-1):

        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False

        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(n-i-1):

            # If we find an element that is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If there were no swaps during the last iteration, the array is already sorted, and we can terminate
        if not swapped:
            break

    return arr

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted list:", sorted_arr)

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
### Explanation

1. The outer loop (`for i in range(n-1):`) controls the number of passes through the array.
2. The inner loop (`for j in range(n-i-1):`) compares each pair of adjacent elements and swaps them if they are out of order.
3. A flag variable (`swapped = False`) is used to track whether any swaps were made during the last pass. If no swaps were made, it means that the
array is already sorted, and we can terminate early.

### Time Complexity

* Best-case: O(n) when the input list is already sorted.
* Worst-case: O(n^2) when the input list is in reverse order.
* Average-case: O(n^2).
'''