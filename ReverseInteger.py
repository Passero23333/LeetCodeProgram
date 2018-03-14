class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        num = []
        remain = abs(x)
        if x < 0:
            flag = -1
        else:
            flag = 1

        while (True):
            digit = remain % 10
            remain = remain // 10
            num.append(digit)
            if remain == 0:
                break

        res = 0
        for i in num:
            res *= 10
            res += i

        if res > 0x7FFFFFFF:
            return 0
        else:
            return res * flag

# test code
x = Solution()
test = 123
print(x.reverse(test))