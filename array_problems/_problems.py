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
    

    def max_sub_arr(self,arr):
        current_arr = arr[0]
        max_sum = arr[0]
        for num in arr[1:]:
            current_arr = max(current_arr + num,num)
            max_sum = max(max_sum,current_arr)
        return max_sum
    
    def max_profit(self,prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            min_price = min(min_price,price)
            max_profit = max(max_profit,price - min_price)
        return max_profit
    

    def majority_element(self,arr):
        count = {}
        majority_count = len(arr)//2
        for num in arr:
            count[num] = count.get(num,0)+1
            if count[num] > majority_count:
                return num
            
        return None
    

    def move_zeros(self,arr):
        left_index = 0 
        for right,num in enumerate(arr):
            if num != 0:
                arr[left_index],arr[right]=arr[right],arr[left_index]
                left_index+=1


    def merge(num1,num2):
        # nums1 = [1,2,3,0,0,0], m = 3
        # nums2 = [2,5,6],       n = 3
        pass


    def remove_duplicates_sorted_arr(self,arr):
        if not arr:
            return None
        
        k = 1
        n = len(n)
        for index in range(1,n):
            if arr[index] != arr[index -1]:
                arr[k] = arr[index]
                k+=1
        return k
    
    def merge_sorted_list(self,list1,list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2 :
            if list1.val <= list2.val:
                current.next = list
                list1 = list.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        else :
            current.next = list2

        return dummy.next


class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None


