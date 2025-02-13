class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # sort the array for two sum's two pointer solution to work.
        nums.sort()

        for i in range(len(nums) - 2):
            # if current no is same as the previous no. then we need to skip it
            # we will get the same result.
            if i > 0 and nums[i] == nums[i - 1]: 
                continue


            j = i + 1
            k = len(nums) - 1

            while j < k:
                target = nums[i] +  nums[j] + nums[k]

                if target < 0:
                    j += 1
                elif target > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    # skip the duplicates
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
      

        return res
