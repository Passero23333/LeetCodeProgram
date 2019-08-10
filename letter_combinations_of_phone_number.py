from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        if n == 0:
            return ans
        elif n == 1:
            for i in letters[int(digits) - 2]:
                ans.append(i)
            return ans
        else:
            ans = ["".join(i) for i in product(*[letters[int(i) - 2] for i in digits])]
            return ans
