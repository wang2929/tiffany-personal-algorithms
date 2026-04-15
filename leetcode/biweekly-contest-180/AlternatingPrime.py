'''
You are given an integer array nums.

An array is considered alternating prime if:
    Elements at even indices (0-based) are prime numbers.
    Elements at odd indices are non-prime numbers.

In one operation, you may increment any element by 1.
Return the minimum number of operations required to transform nums into an alternating prime array.
A prime number is a natural number greater than 1 with only two factors, 1 and itself.
©leetcode
'''

class Solution:
    def isPrime(self, num: int) -> list[int]:
        if num == 1:
            return False # exception: 1 is not prime
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    def nearestPrime(self, num:int) -> int:
        # ideally want the nearest one, so should work backwards from the number in either direction
        upper_prime = num*100
        for i in range(num+1, (num+1)**2):
            if self.isPrime(i):
                upper_prime = i
                break
        return upper_prime - num
    def minOperations(self, nums: list[int]) -> int:
        ops = 0
        for i in range(len(nums)):
            is_prime = self.isPrime(nums[i])
            if is_prime and i&1 == 1:
                # most primes aren't next to each other because even numbers, can find a non-prime in one op
                if nums[i] != 2:
                    ops += 1
                else:
                    ops += 2
            elif not is_prime and i&1 == 0:
                # harder to find a nearest prime number
                ops += self.nearestPrime(nums[i])
        return ops
    
if __name__ == '__main__':
    print(Solution().isPrime(1)) # False
    print(Solution().isPrime(2)) # True
    print(Solution().isPrime(3)) # True
    print(Solution().isPrime(4)) # False
    print(Solution().minOperations([8, 12])) # 3
    print(Solution().minOperations([1, 2, 3, 4])) # 3
    print(Solution().minOperations([5, 6, 7, 8])) # 0
    print(Solution().minOperations([4, 4])) # 1
    