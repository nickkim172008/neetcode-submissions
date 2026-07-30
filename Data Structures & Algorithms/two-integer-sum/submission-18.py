class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for index, value in enumerate(nums):
            hm[value] = index  

        for index, value in enumerate(nums):
            find = target - value
            if find in hm and index != hm[find]:
                return([index, hm[find]])
        
            
    
