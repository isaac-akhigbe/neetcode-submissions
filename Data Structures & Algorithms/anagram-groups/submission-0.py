class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_freq = {}
        for word in strs:
            freq = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                freq[index] += 1
            hash_freq[tuple(freq)] = hash_freq.get(tuple(freq), [])
            hash_freq[tuple(freq)].append(word)

        return list(hash_freq.values())          
            
