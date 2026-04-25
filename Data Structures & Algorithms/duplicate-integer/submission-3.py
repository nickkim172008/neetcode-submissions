class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        remember = 0 
        for i in nums:
            if i == remember:
                return True 
                break
            remember = i
        return False
            
            

    
            