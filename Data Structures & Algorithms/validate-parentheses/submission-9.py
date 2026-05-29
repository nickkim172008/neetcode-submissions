class Solution:
    def isValid(self, s: str) -> bool:

        hm = {")":"(", "]": "[", "}":"{"}
        stack = []
        for i in range(len(s)):

            if s[i] in hm:
                if len(stack)>0 and hm[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(s[i])

        if stack:
            return False
        else:
            return True

            