class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        if low==high:
            return nums[low]
        elif nums[-1]!=nums[-2]:
            return nums[-1]
        elif nums[0]!=nums[1]:
            return nums[0]
        else:
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                    return nums[mid]
                elif nums[mid]==nums[mid-1]:
                    if mid%2==0:
                        high=mid-1
                    else:
                        low=mid+1
                else:
                    if mid%2==0:
                        low=mid+1
                    else:
                        high=mid-1