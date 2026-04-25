class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            a = target - nums[i]
            for _ in range(len(nums)):
                if nums[_] == a and _!=i:
                    a = [i, _]
                    return a    