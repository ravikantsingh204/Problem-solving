class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        low,high=0,len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                res[0]=mid
                high=mid-1
            elif target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        low,high=0,len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                res[1]=mid
                low=mid+1
            elif target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return res