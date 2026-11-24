class Solution:
    def helper(self,curr,prev):
        if self.prev_hash.get(prev,None) == curr:
            return -self.hash_romans[curr]
        else:
            return self.hash_romans[curr]
    def romanToInt(self, s: str) -> int:
        self.hash_romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        self.prev_hash={'V':'I','X':'I','L':'X','C':'X','D':'C','M':'C'}
        prev=None
        ans=0
        for i in range(len(s)-1,-1,-1):
            if prev:
                temp=self.helper(s[i],prev)
                ans+=temp 
            else:
                ans+=self.hash_romans[s[i]]
            prev=s[i]
        return ans
            




