"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]
 

提示：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 利用库函数
    def topKFrequent_1(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        return [num for num, _ in Counter(nums).most_common(k)]

    # 利用最小堆
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        heap = []
        for key, value in cnt.items():
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)][::-1]

    # 其他方法：利用快速排序的思想


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
