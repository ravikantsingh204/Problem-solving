#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here
		ans=-1
		low,high=0,m
        while(low<=high):
            mid=(low+high)//2
            res=mid**n
            if res<=m:
                low=mid+1
                if res==m:
                    ans=mid
            else:
                high=mid-1
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends