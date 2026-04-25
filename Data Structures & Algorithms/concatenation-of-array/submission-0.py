class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        a=0
        while a<2:
            for i in range(len(nums)):
                ans.append(nums[i])
            a+=1

        return ans
        

        