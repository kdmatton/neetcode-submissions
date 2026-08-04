class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}
        if len(s) != len(t):
            return False
            
        for i in range(len(s)):
            if s[i] not in charMap:
                charMap[s[i]] = 1
            else:
                charMap[s[i]] += 1
            if t[i] not in charMap:
                charMap[t[i]] = -1
            else:
                charMap[t[i]] -= 1
        
        for key in charMap:
            if charMap[key] != 0:
                return False

        return True