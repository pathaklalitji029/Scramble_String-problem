class Solution(object):
    def isScramble(self, s1, s2):
        memo = {}
        
        def solve(a, b):
            if a == b:
                return True
            
            if (a, b) in memo:
                return memo[(a, b)]
            
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False
            
            n = len(a)
            for i in range(1, n):
                # no swap
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                
                # swap
                if solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True
            
            memo[(a, b)] = False
            return False
        
        return solve(s1, s2)


s1="great"
s2="rgeat"

obj=Solution()
print(obj.isScramble(s1,s2))
