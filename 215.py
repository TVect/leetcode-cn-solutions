"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 构造大小为 k 的小顶堆
    def findKthLargest_1(self, nums: List[int], k: int) -> int:
        import heapq
        max_k_heap = []
        for num in nums:
            heapq.heappush(max_k_heap, num)
            if len(max_k_heap) > k:
                heapq.heappop(max_k_heap)
        return max_k_heap[0]

    # 利用快速排序的思想
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(low, high):
            """ 从大到小 """
            pivot = nums[low]
            larger_pt = low
            for pt in range(low+1, high):
                if nums[pt] > pivot:
                    larger_pt += 1
                    nums[larger_pt], nums[pt] = nums[pt], nums[larger_pt]
            nums[larger_pt], nums[low] = nums[low], nums[larger_pt]
            # 结果：
            # larger_pt 及其左侧大于 pivot: nums[0, ..., larger_pt-1] > pivot
            # larger_pt 位置等于 pivot: nums[larger_pt] = pivot
            # larger_pt 右侧不大于 pivot: nums[larger_pt+1, ...] <= pivot
            return larger_pt

        low, high, target_position = 0, len(nums), k - 1
        while True:
            position = partition(low, high)
            if target_position == position:
                break
            elif target_position < position:
                high = position
            else:
                low = position + 1
        return nums[target_position]


nums = [3, 2, 1, 5, 6, 4]
k = 2

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

print(Solution().findKthLargest(nums, k))
