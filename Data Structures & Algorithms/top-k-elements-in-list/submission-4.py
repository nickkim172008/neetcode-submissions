class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #iterate and add to dictionary. key: number, value: frequency
        #iterate through dictionary, if highest add

        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary:
                dictionary[nums[i]]+=1
            else:
                dictionary[nums[i]] = 1

        output = []
        for i in range(k):
            remember = -9999999999
            for _ in dictionary:
                if dictionary[_]>remember and _ not in output:
                    remember = dictionary[_]
                    key = _
            output.append(key)
        
        return output




            
        