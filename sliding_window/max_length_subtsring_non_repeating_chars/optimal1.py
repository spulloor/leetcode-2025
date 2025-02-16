class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        i = 0
        j = 0
        ht = set()
        max_length = 1
        found_duplicate = False

        while j < len(s):
            if s[j] in ht:
                max_length = max(max_length, j - i)
                while True:
                    if s[i] == s[j]:
                        i += 1
                        break

                    ht.remove(s[i])
                    i += 1

                found_duplicate = True
            else:
                ht.add(s[j])
                found_duplicate = False
            
            j += 1


        # if the last character is not present in the hashset, then we don't consider that 
        # for max_length calculation so we do it here
        return max(max_length, j - i) if not found_duplicate and j - 1 != 0 else max_length
            