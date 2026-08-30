class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        ans=nums[0]
        while left<right:
            if nums[left]<nums[right]:
                return min(ans,nums[left])
            mid=(left+right)//2
            ans=min(ans,nums[mid])
            if nums[mid]>=nums[left]:
                left=mid+1
                
            elif nums[mid]<nums[right]:
                right=mid-1
        return min(nums[left],ans)
            
        