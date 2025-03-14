class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        i = 0
        mapping_s_t = {}
        mapping_t_s = {}

        while i < len(s):
            if s[i] in mapping_s_t:
                if mapping_s_t[s[i]] != t[i]:
                    return False
            elif t[i] in mapping_t_s:
                if mapping_t_s[t[i]] != s[i]:
                    return False
            else:
                mapping_s_t[s[i]] = t[i]
                mapping_t_s[t[i]] = s[i]

            i += 1

        return True