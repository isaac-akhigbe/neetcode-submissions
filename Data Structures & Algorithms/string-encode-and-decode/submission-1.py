class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            length = str(len(word))
            per_string = length + '&' + word
            encoded_string += per_string
        return encoded_string



    def decode(self, s: str) -> List[str]:
        decoded_string = []
        while True:
            sep = s.find('&')
            if sep == -1:
                break
            length = int(s[:sep]) + 1
            word = s[sep + 1: sep + length]
            s = s[sep + length:]
            decoded_string.append(word)
        return decoded_string
        
