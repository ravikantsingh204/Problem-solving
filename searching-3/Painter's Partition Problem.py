def findLargestMinDistance(boards:list, k:int):
    # Write your code here
    # Return an integer
    def painters(boards,max_limit):
        s=0
        painter=1
        for i in boards:
            s=s+i
            if s>max_limit:
                s=i
                painter+=1
        return painter
    # low=max(boards)
    # high=sum(boards)
    low=0
    high=0
    for i in boards:
        high=high+i
        if low<i:
            low=i
    while(low<=high):
        mid=(low+high)//2
        if painters(boards,mid)<=k:
            high=mid-1
        else:
            low=mid+1
    return low