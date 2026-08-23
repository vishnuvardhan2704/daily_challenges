class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(len(nums)):
            # Expand the window
            if nums[right] == 0:
                zero_count += 1
            
            # Shrink the window until zero_count is valid
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Window length is (right - left + 1)
            max_len = max(max_len, right - left + 1)
            
        return max_len