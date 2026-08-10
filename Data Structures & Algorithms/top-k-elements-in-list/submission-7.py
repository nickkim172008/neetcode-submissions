class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #key: num
        #value: freq
        #loop thorugh it, then take it away from hm after, 

        hm = {}

        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        arr = []
        for i in range(k):
            greatest_freq = 0
            greatest_number = 0
            for number, freq in hm.items():
                if freq > greatest_freq:
                    greatest_freq = freq
                    greatest_number = number
                
            del hm[greatest_number]
            arr.append(greatest_number)
        
        return(arr)



            
