class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbers_seen = {}

        for i, v in enumerate(nums):
           numbers_seen[v] = i 

        for i, v in enumerate(nums):

            diff = target - v

            diff_index = numbers_seen.get(diff)

            if diff_index and i != diff_index:
                return [i, diff_index]

        return []

