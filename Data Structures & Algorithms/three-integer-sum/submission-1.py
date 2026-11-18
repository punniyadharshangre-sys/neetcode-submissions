class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums=sorted(nums)
        for i in range(len(nums)-2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    # Found a triplet matching the target sum
                    if sorted([nums[left],nums[right],nums[i]]) not in ans:
                        ans.append(sorted([nums[left],nums[right],nums[i]]))
                    left += 1
                    right -= 1
                    
        return ans
        