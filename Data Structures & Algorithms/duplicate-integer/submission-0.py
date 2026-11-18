class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map={}
        for k in nums:
            if k in hash_map:
                return True
            else:
                hash_map[k]=1
        return False
        