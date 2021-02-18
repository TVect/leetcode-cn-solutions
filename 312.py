"""
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 
这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
求所能获得硬币的最大数量。

示例 1：
    输入：nums = [3,1,5,8]
    输出：167
    解释：
        nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
        coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

示例 2：
    输入：nums = [1,5]
    输出：10

提示：
    n == nums.length
    1 <= n <= 500
    0 <= nums[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        nums_size = len(nums)
        # dp[i][j] 表示戳破 i -> j 之间所有的气球(不包括 i 和 j) 能获得的最多分数
        # dp[i][j] = max(dp[i][idx] + dp[idx][j] + nums[idx] for idx in range(i+1, j))
        dp = [[0] * nums_size for _ in range(nums_size)]
        for i in range(nums_size - 2):
            dp[i][i + 2] = nums[i] * nums[i+1] * nums[i+2]
        for i in range(nums_size - 3, -1, -1):
            for j in range(i + 2, nums_size):
                dp[i][j] = max(dp[i][idx] + dp[idx][j] + nums[idx] * nums[i] * nums[j] for idx in range(i + 1, j))
        return dp[0][nums_size-1]


nums = [3, 1, 5, 8]
nums = [1, 5]
print(Solution().maxCoins(nums))
