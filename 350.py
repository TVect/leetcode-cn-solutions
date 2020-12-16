"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
    输入：nums1 = [1,2,2,1], nums2 = [2,2]
    输出：[2,2]

示例 2:
    输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出：[4,9]
 

说明：
    输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
    我们可以不考虑输出结果的顺序。

进阶：
    如果给定的数组已经排好序呢？你将如何优化你的算法？
    如果 nums1 的大小比 nums2 小很多，哪种方法更优？
    如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # Hash 表
    def intersect_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = {}
        for num in nums1:
            if num not in cnt:
                cnt[num] = [0, 0]
            cnt[num][0] += 1

        for num in nums2:
            if num not in cnt:
                cnt[num] = [0, 0]
            cnt[num][1] += 1

        return [key for key, values in cnt.items() for _ in range(min(values))]

    # 先排序 + 双指针遍历
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        pt1, pt2 = 0, 0
        nums1_size, nums2_size = len(nums1), len(nums2)
        rets = []
        while pt1 < nums1_size and pt2 < nums2_size:
            if nums1[pt1] < nums2[pt2]:
                pt1 += 1
            elif nums1[pt1] > nums2[pt2]:
                pt2 += 1
            else:
                rets.append(nums1[pt1])
                pt1 += 1
                pt2 += 1
        return rets


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersect(nums1, nums2))
