class Solution:
    def maxArea(self, height: List[int]) -> int:

        max = 0
        l = 0
        r = len(height) - 1

        while l<r:
            area = (r - l)*min(height[r], height[l])

            if area>max:
                max = area
                
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1


        return max

            