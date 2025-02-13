class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        min_length = float('inf')
        j = 0
        i = 0

        while j < len(nums):

            total += nums[j]
            j += 1
            while total >= target:
                total -= nums[i]
                min_length = min(min_length, (j - i))

                i += 1



        return min_length if min_length != float('inf') else 0