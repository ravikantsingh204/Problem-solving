class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if(nums[low]==nums[mid] and nums[mid]==nums[high]):
                low+=1
                high-=1
                continue
            if nums[low]<=nums[mid]:     # left sorted array
                if nums[low]<=target and target<nums[mid]:      #left part
                    high=mid-1
                else:       # right part
                    low=mid+1
            else:       # right sorted array 
                if nums[mid]<=target and target<=nums[high]:     # right part
                    low=mid+1
                else:     # left part
                    high=mid-1
        return False