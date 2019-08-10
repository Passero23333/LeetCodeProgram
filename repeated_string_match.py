class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if set(B).issubset(A) == False:
            return -1
        
        max = int(10000 / len(A)) + 1   
        for i in range(1, max):
            new_A = A * i
            if B in new_A:
                return i
        return -1
        
