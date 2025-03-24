class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        seq = []

        for i in range(0, len(nums)):
            # add the number to the seq
            seq.append(nums[i])

            if len(nums) - 1 == i or nums[i] + 1 != nums[i + 1]:

                if len(seq) == 1:
                    res.append(f'{seq[0]}')
                else:
                    res.append(f'{seq[0]}->{seq[-1]}')

                # because this breaks the current seq
                seq = []

        return res