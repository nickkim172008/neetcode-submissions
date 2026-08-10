class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            looking_for = target - nums[i]
            if looking_for in hm:
                return([hm[looking_for], i])

            hm[nums[i]] = i