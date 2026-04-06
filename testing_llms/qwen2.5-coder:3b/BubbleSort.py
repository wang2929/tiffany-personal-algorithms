def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

if __name__ == "__main__":
    example_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(example_array)
    print("Sorted array is:", sorted_array)
    
    # This is boilerplate testing code that I give to every one
    from random import randint
    print("")
    for i in range(10):
        arr = [randint(-100, 100) for i in range(20)]
        print("Original list:", arr)
        sorted_arr = bubble_sort(arr)
        print("Is it sorted?:", sorted_arr == sorted(arr))
        print("")
    
'''### from qwen2.5-coder
Explanation:
1. **Outer Loop (`for i in range(n)`):**
   - This loop iterates over each position in the array up to the last unsorted element.

2. **Inner Loop (`for j in range(0, n-i-1)`):**
   - This loop compares each pair of adjacent elements and swaps them if they are in the wrong order.
   - The `n-i-1` adjustment is used because after each iteration, the largest unsorted element "bubbles up" to its correct position.

3. **Swapping Condition (`if arr[j] > arr[j+1]:`):**
   - If the current element is greater than the next element, a swap is performed by swapping them using tuple unpacking `(arr[j], arr[j+1]) =
(arr[j+1], arr[j])`.

4. **Return Statement:**
   - The function returns the sorted array.

### Example:
For the input array `[64, 34, 25, 12, 22, 11, 90]`, the output will be `[11, 12, 22, 25, 34, 64, 90]`.

This algorithm has a time complexity of \(O(n^2)\), which makes it inefficient for large datasets. However, it is easy to understand and implement,
making it a good starting point for educational purposes or simple applications.
'''