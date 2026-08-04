class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key: [array O(26)] value: all words w this

        hm = {}
        for stri in strs:
            arr = [0] * 26
            for let in stri:
                arr[ord(let) - 97]+=1
            tup = tuple(arr)
            if tup in hm:
                hm[tup].append(stri)
            else:
                hm[tup] = [stri]

        final = []
        for key, value in hm.items():
            final.append(value)
        
        return final
            

