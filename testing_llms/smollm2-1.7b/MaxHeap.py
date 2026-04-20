class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)

    def delete(self):
        if len(self.heap) == 0:
            return None

        # If the heap has only one element, remove it and make the list empty
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Replace the root with the last element in the heap
        self.heap[0] = self.heap.pop()
        # Heapify down to maintain max-heap property
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2

        while index > 0 and self.heap[parent_index] < self.heap[index]:
            # Swap elements if the parent is smaller than the child
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]

            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        largest_index = index

        # Find the largest child in the heap
        if (left_child_index < len(self.heap) and
            self.heap[left_child_index] > self.heap[largest_index]):
            largest_index = left_child_index

        if (right_child_index < len(self.heap) and
            self.heap[right_child_index] > self.heap[largest_index]):
            largest_index = right_child_index

        # Swap elements if the child is larger than the parent
        if largest_index != index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]

            # Recursively heapify down to maintain max-heap property
            self._heapify_down(largest_index)

if __name__ == '__main__':
    # compare to heapq
    from heapq import heappush, heappop
    test_heap = []
    heappush(test_heap, -10)
    heappush(test_heap, -20)
    heappush(test_heap, -15)
    heappush(test_heap, -7)
    heappush(test_heap, -5)
    heappush(test_heap, -9)
    heappush(test_heap, -8)
    print("Compare to heapq")
    print("Heapq's Maximum value:", -heappop(test_heap)) # 20
    print("Heapq's Maximum value:", -heappop(test_heap)) # 15
    print("Heapq's Maximum value:", -heappop(test_heap)) # 10
    print("Heapq's Maximum value:", -heappop(test_heap)) # 9
    print("Heapq's Maximum value:", -heappop(test_heap)) # 8
    print("Heapq's Maximum value:", -heappop(test_heap)) # 7
    print(test_heap)
    
    # smollm2:1.7b
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(15)
    max_heap.insert(7)
    max_heap.insert(5)
    max_heap.insert(9)
    max_heap.insert(8)
    print("\nSmollm:1.7b implementation")
    print(max_heap.delete())  # prints 20
    print(max_heap.delete())  # prints 15
    print(max_heap.delete())  # prints 10
    print(max_heap.delete())  # prints 9
    print(max_heap.delete())  # print 8
    print(max_heap.delete())  # print 7
    print(max_heap.heap)