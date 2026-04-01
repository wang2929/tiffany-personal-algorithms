from heapq import heapify_max, heappush_max
type List = List[int]

class Solution:
    def maxSlidingWindow(self, nums: List, k: int) -> List:
        ret = []
        mx = []
        for i in range(k):
            heappush_max(mx, nums[i])
        ret.append(mx[0])
        i, j = 0, k - 1
        while (j+1) < len(nums):
            j += 1
            heappush_max(mx, nums[j])
            mx.remove(nums[i])
            heapify_max(mx)
            i += 1
            ret.append(mx[0])
        return ret
    
if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1,2,1,0,4,2,6], 3))