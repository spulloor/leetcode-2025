class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # base case if numRows == len(s) then return the string itself.
        if numRows == 1:
            return s

        res = ""

        for r in range(numRows):
            increment = (numRows - 1) * 2

            # loop through the string for n rows
            for i in range(r, len(s), increment):
                res += s[i]

                # to find out the middle chars
                if (r > 0 and r < numRows - 1) and (i + increment - (2 * r)) < len(s):
                    res += s[(i+ increment - (2 * r))]

        return res
