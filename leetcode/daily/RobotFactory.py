type List = List

class Solution:
    def cutOffEnd(self, arr:List[List[int]], dir:str):
        indices = range(len(arr)) if dir == "left" else range(len(arr)-1, -1, -1)
        
        dist, factory = [], -1
        for i in indices:
            pos, limit = arr[i]
            if factory < 0 and limit != 0:
                factory = i
            
            if limit == 0:
                dist.append(pos)
            elif factory < 0 and limit > 0: # found first factory
                factory = i
                
            # case: found the factory
            if factory >= 0:
                fac_pos, fac_limit = arr[factory]
                # cut off array and return if factory is full
                if fac_limit == len(dist):
                    arr[:] = arr[(i+1):] if dir == "left" else arr[:i]
                    dist = [abs(d - fac_pos) for d in dist]
                    return sum(dist)
                    
            
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # ideally, robot gets repaired at nearest factory
        # if there's a case where it cannot, then that's a problem
        # I could calculate all solutions and store in a min heap, 
        # but I'll probably get dinged on time
        # if f = len(factory) and r = len(robot), then it's f^r options
        # I need something better than that, but how do I get there?
        
        # hint: sort robots and factories by location
        robots_and_factories = [[r, 0] for r in robot] + factory
        robots_and_factories = sorted(robots_and_factories)
        
        # then calculate the subsegment of robots each factory must fix
        # how do I do that...
        # if robots_and_factories = (1,0), (2,0), (3,0), (4,1), (7,2), (8,0), (9,4), (10,0), (11,0)
        # it's easiest to calculate the robots on the ends (left of leftmost factory, right of rightmost factory)
        # because they really only have one realistic choice
        ret = 0
        total_capacity = sum([f[1] for f in factory])
        if total_capacity < len(robot):
            # shouldn't happen but I put this here
            return -1
        elif total_capacity == len(robot):
            # every factory must operate at full capacity: can do this without worrying
            while len(robots_and_factories) > 0:
                ret += self.cutOffEnd(robots_and_factories, "left")
                ret += self.cutOffEnd(robots_and_factories, "right")
        else:
            # have more capacity than robots, so need to take into account minimum distances now
            # not all robots can choose a factory; only ones between two factories should
            # be able to choose which one to go to
            # this is the case where worst case scenario is close to f^r I think
            # robots on the left or right extreme will be cut, then robots in the
            # middle are tried, min distances first and if that doesn't work, then
            # try second min distances until a solution is found
            ret = -1
        # since I keep cutting off the robots_and_factories, I can keep cutting until the length is zero
        return ret
            

        

if __name__ == '__main__':
    solver = Solution()
    robot = [0, 4, 6]
    factory = [[2, 2], [6, 2]]
    print(solver.minimumTotalDistance(robot, factory))