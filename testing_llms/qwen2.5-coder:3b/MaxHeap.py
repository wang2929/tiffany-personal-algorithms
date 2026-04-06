class MaxHeap:
    def __init__(self):
        # Initialize the heap list with a dummy value
        self.heap = [-1]  # Start index at 1

    def __len__(self):
        return len(self.heap) - 1

    def parent(self, i):
        return i // 2

    def left_child(self, i):
        return 2 * i

    def right_child(self, i):
        return 2 * i + 1

    def is_leaf(self, i):
        return i > len(self.heap) // 2 # tester note: check uses wrong length (should be len(self.heap) - 1)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        # Add the new value to the end of the heap
        self.heap.append(value)

        # Restore the heap property by moving the newly added element up until it is in the correct position
        i = len(self.heap) - 1
        while i > 1 and value > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def delete_max(self):
        # Swap the root element with the last element of the heap
        if not self.is_empty():
            self.swap(1, len(self.heap) - 1)

            # Remove the last element from the heap
            del self.heap[-1]

            # Restore the heap property by moving the new root element down until it is in the correct position
            i = 1
            while not self.is_leaf(i):
                left = self.left_child(i)
                right = self.right_child(i)

                if right > len(self.heap) - 1 or self.heap[right] <= self.heap[left]:
                    child_index = left
                else:
                    child_index = right

                if self.heap[child_index] > self.heap[i]:
                    self.swap(i, child_index)
                    i = child_index
                else:
                    break

    def is_empty(self):
        return len(self.heap) == 1
    
if __name__ == "__main__":
    max_heap = MaxHeap()

    # Insert some values into the heap
    max_heap.insert(5)
    max_heap.insert(9)
    max_heap.insert(3)
    max_heap.insert(7)

    print("Heap after insertion:", max_heap.heap[1:])

    # Delete the maximum element from the heap
    max_heap.delete_max() # tester note: index out of bounds error

    print("Heap after deletion of maximum element:", max_heap.heap[1:])

''' qwen2.5-coder:3b
### Explanation:
1. **Initialization (`__init__`):**
   - Initialize the heap list with a dummy value `-1`. The root of the heap is at index 1.

2. **Length Accessor (`__len__`):**
   - Return the number of elements in the heap (excluding the dummy value).

3. **Parent and Child Index Calculation:**
   - `parent(i)`: Calculate the parent index of a node.
   - `left_child(i)`: Calculate the left child index of a node.
   - `right_child(i)`: Calculate the right child index of a node.

4. **Is Leaf Node Check (`is_leaf`):**
   - Determine if a node is a leaf node based on its index.

5. **Swap Elements (`swap`):**
   - Swap two elements in the heap list.

6. **Insert Value (`insert`):**
   - Add a new value to the end of the heap.
   - Restore the heap property by moving the newly added element up until it is in the correct position.

7. **Delete Maximum Element (`delete_max`):**
   - Swap the root element with the last element of the heap.
   - Remove the last element from the heap.
   - Restore the heap property by moving the new root element down until it is in the correct position.

8. **Empty Check (`is_empty`):**
   - Determine if the heap is empty (i.e., contains only the dummy value).

This implementation of a Max-Heap uses an array to store the heap nodes and leverages several helper functions for maintaining the heap properties.
'''