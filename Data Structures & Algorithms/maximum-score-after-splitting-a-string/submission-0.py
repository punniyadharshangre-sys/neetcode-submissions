class Solution:
    def helper(self,left,right):
        zeros=len([z for z in left if z=='0'])
        ones=len([o for o in right if o=='1'])
        return zeros+ones

    def maxScore(self, s: str) -> int:
        s_lis=list(s)
        i=0
        max_num=0
        while i<len(s_lis)-1:
            left=s_lis[:i+1]
            right=s_lis[i+1:]
            max_num=max(max_num,self.helper(left,right))
            i+=1
        return max_num
        