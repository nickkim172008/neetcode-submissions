class Solution: #hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i in range(len(nums)):
            if nums[i] in hashm:
                if nums[i]*2 == target:
                    return[hashm[nums[i]], i]
            else:
                hashm[nums[i]] = i
                difference = target - nums[i]
                if difference in hashm and hashm[difference] != hashm[nums[i]]:
                    return [hashm[difference],hashm[nums[i]]]
                
                






        
        