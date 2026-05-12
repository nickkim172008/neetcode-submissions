class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = ""

        for alphanumeric in s:
            if alphanumeric.isalnum():
                clean_s += alphanumeric.lower()

        start = 0
        end = len(clean_s) - 1

        while start <= end:
            if clean_s[start] == clean_s[end]:
                start+=1
                end-=1
            else:
                return False

        return True

        

        



