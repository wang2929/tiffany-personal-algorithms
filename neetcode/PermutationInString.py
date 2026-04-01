'''
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise. 
That means if a permutation of s1 exists as a substring of s2, then return true.
Both strings only contain lowercase letters.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for char in s1:
            d[char] = d.get(char, 0) + 1
        # two pointer
        i, j = 0, len(s1) - 1
        # calculate matching chars
        m = {}
        for k in range(i, j+1):
            if d.get(s2[k], 0) > 0:
                m[s2[k]] += 1
        if sum(m.values()) == len(s1): return True
        while j < len(s2):
            # if s2[i], s2[j] in s1, subtract from match
            if s2[i] in d:
                m[s2[i]] -= 1
            if s2[j] in d:
                m[s2[j]] -= 1
            # shift to the right
            i += 1
            j += 1
            # calculate new match count
            if m.get(s2[k], 0) > 0:
                d[s2[i]] -= 1
            if d.get(s2[k], 0) > 0:
                d[s2[j]] -= 1
            # compare matching chars to length of s1
            if sum(d.values()) == 0:
                return True
        return False

if __name__ == '__main__':
    print(Solution().checkInclusion("hello", "ooolleoooleh"))
    print(Solution().checkInclusion("mart", "karmta")) # True
    print(Solution().checkInclusion("ky", "ainwkckifykxlribaypk")) # True