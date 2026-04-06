'''
You are given an array of integers temperatures 
where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after 
the ith day before a warmer temperature appears on a future day. 
If there is no day in the future where a warmer temperature will 
appear for the ith day, set result[i] to 0 instead.
'''
type List[int] = List[int]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack stores days without warmer day yet
        stack = []
        # return array
        ret = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            # warmer day found
            while stack and t > stack[-1][0]:
                # clear the stack until a warmer day is found
                temp, index = stack.pop()
                # update the number of days since value
                ret[index] = i - index
            stack.append((t, i))
        return ret

if __name__ == '__main__':
    print(Solution().dailyTemperatures([30,38,30,36,35,40,28])) # [1,4,1,2,1,0,0]