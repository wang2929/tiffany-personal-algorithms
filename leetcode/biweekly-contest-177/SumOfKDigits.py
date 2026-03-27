class Solution: 
    def BFS(self, l, r, limit):
        if limit == 1:
            return list(range(l, r+1))
        str_name = [str(i) for i in range(l, r+1)]
        qu = []
        discovered = {}
        for elem in str_name:
            qu.append(elem)
            discovered[elem] = True
        ret = []
        for path in qu:
            if len(path) > limit:
                # do stuff to format
                return ret
            for next_step in str_name:
                new_path = path + next_step
                if new_path not in discovered:
                    qu.append(new_path)
                    discovered[new_path] = True
                    if len(new_path) == limit:
                        ret.append(int(new_path))
    
    def DFS(self, l, r, limit):
        if limit == 1:
            return list(range(l, r+1))
    
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        mod = 10**9 + 7
        # this is like a DFS for building the numbers
        numbers_list = self.BFS(l, r, k)
        sum = 0
        for elem in numbers_list:
            sum = (sum + elem) % mod
        return sum

# memory limit :/
test = Solution()
print(test.sumOfNumbers(0, 6, 1)) # expect 21 = 0 + 1 + 2 + 3 + 4 + 5 + 6
# print(test.sumOfNumbers(5, 5, 10))
# print(test.sumOfNumbers(1, 2, 2))
# print(test.sumOfNumbers(0, 1, 3))
# print(test.sumOfNumbers(3, 2, 3))