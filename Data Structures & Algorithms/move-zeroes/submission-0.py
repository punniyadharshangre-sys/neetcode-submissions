class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros=0
        length=len(nums)
        i=0
        while i<length-zeros:
            if nums[i]==0:
                zeros+=1
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
        return nums
        