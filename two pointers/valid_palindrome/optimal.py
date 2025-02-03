import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric chars
        s = re.sub(r'[^A-Za-z0-9]+', '', s)

        # convert s to uppercase
        s = s.upper()

        # check the reverse of the string with itself
        return s == s[::-1]