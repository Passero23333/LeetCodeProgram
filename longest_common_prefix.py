class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        ans = ""
        
        # empty list or empty strings in the list
        if n == 0 or "" in strs:
            return ans
        
        min_str_len = len(min(strs, key=len))
        first_letter_set = set()
        for i in strs:
            first_letter_set.add(i[0])
        
        # no common prefix
        if len(first_letter_set) != 1:
            return ans
        # there is common prefix
        else:
            ans += first_letter_set.pop()
            latter_letter_set = set()
            for j in range(1, min_str_len):
                for i in strs:
                    latter_letter_set.add(i[j])
                if len(latter_letter_set) == 1:
                    ans += latter_letter_set.pop()
                    latter_letter_set.clear()
                else:
                    break
            return ans
      
