class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_hashset = set(nums)

        longest = 0
        for num in nums:
            length = 1
            if (num-1) in nums_hashset:
                continue

            while True:
                if (num + 1) in nums_hashset:
                    length +=1
                    num +=1
                else:
                    break
                


            if length>longest:
                longest = length

        return longest

        

            

            

        