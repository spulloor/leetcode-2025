import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 0
        minDiff = float('inf')

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == target:
                    return s
                
                if s < target:
                    j += 1
                else:
                    k -= 1

                # this part makes it unique from 3 sum problem
                # closest means the least difference between the sum and the target
                diff = abs(s - target)
                if diff < minDiff:
                    minDiff = diff
                    closest = s

        return closest