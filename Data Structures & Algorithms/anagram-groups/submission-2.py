class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #key: arrayof 26, #value array of words

        hashmap = {}

        for i in range(len(strs)):
            count = [0] * 26
            for _ in range(len(strs[i])):
                count[ord(strs[i][_]) - 97] += 1
            
            key = tuple(count)
            if key in hashmap:
                hashmap[key].append(strs[i])
            else:
                hashmap[key] = [strs[i]]
        
        return list(hashmap.values())


