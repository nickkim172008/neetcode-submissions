class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        #iterate through strs, sort
        for i in range(len(strs)):
            a = "".join(sorted(strs[i]))
                #key: sorted word value: [index,index]
            if a in hashmap:
                hashmap[a].append(i)
            else:
                hashmap[a] = [i]

        b = []

        for value in hashmap.values():
            group = []
            for index in value:
                group.append(strs[index])
            b.append(group)
            
        return b


                



        
        