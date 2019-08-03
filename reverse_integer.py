class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        if x == 0:
            return 0
        else:
            new_x = sign * int(str(abs(x)).strip('0')[::-1])
            if new_x  < pow(-2,31) or new_x > pow(2,31) - 1:
                return 0
            else:
                return new_x

# test code
x = Solution()
test = 123
print(x.reverse(test))
