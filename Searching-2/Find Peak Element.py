class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        elif nums[0]>nums[1]:
            return 0
        elif nums[-1]>nums[-2]:
            return n-1
        else:
            low,high=0,n-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                    return mid
                elif nums[mid+1]>nums[mid]:
                    low=mid+1
                else:
                    high=mid-1