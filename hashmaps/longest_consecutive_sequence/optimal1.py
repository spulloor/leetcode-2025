class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        longest = 0
        s = set(nums)
        seenNums = set()

        # loop through the nums
        for n in nums:

            # check if n - 1 is there in the set
            if not n - 1 in s and n not in seenNums:

                # don't loop through duplicate elements
                seenNums.add(n)

                # if it is not there then build out a sequence
                length = 0

                while n + length in s:
                    length += 1

                # get the final length for this particular seq
                longest = max(longest, length)

        return longest

        

                