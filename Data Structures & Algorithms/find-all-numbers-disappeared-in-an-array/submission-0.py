class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length=len(nums)
        ans=[]
        for i in range(length):
            if i+1 not in nums:
                ans.append(i+1)
        return ans
       

        