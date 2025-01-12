class Solution:
    def jump(self, nums: List[int]) -> int:

        l, r, farthest = 0, 0, 0
        jumps = 0

        while r < len(nums) - 1:
            i = l
            while i <= r:
                farthest = max(farthest, nums[i] + i)
                i += 1

            l = r + 1
            r = farthest
            farthest = 0
            jumps += 1

        return jumps

            
            

        return cnt

        
