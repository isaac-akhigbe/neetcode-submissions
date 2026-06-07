class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        num_buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            num_buckets[count].append(num)

        result = []
        for bucket in reversed(num_buckets):
            if len(result) == k:
                break
            if not bucket:
                continue
            result.extend(bucket)
        return result


            
            