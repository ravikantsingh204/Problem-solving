class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        low=1
        high=max(nums)

        while(low<=high):
            mid=(low+high)//2

            if Solution.operation_required(nums,mid)<=maxOperations:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def operation_required(nums,mid):
        operations=0
        for i in nums:
            operations=operations+((i-1)//mid)
        return operations