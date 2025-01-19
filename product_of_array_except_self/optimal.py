from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = len(nums)
        left_array = []
        right_array = [0] * s

        res = 1
        # generate left array
        for n in nums:
            left_array.append(res)
            res *= n

        res = 1
        # generate right array
        for n in nums[::-1]:
            right_array.append(res)
            res *= n

        # reverse the right array
        right_array = reversed(right_array)

        # multiply left and right array
        ans = []
        for x, y in zip(left_array, right_array):
            ans.append(x*y)

        return ans