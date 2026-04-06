class MaxHeap:
    def __init__(self):
        """
        Initializes an empty max heap.
        """
        self.heap = []

    def insert(self, value):
        """
        Inserts a new value into the max heap.

        Args:
            value (int): The value to be inserted.
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        """
        Deletes and returns the maximum element from the max heap.

        Returns:
            int: The maximum element deleted.
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def extract_max(self):
        """
        Extracts and returns the maximum element from the max heap without deleting it.

        Returns:
            int: The maximum element extracted.
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        for i in range(len(self.heap)):
            if self.heap[i] > max_value:
                max_value = self.heap[i]

        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        """
        Heapifies the subtree rooted at the given index upwards.

        Args:
            index (int): The index of the node to heapify up.
        """
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """
        Heapifies the subtree rooted at the given index downwards.

        Args:
            index (int): The index of the node to heapify down.
        """
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        largest = index
        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] > self.heap[largest]
        ):
            largest = left_child_index
        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] > self.heap[largest]
        ):
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

# Example usage:
from heapq import heappush, heappop
if __name__ == '__main__':
    # compare to heapq
    test_heap = []
    heappush(test_heap, -10)
    heappush(test_heap, -20)
    heappush(test_heap, -5)
    print(-heappop(test_heap))
    print(-test_heap[0])
    
    # Given from hk-devbrains
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(5)
    print(max_heap.delete_max())  # Output: 20
    print(max_heap.extract_max())  # Output: 10
    
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
    print("Maximum value:", max_heap.extract_max()) # 25
    
    print("Heapq's Maximum value:", -heappop(test_heap)) # 25
    print("Heapq's Max Heap:", [-i for i in test_heap]) # [20, 15, 10, 5, 10]
    print("Maximum value:", max_heap.delete_max()) # 25
    print("Max heap:", max_heap.heap) # [20, 15, 10, 5, 10]