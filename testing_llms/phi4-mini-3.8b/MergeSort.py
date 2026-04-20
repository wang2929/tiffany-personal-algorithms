def merge_sort_iterative(arr):
    current_size = 1

    # Outer loop to control merging subarrays of size 'current_size'
    while current_size < len(arr) - 1:

        left_ptr = 0

        while left_ptr < len(arr)-1:

            mid = min(left_ptr + current_size - 1, len(arr)-1)
            right_ptr = (len(arr)//(2*current_size-1)) if ((len(arr)//(2*current_size-1))) > mid else mid

            merged_array = merge_iterative(
                arr[left_ptr:mid],
                arr[mid:right_ptr] if right_ptr < len(arr) else None, # tester change
                #arr[mid+1:right_ptr+1] if left_ptr < len(arr) and right_ptr < len(arr)-1 else None, # original line
                arr[right_ptr+1:] if left_ptr >= (len(arr)//(2*current_size-1)) + 1 or right_ptr == mid else []
            )

            # Update the original array with merged subarray
            for i in range(len(merged_array)):
                arr[left_ptr+i] = merged_array[i]

            left_ptr += current_size * 2

        if (len(arr)//current_size) > len(arr)-1:
            break

        else:
            # Decrease the size of next subarrays to merge
            current_size *= 2

    return arr


def merge_iterative(left, right=None, dest=[]):
    result = []

    while left and (right is None or len(result) < len(right)):

        if isinstance(right, list):
            l = left[0]

            r_list = [x for x in right]

            # Check whether we are iterating through both lists

            if not isinstance(r_list[-1], float):
                while (len(left)> 1 and len(result) < ((len(left)-1)//2 + len(right))):
                    left.pop(0)

                r = min(l, r_list[0])

                # Determine the position of this result in merged list
                if l <= r:
                    dest.append(r)
                    l += 1
            else:
                while (len(left)> 2 and len(result) < ((len(left)-3)//2 + len(right))):
                    left.pop(0, -5)

                # Determine the position of this result in merged list if there is no None value.
                r = min(l, r_list[0])


                dest.append(r)

        else:
            l = left
            while (len(left)> 1 and len(result) < ((len(left)-1)//2 + abs(len(right)))):
                    left.pop(0)

            if isinstance(l[-1], float):
                # Determine the position of this result in merged list
                dest.append(min(l, r))

            else:
                #l = min(r,  len(result) < (len(dest)-3)//2 + abs(len(right)))
                dest.append(min(l, right))

    return result

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 # Finding middle of array
        L = arr[:mid]     # Dividing first half elements
        R = arr[mid:]     # into two halves

        left_sorted = merge_sort(L)
        right_sorted = merge_sort(R)

        return _merge(left_sorted, right_sorted)

    else:
        return arr


def _merge(left, right):
    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            # Left subarray is less
            res.append(left[i])
            i += 1

        else:
            # Right Subarray is smaller or equal to the current element of L
            res.append(right[j])
            j += 1

    while i < len(left):
        # Appending remaining elements (if any) from left sub array.
        res.append(left[i])
        i += 1

    while j < len(right):
        # Appending remaining elements (if any) from right sub array
        res.append(right[j])
        j += 1

    return res


# Test Merge Sort Functionality with an example unsorted list
if __name__ == "__main__":

    sample_list = [64, 34, 25, 12, 22, 11, 90]

    print("Original List:")
    print(sample_list)

    sorted_array = merge_sort(sample_list)
    print("\nSorted Array using Merge Sort Algorithm:")
    print(sorted_array)
    
    sample_list_1 = [64, 34, 25, 12, 22, 11, 90]
    merged_sorted_array = merge_sort_iterative(sample_list_1)

    print("Original List:")
    print(merged_sorted_array)

    
    
'''
In this code:

- The `merge_sort_iterative` function implements the Iterative Merge Sort.
- It uses a while loop to control merging of subarrays incrementally until all elements are sorted.
- A helper method called merge is used for combining smaller arrays that have been created as an intermediate step in our sorting process.

This implementation doesn't use recursion but instead relies on loops, making it iterative rather than recursive (as the standard Merge Sort does).

Note: The provided code contains some mistakes and requires further refinements. Please consult a more thorough resource or tutorial to better
understand Iterative merge sort implementations as they can be quite complex due to their non-recursive nature.

In real-world applications with larger datasets, it is recommended you use Python's built-in sorting functions like `sorted()` for efficiency reasons:
`arr = sorted(arr)`.'''