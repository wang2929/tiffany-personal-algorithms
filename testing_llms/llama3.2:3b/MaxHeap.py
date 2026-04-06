class MaxHeap:
    def __init__(self):
        self.heap = []

    # Get the index of the maximum element (root) in the max heap
    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    # Replace the root with a new value
    def replace_root(self, val):
        if len(self.heap) > 1 and val > self.heap[0]:
            self.heap[0] = val

    # Heapify-up: when a larger element is inserted into the heap
    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent_index] < self.heap[index]:
            temp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = temp
            self.heapify_up(parent_index)

    # Heapify-down: when the maximum element needs to be updated with a smaller value
    def heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        largest = index
        if len(self.heap) > left_child_index and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if len(self.heap) > right_child_index and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[largest]
            self.heap[largest] = temp
            self.heapify_down(largest)

    # Insert a new value into the max heap
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    # Remove and return the maximum element from the max heap
    def remove_max(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            root_val = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify_down(0)
            return root_val

# Example usage:
if __name__ == '__main__':
    # compare to heapq
    from heapq import heappush, heappop
    test_heap = []
    heappush(test_heap, -10)
    heappush(test_heap, -5)
    heappush(test_heap, -20)
    print("Heapq's Max Heap:", [-i for i in test_heap])
    print("Heapq's Maximum value:", -test_heap[0])
    
    # given test from llama3.2
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(5)
    max_heap.insert(20)
    print("Max heap:", max_heap.heap)  # [20, 10, 5]
    print("Maximum value:", max_heap.get_max())  # 20
    
    # further testing here
    max_heap.insert(25)
    max_heap.insert(15)
    max_heap.insert(10)
    heappush(test_heap, -25)
    heappush(test_heap, -15)
    heappush(test_heap, -10)
    print("Heapq's Max Heap:", [-i for i in test_heap])
    print("Heapq's Maximum value:", -test_heap[0])
    print("Max heap:", max_heap.heap) # 
    print("Maximum value:", max_heap.get_max()) # 25
    
    print("Heapq's Maximum value:", -heappop(test_heap)) # 25
    print("Heapq's Max Heap:", [-i for i in test_heap]) # [20, 15, 10, 5, 10]
    print("Maximum value:", max_heap.remove_max()) # 25
    print("Max heap:", max_heap.heap) # [20, 15, 10, 5, 10]

''' From llama3.2:3b
### Explanation

*   The `get_max()` method returns the maximum element in the max heap.
*   The `replace_root()` method updates the root of the max heap with a new value.
*   The `heapify_up()` and `heapify_down()` methods are used to maintain the max heap property after insertion or removal of elements.
*   The `insert()` method adds a new element to the max heap while maintaining the max heap property.
*   The `remove_max()` method removes and returns the maximum element from the max heap.

### Time Complexity

*   Insertion: O(log n)
*   Removal: O(log n)
'''