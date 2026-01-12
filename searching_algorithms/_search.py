# 1. Linear Search (Sequential Search)
# ✅ Idea

# Check each element one by one until the target is found.

# 📌 When to use

# Data is unsorted

# Small list

# ⏱ Time Complexity

# Best: O(1)

# Worst: O(n)

class Solution:
    def __inti__(self):
        pass

    def linear_search(self,arr,val):
        n=len(arr)
        for i in range(n):
            if arr[i] == val :
                return i

        return -1
    
    def binary_search(self,arr,val):
        left = 0
        right = len(arr)
        while left <= right:
            mid = (left + right )//2
            if val == arr[mid]:
                return mid
            elif val < arr[mid]:
                right = mid - 1
            else :
                left = mid + 1
    
arr = sorted([2,3,4,1,6,8])
print(arr)
val = 6
print(Solution().linear_search_algorithm(arr,val))
print(Solution().binary_search(arr,val))