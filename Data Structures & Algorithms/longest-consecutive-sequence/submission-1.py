class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        items = set(nums)
        largest = 0
        for num in nums:
            if (num - 1) in items:
                continue
            else:
                longest = 1
                while (num + 1) in items:
                    longest += 1
                    num += 1
                if longest > largest:
                    largest = longest
        return largest



        