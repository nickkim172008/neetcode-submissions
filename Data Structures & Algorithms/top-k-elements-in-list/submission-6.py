class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap: key - num, value - freq
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        
        #bucket sort --> arrays within an array: index -> frequency
        buck_sort = []
        for i in range(len(nums)+1):
            buck_sort.append([])

        for num, freq in hm.items():
            buck_sort[freq].append(num)

        #make final array, by tranversing backwards
        final_array = []
       
        for i in range(len(nums), 0, -1):
            for _ in buck_sort[i]:
                final_array.append(_)
                if len(final_array) == k:
                     return final_array

        
       