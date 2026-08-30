class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        
        # 1. Direct Base Case: If already fully sorted, binary search entire array
        if nums[0] <= nums[-1]:
            return self.binary_search(nums, target, 0, n - 1)
            
        # 2. Otherwise, find inflection point
        pivot = self.find_pivot(nums)
        
        # 3. Choose the appropriate half and binary search
        if nums[0] <= target <= nums[pivot - 1]:
            return self.binary_search(nums, target, 0, pivot - 1)
        else:
            return self.binary_search(nums, target, pivot, n - 1)
            
    def find_pivot(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(self, nums: list[int], target: int, left: int, right: int) -> int:
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
