class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}

        for char in s:
            if char in hm1:
                hm1[char] += 1
            else:
                hm1[char] = 0

        for char in t:
            if char in hm2:
                hm2[char] += 1
            else:
                hm2[char] = 0

        if hm1 == hm2:
            return True
        else:
            return False
        