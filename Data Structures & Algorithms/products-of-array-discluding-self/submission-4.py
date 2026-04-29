class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        new_list = [0] * len(nums)
        #prefix traverse l -> r
        start = 1
        for i in range(len(new_list)):
            new_list[i] = start 
            start *= nums[i]

        #postfix     
        end = 1
        for i in range(len(new_list)-1, -1, -1):
            new_list[i] *= end 
            end *= nums[i]

        return new_list




        