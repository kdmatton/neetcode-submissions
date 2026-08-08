class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0 

        if len(t) < len(s):
            return False
        for right in range(len(t)):
            if left >= len(s):
                return True
            if s[left] == t[right]:
                left += 1
        if left >= len(s):
            return True 
        else:
            return False
            