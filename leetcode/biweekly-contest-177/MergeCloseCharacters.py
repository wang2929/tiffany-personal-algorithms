class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        s = list(s)
        while True:
            finished = True
            tracker = {}
            for i in range(len(s)):
                if s[i] not in tracker:
                    tracker[s[i]] = i
                elif (i - tracker[s[i]]) <= k:
                        del s[i]
                        finished = False
                        break
                else:
                    tracker[s[i]] = i
            if finished: break
        return ''.join(s)
        
test = Solution()
print(test.mergeCharacters('abca', 3)) # abc
print(test.mergeCharacters('aabca', 2)) # abca
print(test.mergeCharacters('yybyzybz', 2)) # ybzybz
print(test.mergeCharacters('hhh', 1)) # h
print(test.mergeCharacters('xsvtvv', 1)) # xsvtv