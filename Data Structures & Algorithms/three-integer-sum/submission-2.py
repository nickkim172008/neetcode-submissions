class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort, and choose an anchor (no duplicates)
        new = []
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            #now simple two pointer for each anchor
            l = i + 1
            r = len(nums) - 1
            while l<r:
                total = nums[l] + nums[r] + nums[i]

                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    new.append([nums[l], nums[r], nums[i]])
                    l+=1
                    r-=1
                    #make sure no duplicates for Left side when checking for more inside same index
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        
        #right side duplicates dont matter, as if making sure no dup on left side, then dup on right side wont cahnge anytihg
        return new
