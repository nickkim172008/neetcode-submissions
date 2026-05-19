class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        nums.sort()
        end = []
        for i in range(len(nums)):
        
            l = i+1
            r = len(nums) - 1

            if i>0 and nums[i - 1] == nums[i]:
                continue

            while l<r:
                
                target = nums[l] + nums[r] + nums[i]
                
                if target>0:
                    r-=1
                elif target<0:
                    l+=1
                else:
                    end.append([nums[l], nums[r], nums[i]])
                    l+=1

                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        
        return end

        