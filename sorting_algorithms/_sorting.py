

class Solution:

    def bubble_sort(self,arr):

        n = len(arr)
        for i in range(n-1):
            for j in range(0,n-1-i):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr

    def select_sort(self,arr):
        n = len(arr)
        for i in range(n):
            min_ind = i
            for j in range(i,n):
                if arr[min_ind]> arr[j]:
                    min_ind = j
            arr[min_ind],arr[i]=arr[i],arr[min_ind]
        return arr



    def merge_sort(self,arr):
        if len(arr)<=1:
            return arr
        mid = len(arr)//2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left,right)
    
    def merge(self,left,right):
        result =[]
        i=j=0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
            
        result+=left[i:]
        result+=right[j:]
        return result



arr = [3,2,4,5,1,9,0]
print(Solution().bubble_sort(arr))
print(Solution().select_sort(arr))
print(Solution().merge_sort(arr))