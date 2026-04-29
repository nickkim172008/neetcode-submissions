class Solution:

    def encode(self, strs: List[str]) -> str:
        og = ""
        for word in strs:
            og = og + str(len(word)) + "?" +  word
        
        return og


    def decode(self, s: str) -> List[str]:
        new_list = []
        a = 0
        while a<len(s) - 1:
            z_1 = a
            z_2 = a + 1
            while True:
                if s[z_2] != "?":
                    z_2+=1
                else:
                    break
            length_word = int(s[z_1:z_2])
            new_list.append(s[z_2+1:z_2 + length_word + 1])

            a+= length_word + z_2 - z_1 + 1
        return new_list