class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        n = len(s)
        
        def backtrack(start, parts, path):
            # If 4 parts are formed
            if parts == 4:
                # Check if string is fully consumed
                if start == n:
                    res.append(".".join(path))
                return
            
            # Try segments of length 1 to 3
            for length in range(1, 4):
                if start + length > n:
                    break
                
                segment = s[start:start+length]
                
                # Leading zero restriction
                if segment[0] == '0' and length > 1:
                    continue
                
                # Range restriction
                if int(segment) > 255:
                    continue
                
                path.append(segment)
                backtrack(start + length, parts + 1, path)
                path.pop()
        
        backtrack(0, 0, [])
        return res
