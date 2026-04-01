'''
Given two strings s and t, return the shortest substring of s 
such that every character in t, including duplicates, is present 
in the substring. If such a substring does not exist, 
return an empty string "".
You may assume that the correct output is always unique.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if len(s) == 1:
            return t if s == t else ""
        if len(t) == 1:
            return t if t in s else ""
        substring = ""
        freq_map = {}
        for char in t:
            freq_map[char] = freq_map.get(char, 0) + 1
        # step 1: find the leftmost substring with all the chars of t
        i, j = 0, 0
        s_count = {}
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        while (j+1) < len(s):
            j += 1
            s_count[s[j]] = s_count.get(s[j], 0) + 1
            cnt = 0
            for key, val in freq_map.items():
                if key in s_count and s_count[key] >= val:
                    cnt += 1
            if cnt == len(freq_map):
                # shrink the window as much as possible to find the substring
                while i < j:
                    s_count[s[i]] -= 1
                    i += 1
                    tmp = 0
                    for key, val in freq_map.items():
                        if key in s_count and s_count[key] >= val:
                            tmp += 1
                    if tmp != len(freq_map):
                        i -= 1
                        s_count[s[i]] += 1
                        substring = s[i:j+1]
                        break
                break
        if cnt < len(freq_map): 
            return ""
        substring = s[i: j+1]
        # step 2: shift window to the right until find another valid substring
        while (j + 1) < len(s):
            s_count[s[i]] = s_count.get(s[i], 0) - 1
            i += 1
            j += 1
            s_count[s[j]] = s_count.get(s[j], 0) + 1
            cnt = 0
            for key, val in freq_map.items():
                if key in s_count and s_count[key] >= val:
                    cnt += 1
            if cnt == len(freq_map):
                # shrink the window as much as possible to find the substring
                while i < j:
                    s_count[s[i]] -= 1
                    i += 1
                    cnt = 0
                    for key, val in freq_map.items():
                        if key in s_count and s_count[key] >= val:
                            cnt += 1
                    if cnt != len(freq_map):
                        i -= 1
                        s_count[s[i]] += 1
                        substring = s[i:j+1]
                        break
        return substring
            
if __name__ == "__main__":
    print(Solution().minWindow("babb", "baba"))
    print(Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))
    print(Solution().minWindow("OUZODYXAZV", "XYZ")) #YXAZ
    print(Solution().minWindow("abc", "b")) # b
    print(Solution().minWindow("b", "b")) # b
    print(Solution().minWindow("ab", "a")) # "b"
    print(Solution().minWindow("xyz", "xyz"))