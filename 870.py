"""
给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。
返回 A 的任意排列，使其相对于 B 的优势最大化。

示例 1：
    输入：A = [2,7,11,15], B = [1,10,4,11]
    输出：[2,11,7,15]

示例 2：
    输入：A = [12,24,8,32], B = [13,25,32,11]
    输出：[24,32,8,12]

提示：
    1 <= A.length = B.length <= 10000
    0 <= A[i] <= 10^9
    0 <= B[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/advantage-shuffle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)
        sortedB = sorted(enumerate(B), key=lambda item: item[1])
        res = [0] * len(sortedA)
        startB, endB = 0, len(sortedB) - 1
        for num in sortedA:
            # 田忌赛马：
            # 如果 A 中最小元素如果大于 B 中最小元素，就将这两个元素对齐
            # 否则，将 A 中最小元素 和 B 中最大元素对齐
            if num > sortedB[startB][1]:
                res[sortedB[startB][0]] = num
                startB += 1
            else:
                res[sortedB[endB][0]] = num
                endB -= 1
        return res


A, B = [2, 7, 11, 15], [1, 10, 4, 11]
A, B = [12, 24, 8, 32], [13, 25, 32, 11]
A, B = [2, 0, 4, 1, 2], [1, 3, 0, 0, 2]
print(Solution().advantageCount(A, B))
