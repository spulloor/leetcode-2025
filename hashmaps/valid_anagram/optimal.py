from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if s and t have same length
        if len(s) != len(t):
            return False

        # store the freq of chars in s
        char_count = defaultdict(int)
        for c in s:
            char_count[c] += 1

        # check if we have enough chars 
        for c in t:
            if c in char_count and char_count[c] > 0:
                char_count[c] -= 1
            else:
                return False

        return True