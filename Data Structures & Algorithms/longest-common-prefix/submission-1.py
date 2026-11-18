class Solution:

    def logic(self,min_len,firts_elem,strs):
        for i in range(len(strs[1:])):
            if not strs[i+1][:min_len]==firts_elem[:min_len]:
                break
            if i==len(strs[1:])-1:
                return firts_elem[:min_len]
        return None



    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)>1:
            strs=sorted(strs)
            min_len=len(strs[0])
            firts_elem=strs[0]
            ans=self.logic(min_len,firts_elem,strs)
            print(ans)
            if ans:
                return ans
            min_len-=1
            firts_elem=firts_elem[:min_len]
            print(firts_elem)
            while min_len>=1:
                ans=self.logic(min_len,firts_elem,strs)
                if ans:
                    return ans
                min_len-=1
                firts_elem=firts_elem[:min_len]
            return ''
        else:
            return strs[0]
            
                    

        