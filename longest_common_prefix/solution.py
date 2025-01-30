class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find out the string with the minimum length
        min_length = float('inf')

        for i in strs:

            if len(i) < min_length:
                min_length = len(i)


        # loop through the strs list atmost the minimum length
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1

        return strs[0][:i]
