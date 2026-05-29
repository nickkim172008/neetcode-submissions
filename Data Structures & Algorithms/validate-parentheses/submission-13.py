class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False
        
        stac = []

        for i in range(len(s)):
            if s[i] in "({[":
                stac.append(s[i])
            
            else:

                if len(stac)>0 and ((stac[-1] == "[" and s[i] == "]") or (stac[-1] == "{" and s[i] == "}") or (stac[-1] == "(" and s[i] == ")")):
                    stac.pop() 
                else:
                    return False

        
        if stac:
            return False
        else:
            return True

        
             
        






                
        