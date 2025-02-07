class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = float('-inf')
        i = 0
        j = len(height) - 1

        while i < len(height) and j >= 0:

            width = j - i
            h = min(height[i], height[j])
            area = max(width * h, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area