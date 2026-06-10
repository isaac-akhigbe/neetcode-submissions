class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        # initialize i and j with 1
        pre = suf = 1
        final = [1] * nums_length

        for i in range(nums_length):
            final[i] *= pre
            pre *= nums[i]
            # reverse
            j = nums_length - i - 1
            final[j] *= suf
            suf *= nums[j]

        return final

