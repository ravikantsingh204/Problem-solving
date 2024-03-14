class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if n<(m*k):
            return -1
        else:
            low=min(bloomDay)
            high=max(bloomDay)
            ans=high
            while(low<=high):
                mid=(low+high)//2
                count=0
                noBouquets=0
                for i in bloomDay:
                    if i<=mid:
                        count=count+1
                    else:
                        noBouquets=noBouquets+(count//k)
                        count=0
                noBouquets=noBouquets+(count//k)
                if noBouquets>=m:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans