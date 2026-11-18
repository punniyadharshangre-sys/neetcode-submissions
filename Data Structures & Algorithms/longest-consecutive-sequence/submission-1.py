class Solution:
    def remove_duplicates(self,nums):
        length=len(nums)
        i,j=0,1
        dl=0
        while j<length-dl:
            if nums[i]==nums[j]:
                nums.pop(j)
                dl+=1
            else:
                j+=1
                i+=1
        return nums
        
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)>1:
            nums=self.remove_duplicates(sorted(nums))
            max_num=1
            i,j=0,1
            while j<len(nums):
                if j-i==nums[j]-nums[i]:
                    max_num=max(max_num,j-i+1)
                else:
                    while j-i!=nums[j]-nums[i] and i<j:
                        i+=1
                j+=1
            return max_num
        else:
            return len(nums)

        