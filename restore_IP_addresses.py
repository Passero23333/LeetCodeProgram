class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def partition(s,index,res):
            nonlocal ans
            # incorrect
            if len(res) > 4:
                return
            # there are already 4 parts
            if len(res) == 4 :
                if index==len(s):
                    if res not in ans:
                        ans.append(res)
                return
            # still needs partition
            for i in range(index,min(index+3,len(s))):
                if int(s[index:i+1]) < 256 :
                    if int(s[index:i+1]) > 0 and s[index]=='0':
                        continue
                    if int(s[index:i+1])==0 and len(s[index:i+1])>1:
                        continue                        
                    partition(s,i+1, res + [s[index:i+1]] )
        partition(s,0,[])
        return [".".join(i) for i in ans]   
