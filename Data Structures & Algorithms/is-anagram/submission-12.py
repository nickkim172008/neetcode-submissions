class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in s_hash:
                    s_hash[s[i]] += 1 
                else:
                    s_hash[s[i]] = 1 

                if t[i] in t_hash:
                    t_hash[t[i]] += 1
                else: 
                    t_hash[t[i]] = 1 
            
            if s_hash == t_hash:
                return True
            else:
                return False
        else:
            return False