class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
       
        # check if length is exactly 3, and return if the sum is 0
        if length == 3 and sum(nums) == 0:
            return [nums]

        result = []
        for i, num in enumerate(nums): 
            if num > 0:
                break
            # Handle first duplicate
            if i > 0 and num == nums[i - 1]:
                continue

            j, k = i + 1, length - 1
            # nums=[-4, -1, -1, 0, 1, 2]  
            # j = 2, 3, 4 k = 5,3, 2
            while j < k:
                iplusj = nums[j] + nums[k]

                # if nums[j] + nums[k] = - nums[i], it matches
                if iplusj == -num:
                    #[-2, 0, 2]
                    result.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                # Adjust j and k respectively
                if iplusj < -num:
                    j += 1
                if iplusj > -num:
                    k -= 1
        return result


                
        