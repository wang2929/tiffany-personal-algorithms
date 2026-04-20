def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n-1):

        # Last i elements are already sorted, no need to check them again.
        swapped = False

        for j in range(0, n-i-1):

            # Compare adjacent positions and swap if needed
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # Mark as Swapped after swapping elements.
                swapped = True

        # If no two elements were swapped by inner loop, then break the sorting process early
        if not swapped:
            break
    return arr


# Test Bubble Sort Functionality with an example list
if __name__ == "__main__":
    # sample_list = [64, 34, 25, 12, 22, 11, 90]

    # print("Original List:")
    # print(sample_list)

    # sorted_list = bubble_sort(sample_list)

    # print("\nSorted List using Bubble Sort Algorithm:")
    # print(sorted_list)
    
    # This is boilerplate testing code that I give to every one
    arr = [3, 4, 5, 6, 7, 8, 1]
    sorted_arr = bubble_sort(arr)
    print("\nIs it sorted?:", sorted_arr == sorted(arr))
    from random import randint
    print("")
    for i in range(10):
        arr = [randint(-100, 100) for i in range(20)]
        sorted_arr = bubble_sort(arr)
        print("Is it sorted?:", sorted_arr == sorted(arr))
        
'''
In this code:

- The `bubble_sort` function takes a list as an argument and sorts it in place.
- It uses nested loops to compare adjacent elements, swapping them if they are out of order. This process is
repeated until no swaps occur during the inner loop iterations (indicating that sorting has been completed).
- If any swap occurs at all within complete passes through the array, `swapped` remains True and we need another
pass.
- The main block demonstrates an example usage by applying bubble sort to a sample list.

This simple implementation is not very efficient for large datasets compared with more advanced algorithms like
quicksort or mergesort. However, it serves as good educational material due to its simplicity in demonstrating the
concept of sorting through comparisons and swaps between adjacent elements.
'''