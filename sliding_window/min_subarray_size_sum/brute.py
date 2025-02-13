class Solution:
    @staticmethod
    def minSubArrayLen(target: int, nums) -> int:
        total = 0
        min_length = float('inf')
        j = 0

        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):

                total += nums[j]
                if total >= target:
                    if min_length == 0:
                        min_length = (j - i + 1)
                    else:
                        min_length = min(min_length, (j - i + 1))
                    break

        return min_length if min_length != float('inf') else 0
    
Solution.minSubArrayLen(7, [2,3,1,2,4,3])