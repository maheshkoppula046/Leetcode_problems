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

    def linear_search_algorithm(self,arr,val):
        n=len(arr)
        for i in range(n):
            if arr[i] == val :
                return i

        return -1
    
arr = [2,3,4,1,6,8]
val = 6
print(Solution().linear_search_algorithm(arr,val))
