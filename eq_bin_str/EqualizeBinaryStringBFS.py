'''
Most recent timing on test 13 (50k chars): 44s
'''

# running: python -m unittest EqualizeBinaryString.TestClass
class Solution:
    # moves format: (<flip 0s to 1s>, <flip 1s to 0s>)
    def findLegalMoves(self, zeros, k, total):
        # choose up to k zeros to flip
        min_zeros = max(0, k-(total-zeros))
        max_zeros = min(zeros, k) + 1
        return min_zeros, max_zeros
    
    def minOperations(self, s: str, k: int) -> int:
        zeros_left = s.count('0')
        total = len(s)
        if zeros_left == 0:
            return 0
        # dictionaries for checking inclusion quickly, then frontier is a queue
        frontier_tracker, reached, frontier = {}, {}, []
        reached[zeros_left] = 0
        min_zeros, max_zeros = self.findLegalMoves(zeros_left, k, total)
        start = zeros_left

        # load the frontier here
        for i in range(min_zeros, max_zeros):
            # formula: zeros_left = prev_zeros - zeros + (k - zeros) = prev_zeros + k - 2*zeros
            zeros_left = start + k - 2*i
            if zeros_left <= total:
                if zeros_left not in frontier_tracker:
                    if zeros_left == 0:
                        return 1
                    frontier.append((zeros_left, 1))
                    frontier_tracker[zeros_left] = True
        
        for zeros_left, number_of_moves in frontier:
            reached[zeros_left] = number_of_moves
            min_zeros, max_zeros = self.findLegalMoves(zeros_left, k, total)
            for i in range(min_zeros, max_zeros):
                child_zeros_left = zeros_left + k - 2*i
                child_number_of_moves = number_of_moves + 1
                if child_zeros_left <= total and child_zeros_left not in reached and child_zeros_left not in frontier_tracker:
                    if child_zeros_left == 0:
                        return child_number_of_moves
                    frontier.append((child_zeros_left, child_number_of_moves))
                    frontier_tracker[child_zeros_left] = True
        # reach here if no solution
        return -1

soln = Solution()
print(soln.minOperations('0101', 3)) #2
