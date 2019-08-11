class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits contains one number
        if len(digits) == 1:
            if digits[-1] == 9:
                digits[-1] = 0
                digits.insert(0, 1)
            else:
                digits[-1] += 1
            return digits
        # digits contains multiple number
        else:
            # the last digit is not 9, just add 1 to the last digit
            if digits[-1] != 9:
                digits[-1] += 1
                return digits
            # the last digit is 9
            else:
                n = len(digits)
                # the only 9 appears in the last digit
                if digits.index(9) == n - 1:
                    digits[-1] = 0
                    digits[-2] += 1
                    return digits
                # all digits are 9
                elif digits.count(9) == n:
                    for i in range(n):
                        digits[i] = 0
                    digits.insert(0, 1)
                    return digits
                # 9s appear in a consecutive manner
                elif digits.count(9) + digits.index(9) == n:
                    start = digits.index(9)
                    digits[start - 1] += 1
                    for i in range(start, n):
                        digits[i] = 0
                    return digits
                # 9s don't appear in a consecutive manner
                else:
                    # search for the index of non-none element in the reversed list
                    count = 0
                    digits.reverse()
                    for digit in digits:
                        if digit == 9:
                            count += 1
                        else:
                            break
                    digits.reverse()
                    start = n - count
                    digits[start - 1] += 1
                    for i in range(start, n):
                        digits[i] = 0
                    return digits
            
        # s = ''.join([str(digit) for digit in digits])
        # return list(str(int(s) + 1))
