class Solution:

    def encode(self, strs: List[str]) -> str:
        og = ""
        for word in strs:
            og = og +  word + "{}||7z34r"
        
        return og


    def decode(self, s: str) -> List[str]:
        new_list = []
        remember = 0
        for i in range(len(s)):
            if s[i:i+9] == "{}||7z34r":
                new_list.append(s[remember:i])
                remember = i + 9
        
        return new_list


