'''
Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, return the area of the largest rectangle 
in the histogram.
'''
type List = List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # in example 1, I have rectangle areas equal to the heights
        # then I also have 10 (5 x 2), 4 (2 x 2), 8 (2 x 4), 6 (1 x 6)
        # want to account for all of these areas in stack
        # for every bar, could traverse forwards and backwards
        # to calculate all the areas, but that's expensive
        # the data structure is a monotonic stack, so how can I use that?
        # use a monotonic stack somehow... don't know
        
        # how to use monotonic stack:
        # maintain a monotonic stack
        # if encounter a shorter bar, then pop from stack and calculate
        # resulting areas wrt current bar height and width between
        # current bar aand popped bar
        stack = []
        area = []

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                curr = stack.pop()
                start = stack[-1] if stack else -1
                area.append(heights[curr] * (i - 1 - start))
            stack.append(i)

        while stack:
            curr = stack.pop()
            start = stack[-1] if stack else -1
            area.append(heights[curr] * (len(heights) - 1 - start))
        return max(area)
