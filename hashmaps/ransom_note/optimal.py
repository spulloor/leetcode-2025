from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        char_counts = defaultdict(int)

        # store the frequency of chars in magazine
        for c in magazine:
            char_counts[c] += 1

        # check if the frequency if not zero 
        # if it is then we don't have enough chars of ransom note in magazine
        for c in ransomNote:
            if char_counts[c] == 0:
                return False
            
            char_counts[c] -= 1

        return True

        