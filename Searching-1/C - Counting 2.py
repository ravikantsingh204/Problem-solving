N,Q=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
while(Q):
    Q-=1
    x=int(input())
    if x>arr[-1]:
        print(0)
    else:
        low=0
        high=N-1
        ans=high
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]>=x:
                high=mid-1
                ans=mid
            else:
                low=mid+1
        print(N-ans)