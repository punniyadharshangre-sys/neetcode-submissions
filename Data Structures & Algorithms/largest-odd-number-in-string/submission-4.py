class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        if float(num)%2>0:
            return num
        ans=''
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2>0:
                return num[:i+1]
        

        return ''

