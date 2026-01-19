from collections import Counter

class Solution:
    
    def two_sum(self,arr,target):

        seen = {}

        for index, num in enumerate(arr):
            val = target - num
            if val in seen:
                return [seen[val],index]
            
            seen[num] = index
        return [-1,-1]
    
            
    # def contain_duplicates(self,arr):
    #     return len(arr) != len(set(arr))
    
    def contain_duplicates(self,arr):
        seen = set()
        for num in arr:
            if num in seen :
                return True
            seen.add(num)
        return False

    
    # def valid_anagram(self,str1,str2):
    #     return Counter(str1) == Counter(str2)

    def valid_anagram(self,str1,str2):
        if len(str1) != len(str2):
            return False
        count = {}
        for ch in str1:
            count[ch] = count.get(ch,0) + 1
        
        for ch in str2:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True
    

