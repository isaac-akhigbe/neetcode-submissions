class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums) 

        # first walk forward to fetch the prefixes
        pre_output = [1]
        for index, prefix in enumerate(nums):
            pre_output.append(prefix * pre_output[-1])
        
        # walk backward to fetch the suffixes
        suf_output = [None] * nums_length
        suf_output[nums_length - 1] = 1
        for i in reversed(range(nums_length - 1)):
            suf_output[i] = (nums[i + 1] * suf_output[i + 1])

        # Accumulate result
        final = []
        for i in range(nums_length):
            final.append(pre_output[i] * suf_output[i])
        return final




        