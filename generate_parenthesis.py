class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(s, ans, left, right):
            if left == right == 0:
                ans.append(s)
            else:
                if left > 0:
                    generate(s + '(', ans, left - 1, right)
                if right > left:
                    generate(s + ')', ans, left, right - 1)
        
        ans = []
        s = ''
        generate(s, ans, n, n)
        return ans
        
