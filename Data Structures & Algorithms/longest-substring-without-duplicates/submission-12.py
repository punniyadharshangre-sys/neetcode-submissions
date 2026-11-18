class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        length=len(s)
        sub=set()
        if length>1:
            
            i,j=0,1
            sub.add(s[i])
            ans=1
            while j<length:
                if s[j] not in sub:
                    sub.add(s[j])
                    ans=max(ans,len(sub))
                else:
                    while s[j] in sub and i<j:
                        sub.remove(s[i])
                        i+=1
                sub.add(s[j])
                j+=1
            return ans
        else:
            return len(s)



        