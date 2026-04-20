def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves and merge them together
    return merge_recursive(merge_sort_recursive(left_half), merge_sort_recursive(right_half))

def merge_recursive(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append the remaining elements, if any
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def merge_sort_iterative(arr):
    if len(arr) <= 1:
        return arr

    # Create a list to store the merged and sorted subarrays
    result = []

    # Divide the array into two halves until we have arrays of size 1
    for i in range(0, len(arr), 2):
        left = [arr[i]] if i < len(arr) - 1 else arr[i:len(arr)] # slight modification to put int in a list
        right = [arr[i + 1]] if i < len(arr) - 1 else arr[i + 1:]

        # Merge the two halves together
        merged = merge_iterative(left, right)

        # Add the merged array to our result list
        result.extend(merged)

    return result # only sorts pairs, does not sort the whole list

def merge_iterative(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append the remaining elements, if any
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def merge_sort_third(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort_third(left_half)
    right_half = merge_sort_third(right_half)

    sorted_array = []
    i, j, k = 0, 0, 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1

    while i < len(left_half):
        sorted_array.append(left_half[i])
        i += 1

    while j < len(right_half):
        sorted_array.append(right_half[j])
        j += 1

    return sorted_array

if __name__ == '__main__':
    # This is my boilerplate testing code that I give to every one
    from random import randint
    print("Testing recursive version")
    for i in range(10):
        arr = [randint(-100, 100) for i in range(20)]
        sorted_arr = merge_sort_recursive(arr)
        print("Is it sorted?:", sorted_arr == sorted(arr))
        
    print("\nTesting iterative version")
    for i in range(10):
        arr = [randint(-100, 100) for i in range(20)]
        sorted_arr = merge_sort_iterative(arr)
        print("Is it sorted?:", sorted_arr == sorted(arr))
        
    # third version is still recursive, just different
    print("\nTesting a third version")
    for i in range(10):
        arr = [randint(-100, 100) for i in range(20)]
        sorted_arr = merge_sort_third(arr)
        print("Is it sorted?:", sorted_arr == sorted(arr))
