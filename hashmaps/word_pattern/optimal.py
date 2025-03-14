import re

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        letter_in_s = {}
        word_2_letter = {}

        words = re.split(r'\s+', s)

        if len(words) != len(pattern):
            return False

        for i in  range(len(pattern)):

            if pattern[i] in letter_in_s:
                if letter_in_s[pattern[i]] != words[i]:
                    return False
            elif words[i] in word_2_letter:
                if word_2_letter[words[i]] != pattern[i]:
                    return False
            else:
                letter_in_s[pattern[i]] = words[i]
                word_2_letter[words[i]] = pattern[i]

        return True
