class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ans=[]
        length=len(nums)
        if length==0:
            ans.append([lower,upper])
            return ans
        if nums[0]>lower:
            ans.append([lower,nums[0]-1])
        for i in range(length-1):
            if nums[i+1] -nums[i]>1:
                ans.append([nums[i]+1,nums[i+1]-1])
        if upper>nums[length-1]:
            ans.append([nums[length-1]+1,upper])
        return ans







        