"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n^2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 二分查找
    # 统计数组中不大于 idx 的数字条目
    # 如果这个数字条目刚不超过 idx，说明数字 1, ... idx 中无重复. 否则说明其中有重复
    def findDuplicate_1(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            cnt_le = 0
            for num in nums:
                if num <= mid + 1:
                    cnt_le += 1
            # 如果不大于 mid+1 的数 总计不超过 mid + 1 个，就说明数字 1, ..., mid + 1 都没有重复
            if cnt_le <= mid + 1:
                start = mid + 1
            else:
                end = mid

        return end + 1

    # 构造快慢指针法
    # 由数组建图，建立 idx -> nums[idx] 的边。由于存在的重复的数字 target，因此 target 这个位置一定有起码两条指向它的边，
    # 因此整张图一定存在环，且我们要找到的 target 就是这个环的入口
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
        return slow


nums = [1, 3, 4, 2, 2]
nums = [3, 1, 3, 4, 2]
nums = [2, 2, 2, 2, 2]
print(Solution().findDuplicate(nums))
