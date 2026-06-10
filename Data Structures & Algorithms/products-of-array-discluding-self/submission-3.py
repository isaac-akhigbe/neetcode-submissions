class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [1]

        # first walk forward to fetch the prefixes
        for num in nums:
            final.append(num * final[-1])
        final.pop()
        
        # walk backward to fetch the suffixes
        suffix = 1
        for i in reversed(range(len(nums) - 1)):
            suffix = (nums[i + 1] * suffix)
            final[i] *= suffix

        return final

        