class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {} #key: sorted version value: array of words
        for stri in strs:
            new = "".join(sorted(stri))
            if new in hm:
                hm[new].append(stri)
            else:
                hm[new] = [stri]
        
        final_arr = []
        for key, value in hm.items():
            final_arr.append(value)

        return final_arr
