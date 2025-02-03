class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0

        for s1, s2 in zip(s, s[1:]):
            if roman[s1] >= roman[s2]:
                num += roman[s1]
            else:
                num -= roman[s1]

        return num + roman[s[-1]]
