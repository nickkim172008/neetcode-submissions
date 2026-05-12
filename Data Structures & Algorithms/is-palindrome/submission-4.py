class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l<r:
            while s[l].isalnum() is False:
                l+=1
                if l == len(s):
                    return True

            while s[r].isalnum() is False:
                r-=1

            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False

        return True
                
         


        

        



