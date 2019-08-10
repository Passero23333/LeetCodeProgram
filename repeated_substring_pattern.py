class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return False
        elif n == 1:
            return False
        else:
            for i in range(1, n):
                sub_str = s[0:i]
                if s == sub_str * int(n / len(sub_str)):
                    return True
            return False
