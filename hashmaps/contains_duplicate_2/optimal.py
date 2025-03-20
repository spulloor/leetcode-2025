class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_numbers = {}

        for j, n in enumerate(nums):
            if n in seen_numbers:
                i = seen_numbers[n]

                if abs(i - j) <= k:
                    return True
                else:
                    seen_numbers[n] = j
            else:
                seen_numbers[n] = j

        return False
                