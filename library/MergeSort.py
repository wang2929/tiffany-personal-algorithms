'''
In-place version of MergeSort to save space
https://www.geeksforgeeks.org/dsa/in-place-merge-sort/
'''
class MergeSort():
    def merge(self, arr, start, middle, end):
        left, right = start, middle+1
        # keep two pointers to compare two split arrays
        while (left <= middle and right <= end):
            # left val < right val: keep shifting left index
            if (arr[left] <= arr[right]):
                left += 1
            # else put the arr[right] to the left index and shift left to the right
            else:
                index = right
                # shifting by swaps
                while (index > left):
                    arr[index], arr[index-1] = arr[index-1], arr[index]
                    index -= 1
                # adjust indices
                left += 1
                middle += 1
                right += 1

    def mergeSort(self, arr, start, end):
        if (start < end):
            middle = start + (end - start) // 2
            self.mergeSort(arr, start, middle)
            self.mergeSort(arr, middle+1, end)
            self.merge(arr, start, middle, end)
            
if __name__ == '__main__':
    arr = [2,0,2,1,1,0]
    arr = [0,0,1,0,1,1]
    MergeSort().mergeSort(arr, 0, len(arr) - 1)
    print(arr)