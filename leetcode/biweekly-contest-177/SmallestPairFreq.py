class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        if len(nums) <= 2:
            return [-1, -1]
        if len(set(nums)) == len(nums):
            return [-1, -1]
        vals = sorted(set(nums))
        counts = [nums.count(x) for x in vals]
        if len(set(counts)) == 1:
            return [-1, -1]
        for i in range(len(vals) - 1):
            for j in range(i, len(vals)):
                if counts[i] != counts[j]:
                    return [vals[i], vals[j]]

test = Solution()
print(test.minDistinctFreqPair([1, 5]))
print(test.minDistinctFreqPair([7]))
print(test.minDistinctFreqPair([1, 1, 2, 2, 3, 4]))
print(test.minDistinctFreqPair([3,5,4]))
print(test.minDistinctFreqPair([3, 3, 5, 5, 4, 4]))