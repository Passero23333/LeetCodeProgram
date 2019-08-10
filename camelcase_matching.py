class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        
        def match(q, p):
            i = 0
            j = 0
            while i < len(q) and j < len(p):
                if q[i] == p[j]:
                    i += 1
                    j += 1
                elif q[i].islower():
                    i += 1
                else:
                    return False
            return q[i:].lower() == q[i:] and j == len(p)
        
        for query in queries:
            if match(query, pattern):
                ans.append(True)
            else:
                ans.append(False)
                    
        return ans
                
        
