class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #sorting using dictionary - key: number value: frequency
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        #sort by frequency,
        array = []
        for num, freq in hashmap.items():
            array.append([freq, num])

        array.sort()

        #loop to return valess
        final_array = []
        for i in range(k):
            final_array.append(array[len(array) - 1 - i][1])
        
        return final_array
