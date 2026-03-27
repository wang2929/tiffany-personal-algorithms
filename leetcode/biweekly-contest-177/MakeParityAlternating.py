class Solution:
    def assignAlternating(self, old_nums, max_val, min_val):
        nums = old_nums[:]
        temp_min, temp_max = False, False
        ops = 0
        review = {}
        for i in range(1, len(nums)):
            if nums[i-1]&1 == nums[i]&1:
                val1, val2 = self.changeParity(nums[i], max_val, min_val)
                if val1 != val2:
                    review[i] = [val1, val2]
                nums[i] = val1
                ops += 1
        for index, elemList in review.items():
            if index != 0:
                temp_min, temp_max = nums[0], nums[0]
            else:
                temp_min, temp_max = nums[1], nums[1]
            arr = nums[:index] + nums[index+1:]
            for elem in arr:
                if elem < temp_min: temp_min = elem
                elif elem > temp_max: temp_max = elem
            if elemList[0] < temp_min or elemList[0] > temp_max:
                nums[index] = elemList[1]
        max_val, min_val = max(nums), min(nums)
        return ops, max_val, min_val
        
    def changeParity(self, number, max_val, min_val):
        if number == max_val:
            return number - 1, number - 1
        elif number == min_val:
            return number + 1, number + 1
        else:
            # default decrease because why not BECAUSE IT'S THE WRONG FING ANSWER THAT'S WHY
            if (max_val - number) < (min_val - number):
                return number - 1, number - 1
            elif (number - min_val) < (max_val - number):
                return number + 1, number + 1
            else:
                return number - 1, number + 1
    '''
    Create an array with alternating signs
    Return # ops required and difference of max - min
    Minimize max - min
    '''
    def makeParityAlternating(self, nums):
        # sliding window problem, ugh, do not like
        _max = max(nums)
        _min = min(nums)
        _diff = _max - _min
        if len(nums) == 1:
            return [0, 0]
        elif len(nums) == 2:
            if nums[0]&1 == nums[1]&1:
                ret = [1, 1] if _diff == 0 else [1, _diff - 1]
                return ret
            else:
                return [0, _diff]
        # Problem with the assignAlternating function
        # check first parity
        ops1, max1, min1 = self.assignAlternating(nums, _max, _min)
        nums_2 = nums[:]
        val1, val2 = self.changeParity(nums_2[0], _max, _min)
        nums_2[0] = val1
        ops2, max2, min2 = self.assignAlternating(nums_2, max(nums_2), min(nums_2))
        if val1 != val2:
            nums_2[0] = val2
            ops2_2, max2_2, min2_2 = self.assignAlternating(nums_2, max(nums_2), min(nums_2))
            if ops2_2 < ops2:
                ops2, max2, min2 = ops2_2, max2_2, min2_2
        ops2 += 1
        
        if ops1 < ops2:
            return [ops1, max1 - min1]
        elif ops2 < ops1:
            return [ops2, max2 - min2]
        else:
            if (max1-min1) < (max2-min2):
                return [ops1, max1 - min1]
            else:
                return [ops2, max2 - min2]
        
test = Solution()
print(test.makeParityAlternating([-4,-4,-3,-5,-4])) # expect 2, 1
print(test.makeParityAlternating([-4,-4,-4,-3,-5,-3])) # expect 2, 1
print(test.makeParityAlternating([1,1,1,1,1])) # expect 2, 1
print(test.makeParityAlternating([9,-1,-1,4,-2])) # expect 2, 10
print(test.makeParityAlternating([-4,-2,7,-5])) # [2, 11]
print(test.makeParityAlternating([0, 7, 3])) # [1, 7]
print(test.makeParityAlternating([9,-8,-2,9])) # [8, -7, -2, 9], [2, 16]
print(test.makeParityAlternating([2,-8,-2,9])) # [2, -7, -2, 9], [1, 16]
print(test.makeParityAlternating([9,2,-2,8])) # [9, 2, -1, 8] [1, 10]
print(test.makeParityAlternating([-2,-3,1,4])) # expect 2, 6
print(test.makeParityAlternating([0, 2, -2])) # expect 1, 3
print(test.makeParityAlternating([7])) # expect 0, 0
print(test.makeParityAlternating([3, 7])) # expect 1, 3
print(test.makeParityAlternating([7, 7])) # expect 1, 1
