class Solution:
    def isValid(self, s: str) -> bool:
        hash_map={')':'(','}':'{',']':'['}
        s_l=list(s)
        stack=[]
        for c in s_l:
            if c not in hash_map:
                stack.append(c)
            else:
                if stack:
                    last_c=stack.pop()
                    if hash_map[c]!=last_c:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
        