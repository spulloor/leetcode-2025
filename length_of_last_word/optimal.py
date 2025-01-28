import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        return len(re.split('\s+', s)[-1])