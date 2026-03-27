'''
Calculate the product of an element in an array not including the element
Thought process: Calculate prefix and suffix products
Relative to element in nums[i], where len(nums) is n:
    Prefix product: product of elements from k = 0 to i
    Suffix product: product of elements from k = i+1 to n
'''
class Solution:
    def productExceptSelf(self, nums):
        ret = [1] * len(nums)
        # prefix product
        prod = 1
        for i in range(len(nums)):
            ret[i] *= prod
            prod *= nums[i]
        # suffix product
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            ret[i] *= prod
            prod *= nums[i]
        return ret