"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order,
return a sorted array of only the integers that appeared in all three arrays.

Example 1:
    Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
    Output: [1,5]
    Explanation: Only 1 and 5 appeared in the three arrays.

Constraints:
    1 <= arr1.length, arr2.length, arr3.length <= 1000
    1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""
from typing import List


class Solution:

    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        size1, size2, size3 = len(arr1), len(arr2), len(arr3)
        pt1, pt2, pt3 = 0, 0, 0
        rets = []
        while pt1 < size1 and pt2 < size2 and pt3 < size3:
            if arr1[pt1] == arr2[pt2] and arr2[pt2] == arr3[pt3]:
                rets.append(arr1[pt1])
            min_val = min(arr1[pt1], arr2[pt2], arr3[pt3])
            if arr1[pt1] == min_val:
                pt1 += 1
            if arr2[pt2] == min_val:
                pt2 += 1
            if arr3[pt3] == min_val:
                pt3 += 1
        return rets


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
print(Solution().arraysIntersection(arr1, arr2, arr3))
