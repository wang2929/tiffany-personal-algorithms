from heapq import heappush, heappop
# need a better criteria for no solution than a timeout
# need to remove redundant states
class OLD_Solution:
    def findLegalMoves(self, state, k):
        # can flip up to k ones and zeros
        # first find all the zero indices
        zero_indices, one_indices, moves = [], [], []
        for i in range(len(state)):
            if state[i] == '0':
                zero_indices.append(i)
            else:
                one_indices.append(i)
        # second, choose up to k zeros to flip
        minimum = 0 if k - len(one_indices) < 0 else k - len(one_indices)
        for i in range(minimum, len(zero_indices) + 1):
            new_move = zero_indices[:i] + one_indices[:(k-i)]
            if len(new_move) == k:
                moves.append(new_move)
        return moves
    
    def priority(self, moves, zeros_left, k):
        # heavily favor states that are within range of solving
        return 5*(zeros_left % k) + (zeros_left // k) + moves

    def evaluateGoal(self, state, moves, zeros_left, k, goal):
        if (state == goal):
            return moves
        else:
            if (zeros_left % k) == 0:
                return moves + (zeros_left // k)
        return -1

    def applyMove(self, strng, indices):
        ret = list(strng)
        for i in indices:
            ret[i] = '0' if ret[i] == '1' else '1'
        return ''.join(ret)
    
    def minOperations(self, s: str, k: int) -> int:
        goal = '1'*len(s)
        zeros_left = s.count('0')
        if (try_goal := self.evaluateGoal(s, 0, s.count('0'), k, goal)) != -1:
            return try_goal
        # dictionaries for checking inclusion quickly, then frontier is a PQ
        # need to revamp trackers to check by number of zeros in a state
        frontier_tracker, reached, frontier = {}, {}, []
        reached[zeros_left] = 0
        # another optimization: change legalMoves to return only moves that make unique states
        # these moves should flip a different number of zeros at least
        legalMoves = self.findLegalMoves(s, k)

        for move in legalMoves:
            state = self.applyMove(s, move)
            zeros_left = state.count('0')
            if zeros_left not in frontier_tracker:
                heappush(frontier, (self.priority(1, zeros_left, k), state, 1, zeros_left))
                frontier_tracker[zeros_left] = 1
        
        while len(frontier) > 0:
            _, state, number_of_moves, zeros_left = heappop(frontier)
            if (try_goal:= self.evaluateGoal(state, number_of_moves, zeros_left, k, goal)) != -1:
                return try_goal
            reached[zeros_left] = number_of_moves
            legalMoves = self.findLegalMoves(state, k)
            for move in legalMoves:
                child_state = self.applyMove(state, move)
                child_zeros_left = child_state.count('0')
                if child_zeros_left not in reached:
                    if child_zeros_left not in frontier_tracker:
                        heappush(frontier, (self.priority(number_of_moves + 1, child_zeros_left, k), child_state, number_of_moves + 1, child_zeros_left))
                        frontier_tracker[child_zeros_left] = number_of_moves + 1
                    else:
                        # keep frontier clean by only adding states with a different
                        # number of zeros left (no duplicate states)
                        if frontier_tracker[child_zeros_left] > (number_of_moves + 1):
                            frontier_tracker[child_zeros_left] = number_of_moves + 1
                            frontier = [node for node in frontier if node[-1] != child_zeros_left]
                            heappush(frontier, (self.priority(number_of_moves + 1, child_zeros_left, k), child_state, number_of_moves + 1, child_zeros_left))
                    
        # reach here if no solution
        return -1
