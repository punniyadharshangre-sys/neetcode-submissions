class Solution:

        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map={}
        for i,s in enumerate(strs):
            key=''.join(sorted(list(s)))
            if key not in hash_map:
                hash_map[key]=[]
            hash_map[key].append(s)
            
        return list(hash_map.values())