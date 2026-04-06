def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Create a list to hold all subarrays
    subarrays = []

    # Split the array into individual subarrays
    for i in range(len(arr)):
        subarray = [arr[i]]
        subarrays.append(subarray)

    # Sort each subarray using the merge_sort function
    sorted_subarrays = [merge_sort(subarray) for subarray in subarrays]

    # Merge the sorted subarrays to get the final sorted array
    return merge(sorted_subarrays)

def merge(arr1, arr2):
    merged_array = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # Append any remaining elements from arr1 or arr2
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

if __name__ == "__main__":
    example_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = merge_sort(example_array)
    print("Sorted array is:", sorted_array)

''' qwen2.5-coder:3b
### Explanation:
1. **Merge Sort Function (`merge_sort`):**
   - If the length of the array is less than or equal to 1, it is already sorted, so return it.
   - Split the array into individual subarrays and store them in a list called `subarrays`.
   - For each subarray, recursively apply the merge_sort function.
   - Merge the sorted subarrays using the `merge` function.

2. **Merge Function (`merge`):**
   - Initialize two pointers, `i` and `j`, to traverse through the two arrays being merged.
   - Compare elements at `arr1[i]` and `arr2[j]`. Append the smaller element to the `merged_array` and move the corresponding pointer.
   - Continue this process until one of the subarrays is exhausted.
   - Append any remaining elements from the other subarray to the `merged_array`.

3. **Example Usage:**
   - Define an example array.
   - Call the `merge_sort` function on the array.
   - Print the sorted array.

This implementation of Iterative Merge Sort uses a list to store all subarrays and leverages several helper functions for merging the subarrays.
'''
