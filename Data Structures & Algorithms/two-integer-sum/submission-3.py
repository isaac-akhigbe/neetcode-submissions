class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_i, i in enumerate(nums):
            for index_j, j in enumerate(nums):
                if index_i == index_j:
                    continue
                if i + j == target:
                    if index_i < index_j:
                        return [index_i, index_j]
                    else:
                        return [index_j, index_i]
        