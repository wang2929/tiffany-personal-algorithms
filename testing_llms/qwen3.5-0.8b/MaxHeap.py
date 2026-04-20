class MaxHeap:
    '''
    ## Key Methods

    | Method | Description |
    |--------|-------------|
    | `__init__(self, elements=None)` | Initialize the heap with optional initial elements |
    | `make_max_heap()` | Create a new max heap from the initial elements |
    | `set_max_element()` | Add an element to the max value at the root |
    | `get_max_value()` | Return the maximum element from the heap |
    | `make_parent()` | Set the parent of a node |
    | `get_child()` | Get the child of a node |
    | `set_child()` | Set the child of a node |
    | `parent()` | Find the parent of a node |
    | `child()` | Find the child of a node |
    | `max()` | Get the maximum element |
    | `__str__()` | Print heap as string |
    '''
    def __init__(self, elements=None, parent=None, child=None):
        """
        Initialize the MaxHeap with optional elements, parent, and children
        """
        self.elements = []
        self.n = 0
        self.max_val = -100000
        self.parent = None
        self.child = None
        self.root = None

    def set_max_element(self, value):
        """Set the max element at the root"""
        self.n = self.n if self.n > 0 else 1
        if self.max_val < value:
            self.max_val = value
        self.root = self.elements[0]

    def get_max_value(self):
        """Get the maximum element"""
        if self.n == 0:
            raise ValueError("Heap is empty")
        return self.elements[self.n - 1]

    def get_max_index(self):
        """Get the index of the maximum element"""
        if self.n > 0:
            return self.n - 1
        return self.n - 1

    def make_max_heap(self):
        """
        Create a new max heap from the elements
        """
        if self.n > 0:
            self.max_val = -100000
        else:
            self.max_val = 0

        self.elements = [self.get_max_index() for i in range(len(self.elements))]

        if len(self.elements) > 0:
            self.elements[0] = self.n - 1

        self.parent = None
        self.child = None

        # Rebuild heap with elements
        for i in range(self.n - 1):
            self.elements[self.n - 1 - i] = self.max_element(self.elements[self.n - 1 - i])

        self.max_element = self.elements[-1]

        # Find root and rebuild
        self.parent = self.n - 1
        self.child = self.parent if self.parent is not None else self.n - 1

        # Set max index as the parent
        if self.n == 1:
            self.max_index = 0
        else:
            self.max_index = 1

        # Set root as the max element
        self.root = self.n - 1

    def get_max_element(self):
        """Get the maximum element"""
        if self.n == 0:
            return -100000
        return self.elements[0]

    def make_parent(self, value):
        """
        Set the parent of a node with a given value
        """
        self.max_val = -100000
        self.n = self.n if self.n > 0 else 1
        if self.n > 0:
            self.max_val = value
        self.parent = self.n - 1

    def set_child(self, value):
        """
        Set the child of a node with a given value
        """
        self.max_val = -100000
        self.n = self.n if self.n > 0 else 1
        if self.n > 0:
            self.max_val = value
        self.parent = self.n - 1

    def set_child_node(self, value):
        """
        Set the child node of a node
        """
        self.max_val = -100000
        self.n = self.n if self.n > 0 else 1
        if self.n > 0:
            self.max_val = value # qwen3.5:0.8b made an error
        self.parent = self.n - 1

    def get_parent(self, node):
        """
        Get the parent of a node
        """
        return self.parent

    def set_parent(self, parent_value):
        """
        Set the parent of a node
        """
        self.max_val = -100000
        self.n = self.n if self.n > 0 else 1
        if self.n > 0:
            self.max_val = parent_value # qwen3.5:0.8b made an error
        self.parent = parent_value

    def get_child(self, node):
        """
        Get the child of a node
        """
        return self.child

    def __str__(self):
        return "MaxHeap: max_element={}, children={}, nodes={}, total_nodes={}".format(
            self.max_element, self.n, len(self.elements), 0)

        return self.__str__()
    
if __name__ == "__main__":
    ''' qwen3.5:0.8b wrote this in a main function but this is gibberish
    success = main()
    if success:
        print("✓ Max-Heap creation successful!")
    else:
        print("✗ Max-Heap creation failed!")
    '''
    # Create max heap
    elements = [5, 4, 2, 3, 1]
    heap = MaxHeap(elements=elements)

    # Set maximum value
    heap.set_max_element(1) # index out of range error

    # Access maximum element
    print("Max element:", heap.get_max_element())

    # Set parent of element
    heap.set_parent(heap.get_max_index())

    # Get child of element
    print("Child of root:", heap.get_child(heap.get_max_element()))

    # Print heap info
    print("Max-Heap:", heap)

    # Check if heap is valid
    if heap.get_max_element() > heap.max_element:
        print("Invalid heap!")
    else:
        print("✓ Heap is valid")