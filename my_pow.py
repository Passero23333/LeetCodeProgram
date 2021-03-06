class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
            
        power = 1
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            temp = self.myPow(x, n // 2)
            if n % 2:
                return temp * temp * x
            else:
                return temp * temp
