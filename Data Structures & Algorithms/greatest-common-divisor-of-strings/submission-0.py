class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1+str2!=str2+str1:
            return ''
        len1=len(str1)
        len2=len(str2)
        j=len2
        
        while j>=0:
            if len1%j==0 and len2%j==0:
                return str2[:j]
            j-=1
        
        

        
        