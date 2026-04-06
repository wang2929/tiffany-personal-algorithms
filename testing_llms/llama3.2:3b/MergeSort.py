def merge_sort_recursive(arr):
    """
    Sorts an array using recursive merge sort.

    Args:
        arr (list): The input list to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort_recursive(left_half)
    right_half = merge_sort_recursive(right_half)

    # Merge the sorted halves
    return merge_recursive(left_half, right_half)


def merge_recursive(left, right):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.

    Returns:
        list: The merged sorted list.
    """
    merged = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # Append any remaining elements
    merged.extend(left)
    merged.extend(right)

    return merged

def merge_sort_iterative(arr):
    # If the array has only one element or is empty
    if len(arr) <= 1:
        return arr

    ret = arr.copy()
    size = 1 # editor's note: trying size = 1 to start, originally size = 2
    while size < len(ret):
        for i in range(0, len(ret), size * 2):
            left = ret[i:i + size]
            right = ret[i + size:i + size * 2]

            # Merge smaller subarrays
            ret[i:i + size * 2] = merge_iterative(left, right)

        size *= 2

    return ret

def merge_iterative(left, right):
    merged = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # If there are remaining elements in either subarray, append them to the merged array
    merged += left
    merged += right

    return merged

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = merge_sort_recursive(arr)
    print("Sorted array:", sorted_arr)
    
    # This is boilerplate testing code that I give to every one
    from random import randint
    print("Recursive Merge Sort")
    for i in range(10):
        arr = [randint(-100, 100) for i in range(20)]
        sorted_arr = merge_sort_recursive(arr)
        print("Is it sorted?:", sorted_arr == sorted(arr))
        
    print("\nIterative Merge Sort")
    for i in range(10):
        arr = [randint(-100, 100) for i in range(20)]
        sorted_arr = merge_sort_iterative(arr)
        print("Is it sorted?:", sorted_arr == sorted(arr))
    
''' From Llama3.2
### Explanation

1.  The `merge_sort()` function takes an input list and recursively splits it into two halves until each half has only one element.
2.  The `merge()` function merges two sorted lists into a single sorted list by comparing elements from both lists and appending the smaller one to
the result.
3.  The iterative merge sort algorithm uses two temporary arrays to store the left and right halves of the input array, allowing it to avoid using
recursion.

### Time Complexity

*   Best-case: O(n log n)
*   Worst-case: O(n log n)
*   Average-case: O(n log n)

Note that merge sort has a time complexity of O(n log n) in all cases, making it suitable for large datasets. However, it requires more memory than
some other sorting algorithms due to the need for temporary arrays.
'''
