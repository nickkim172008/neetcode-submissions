class Solution:
    def maxArea(self, height: List[int]) -> int:

        max = 0
        #loop through each starter
        for i in range(len(height)):

            #two pointer
            l = i
            r = len(height) - 1

            while l<r:
                area = (r - l)*min(height[r], height[l])

                if area>max:
                    max = area
                    
                if height[l] < height[r]:
                    l+=1
                elif height[r] < height[l]:
                    r-=1
                else:
                    break

        return max

            