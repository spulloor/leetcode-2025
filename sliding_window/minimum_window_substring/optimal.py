class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t or len(s) < len(t):
            return ""

        if s == t:
            return s

        char_freq = {}
        substring_char_freq = {}
        need = len(t)
        have = 0

        i = 0
        j = 0
        fs = ""
        ml = float('inf')

        # add all the char freq to the dict
        for c in t:
            char_freq[c] = char_freq.get(c, 0) + 1

        while j < len(s):

            c = s[j]

            # add the count of c to the substring dictionary
            substring_char_freq[c] = substring_char_freq.get(c, 0) + 1

            if c in char_freq and char_freq[c] >= substring_char_freq[c]:
                have += 1

            # we found the required substring
            while have == need:

                final_substring = s[i:j+1]
                l = len(final_substring)

                # chekc if it has min length
                if l < ml:
                    ml = l
                    fs = final_substring

                # remove the ith char from out window
                c = s[i]
                i += 1
                substring_char_freq[c] -= 1
                if c in char_freq and substring_char_freq[c] < char_freq[c]:
                    have -= 1

            j += 1

        
        return fs