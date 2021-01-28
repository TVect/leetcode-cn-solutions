"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

示例 1：
    输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
    输出：[3,3,5,5,6,7]
    解释：
    滑动窗口的位置                最大值
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

示例 2：
    输入：nums = [1], k = 1
    输出：[1]

示例 3：
    输入：nums = [1,-1], k = 1
    输出：[1,-1]

示例 4：
    输入：nums = [9,11], k = 2
    输出：[11]

示例 5：
    输入：nums = [4,-2], k = 2
    输出：[4]

提示：
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import heapq


class Solution:

    # 使用单调队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 维护一个单调递减的队列
        queue = []
        ans = []
        nums_size = len(nums)
        for idx in range(nums_size):
            # 前面比当前数小的 都可以丢弃了
            while queue and nums[idx] >= nums[queue[-1]]:
                queue.pop()
            queue.append(idx)
            if idx >= k - 1:
                if queue[0] + k == idx:
                    queue.pop(0)
                ans.append(nums[queue[0]])
        return ans

    # 使用优先队列
    def maxSlidingWindow_1(self, nums: List[int], k: int) -> List[int]:
        nums_size = len(nums)
        windows = [[-nums[idx], idx] for idx in range(k)]
        heapq.heapify(windows)
        ans = [-windows[0][0]]
        for idx in range(k, nums_size):
            heapq.heappush(windows, [-nums[idx], idx])
            while windows[0][1] <= idx - k:
                heapq.heappop(windows)
            ans.append(-windows[0][0])
        return ans


nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
print(Solution().maxSlidingWindow(nums, k))
