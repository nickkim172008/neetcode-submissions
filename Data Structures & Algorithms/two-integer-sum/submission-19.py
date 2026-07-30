class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hm:
                return([hm[diff], index])
        
            hm[value] = index