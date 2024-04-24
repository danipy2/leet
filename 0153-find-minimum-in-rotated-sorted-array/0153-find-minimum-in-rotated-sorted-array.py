class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            if nums[mid] <= nums[mid-1]:
                return nums[mid]
            elif nums[mid] >= nums[left] and nums[left] >nums[left-1]:
                left = mid + 1
            else:
                right = mid -1