def solution(arr,s):
    low=1
    high=len(arr)
    while(low<=high):
        mid=(low+high)//2
        if check(arr,mid,s):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
def check(arr,length,s):
    window_length=0
    element_sum=0
    for i in arr:
        if window_length<length and element_sum<s:
            element_sum=element_sum+i
            window_length+=1
        else:
            if element_sum>s:
                return False
            else:
                window_length=0
    return True

A=[1,3,4,2]
s=7
print(solution(A,s))