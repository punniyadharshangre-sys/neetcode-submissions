class Solution:
    def find_deceresing_element(self,nums):
        prev=nums[0]
        for i,curr in enumerate(nums[1:]):
            if curr<prev:
                print(curr)
                return i
        return 0

    def findMin(self, nums: List[int]) -> int:
        prev=nums[0]
        for i,curr in enumerate(nums[1:]):
            if curr<prev:
                print(curr)
                return curr
        return nums[0]


        