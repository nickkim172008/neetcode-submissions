class Solution:
    def trap(self, height: List[int]) -> int:

        prefix_max = []
        sufix_max = []

        max = 0
        for i in range(len(height)):
            if height[i]>max:
                max = height[i]
            
            prefix_max.append(max)
        
        max_2 = 0
        for i in range(len(height)-1,-1,-1):
            if height[i]>max_2:
                max_2 = height[i]
            
            sufix_max.append(max_2)

        temp_area = 0
        area = 0
        for i in range(len(height)):

            area_column = min(prefix_max[i],sufix_max[len(height) - 1 -i]) - height[i]

            if area_column>0:
                temp_area += area_column
            elif area_column == 0:
                area+=temp_area
                temp_area = 0
            
        return area
            



            






