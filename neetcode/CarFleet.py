'''
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.
    position[i] is the position of the ith car (in miles)
    speed[i] is the speed of the ith car (in miles per hour)

The destination is at position target miles.

A car can not pass another car ahead of it. 
It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. 
A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, 
then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
'''
type List[int] = List[int]

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, spd in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / spd 
            if stack and time <= stack[-1]:
                continue
            # only append faster times
            stack.append(time)
        return len(stack)

if __name__ == '__main__':
    target, position, speed = 10, [8,3,7,4,6,5], [4,4,4,4,4,4]
    print(Solution().carFleet(target, position, speed)) # 6
    
    target, position, speed = 10, [0,4,2], [2,1,3]
    print(Solution().carFleet(target, position, speed)) # 1
    
    target, position, speed = 10, [6,8], [3,2]
    print(Solution().carFleet(target, position, speed)) # 2
    
    target, position, speed = 10, [1,4], [3,2]
    print(Solution().carFleet(target, position, speed)) # 1
    
    target, position, speed = 10, [4,1,0,7], [2,2,1,1]
    print(Solution().carFleet(target, position, speed)) # 3