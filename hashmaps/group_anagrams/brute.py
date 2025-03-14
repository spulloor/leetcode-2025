class Solution:

    def checkAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for c in set(s):
            if s.count(c) != t.count(c):
                return False

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        string_seen_before = set()
        for i in range(len(strs)):

            if strs[i] in string_seen_before:
                continue

            inner = [strs[i]]
            for j in range(i + 1, len(strs)):
                
                if self.checkAnagram(strs[i], strs[j]):
                    string_seen_before.add(strs[j])
                    inner.append(strs[j])

            res.append(inner)

        return res