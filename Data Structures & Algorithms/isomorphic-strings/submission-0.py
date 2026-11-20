class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap={}
        if len(s)==len(t) and len(s)>0:
            for i in range(len(s)):
                if s[i] in hashmap:
                    if hashmap[s[i]]!=t[i]:
                        return False
                else:
                    if t[i] in hashmap.values():
                        return False
                    else:
                        hashmap[s[i]]=t[i]
            return True
        else:
            return True
                


        