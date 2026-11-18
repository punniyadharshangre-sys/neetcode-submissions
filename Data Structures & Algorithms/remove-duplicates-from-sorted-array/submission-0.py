class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=len(nums)
        i,j=0,1
        rem=0
        while j<length-rem:
            if nums[i]==nums[j]:
                nums[:]=nums[:j]+nums[j+1:]
                rem+=1
            else:
                j+=1
                i+=1
        print(nums)
        return len(nums)

        