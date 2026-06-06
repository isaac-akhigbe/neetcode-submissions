class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        for c in t:
            freq[c] = freq.get(c, 0) - 1
        for item in freq.values():
            if item != 0:
                return False
        return True

        