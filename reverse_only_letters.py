class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        n = len(S)
        s = []
        nonletter = []
        nonletter_index = []
        for i in range(n):
            current_letter = S[i]
            if S[i].isalpha():
                s.append(S[i])
            else:
                nonletter.append(S[i])
                nonletter_index.append(i)
        
        s = s[::-1]
        
        for i in range(len(nonletter)):
            s.insert(nonletter_index[i], nonletter[i])
            
        return ''.join(s)
