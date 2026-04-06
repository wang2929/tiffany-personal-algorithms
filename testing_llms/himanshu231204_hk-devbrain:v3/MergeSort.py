def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.
    """

    # Create a copy of the original array for each recursive call
    if len(arr) <= 1:
        return arr

    # Initialize the width of the subarrays
    width = 1

    # Iterate through the array, increasing the width by a factor of 2 at each step
    while width < len(arr):
        left = 0
        right = width * 2

        # Merge adjacent subarrays
        for i in range(left + width, min(right, len(arr))):
            merge(arr, i - width, i, i + width)

        # Double the width for the next iteration
        width *= 2

    return arr


def merge(arr, left, mid, right):
    """
    Merges two sorted subarrays into a single sorted array.

    Args:
        arr (list): The input array.
        left (int): The starting index of the first subarray.
        mid (int): The ending index of the first subarray and the starting index of the second subarray.
        right (int): The ending index of the second subarray.
    """

    # Create temporary arrays for the two subarrays
    left_arr = arr[left:mid]
    right_arr = arr[mid:right]

    # Initialize indices for both subarrays
    i = j = 0

    # Merge smaller elements first
    k = left
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Append any remaining elements from the subarrays
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
    
    # This is boilerplate testing code that I give to every one
    from random import randint
    print("")
    for i in range(10):
        arr = [randint(-100, 100) for i in range(20)]
        print("Original list:", arr)
        sorted_arr = merge_sort(arr)
        print("Is it sorted?:", sorted_arr == sorted(arr))
        print("")