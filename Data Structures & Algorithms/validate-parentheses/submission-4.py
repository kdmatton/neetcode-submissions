class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                if len(stack) <= 0:
                    return False
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif s[i] == ")":
                if len(stack) <= 0:
                    return False
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif s[i] == "}":
                if len(stack) <= 0:
                    return False
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack) > 0:
            return False
        return True