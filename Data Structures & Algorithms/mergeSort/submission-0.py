# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def sort_logic(self,arr1,arr2,arr):
        len1=len(arr1)
        len2=len(arr2)
        i,j,r=0,0,0
        while i<len1 and j<len2:
            if arr1[i].key<=arr2[j].key:
                arr[r]=arr1[i]
                i+=1
            else:
                arr[r]=arr2[j]
                j+=1
            r+=1
        while i<len1:
            arr[r]=arr1[i]
            i+=1
            r+=1
        while j<len2:
            arr[r]=arr2[j]
            j+=1
            r+=1


    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs)<=1:
            return pairs
        mid=len(pairs)//2
        left=pairs[:mid]
        right=pairs[mid:]
        self.mergeSort(left)
        self.mergeSort(right)
        self.sort_logic(left,right,pairs)
        return pairs

