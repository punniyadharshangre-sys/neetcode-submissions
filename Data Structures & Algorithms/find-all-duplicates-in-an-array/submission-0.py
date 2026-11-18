class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_values=set()
        length=len(nums)
        deleted=0
        i=0
        res=[]
        while i<length-deleted:
            if nums[i] in hash_values:
                res.append(nums.pop(i))
                deleted+=1
            else:
                hash_values.add(nums[i])
                i+=1
        return res

