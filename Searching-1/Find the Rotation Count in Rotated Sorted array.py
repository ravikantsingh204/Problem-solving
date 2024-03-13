#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        low=0
        high=len(arr)-1
        while(low<high):
            mid=(low+high)//2
            if mid==0:
                if arr[mid]>arr[mid+1]:
                    return mid+1
            else:
                if arr[mid]>arr[mid+1]:
                    return mid+1
                if arr[mid]<arr[mid-1]:
                    return mid
            if arr[low]<arr[mid]:
                low=mid+1
            else:
                high=mid-1
        return 0
#{ 
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends


#solution 2 

class Solution:
    def findKRotation(self,arr,  n):
        # code here
        low=0
        high=len(arr)-1
        while(low<high):
            mid=(low+high)//2
            if arr[mid]>arr[mid+1]:
                return mid+1
            if arr[mid]<arr[mid-1]:
                return mid
            if arr[low]<arr[mid]:
                low=mid+1
            else:
                high=mid-1
        return 0
#{ 
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends