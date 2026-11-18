class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_filter=[c for c in s.split() if re.search(r'\w',c)]
        hash_map={}
        if len(s_filter)==len(pattern) and len(set(s_filter))==len(set(list(pattern))):
            for i in range(len(pattern)):
                if pattern[i] in hash_map:
                    if  hash_map[pattern[i]]!=s_filter[i]:
                        return False
                else:
                    hash_map[pattern[i]]=s_filter[i]
            return True
        else:
            return False


        