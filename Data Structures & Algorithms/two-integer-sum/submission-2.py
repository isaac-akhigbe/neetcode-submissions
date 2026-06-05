class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_hash = {num: index for index, num in enumerate(nums)}
        for index, num in enumerate(nums):
            diff = target - num
            diff = list_hash.get(diff, -1)
            if index == diff: 
                continue
            if diff != -1:
                if index < diff:
                    return [index, diff]
                else:
                    return [diff, index]
        