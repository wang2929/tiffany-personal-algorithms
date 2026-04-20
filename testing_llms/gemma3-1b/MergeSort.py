# Tester note: this class doesn't work at all
# class MergeSort:
#   """
#   Implementation of Merge Sort algorithm.
#   """

#   def __init__(self):
#     self.arr = []

#   def merge(self, left, right):
#     """
#     Merges two sorted arrays into a single sorted array.
#     """
#     n = len(left)
#     if n == 0:
#       return
#     if n == 1:
#       return

#     mid = n // 2
#     self.left = [left[i] for i in range(mid)]
#     self.right = [right[i] for i in range(mid)]

#     self.merge(left, right)

#     self.left = self.left[len(left):]
#     self.right = self.right[len(right):]

#     self.merge(self.left, self.right)

#   def sort(self):
#     """
#     Sorts the array using Merge Sort.
#     """
#     self.merge(self.arr, [])

#   def __str__(self):
#     return "MergeSort(arr=[{}, {}, {}, {}, {}])"

def merge_sort(arr):
  """
  Sorts an array using the Merge Sort algorithm.
  """
  if len(arr) <= 1:
    return arr  # Base case: already sorted

  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  left_merge = merge_sort(left)
  right_merge = merge_sort(right)

  return merge(left_merge, right_merge)


def merge(left, right):
  """
  Merges two sorted arrays into a single sorted array.
  """
  result = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  # Add any remaining elements from left
  while i < len(left):
    result.append(left[i])
    i += 1

  # Add any remaining elements from right
  while j < len(right):
    result.append(right[j])
    j += 1

  return result

# Example usage
if __name__ == "__main__":
  arr = [10, 7, 8, 9, 1, 5]
  sorted_arr = merge_sort(arr)
  print(sorted_arr)  # Output: [1, 5, 7, 8, 9, 10]


# Tester note: This implementation doesn't work at all
# Example Usage
# if __name__ == "__main__":
#   merge_sort = MergeSort()
#   merge_sort.arr = [10, 7, 8, 9, 1, 5]
#   merge_sort.sort()  # Call the sort method
#   print(merge_sort)