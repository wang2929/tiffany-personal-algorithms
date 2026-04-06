def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False

        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(0, n-i-1):
            # If we find an element that is greater than its adjacent element then swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If there were no swaps during the last iteration, the list is already sorted, and we can terminate
        if not swapped:
            break

    return arr

# You can call this function by passing a list of elements to be sorted as an argument. 
# For example: `bubble_sort([64, 34, 25, 12, 22, 11, 90])`. 
# It will return the sorted list in ascending order.

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(arr))
    
    # This is my boilerplate testing code that I give to every one
    from random import randint
    print("")
    for i in range(10):
        arr = [randint(-100, 100) for i in range(20)]
        sorted_arr = bubble_sort(arr)
        print("Is it sorted?:", sorted_arr == sorted(arr))
        print("")