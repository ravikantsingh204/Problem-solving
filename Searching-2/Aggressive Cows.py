#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        low=1
        high=stalls[-1]-stalls[0]+1
        ans=1
        while(low<=high):
            mid=(low+high)//2
            if Solution.isPossible(stalls,k,mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    def isPossible(stalls,cows,distance):
        n=len(stalls)
        last_cow = stalls[0]
        cows_placed = 1
        for i in range(1,n):
            if stalls[i]-last_cow>=distance:
                cows_placed+=1
                last_cow=stalls[i]
        return cows_placed>=cows
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends