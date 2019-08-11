class Solution:
    def validIPAddress(self, IP: str) -> str:
        ans = ['IPv4', 'IPv6', 'Neither']
        # if IP.find('.') != -1:
        if '.' in IP:
            IP = IP.split('.')
            if len(IP) != 4:                            
                return ans[2]        
            for ip in IP:    
                if len(ip) == 0 or len(ip) > 3:           
                    return ans[2]
                if len(ip) > 1 and ip.startswith('0'):          
                    return ans[2]
                for i in ip:
                    if i not in '0123456789':           
                        return ans[2]
                if int(ip) < 0 or int(ip) > 255:          
                    return ans[2]
            return ans[0]
        else:
            IP = IP.split(':')
            if len(IP) != 8:                            
                return ans[2]
            for ip in IP:
                if len(ip)  == 0:                        
                    return ans[2]
                if len(ip) > 4:                          
                    return ans[2]
                for i in ip:
                    if i not in '0123456789abcdefABCDEF':       
                        return ans[2]
            return ans[1]
