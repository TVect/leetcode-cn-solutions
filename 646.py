"""
给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

示例：
    输入：[[1,2], [2,3], [3,4]]
    输出：2
    解释：最长的数对链是 [1,2] -> [3,4]

提示：
    给出数对的个数在 [1, 1000] 范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-pair-chain
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    # 动态规划
    def findLongestChain_1(self, pairs: List[List[int]]) -> int:
        pairs_size = len(pairs)
        pairs.sort()
        dp = [1] * pairs_size
        for idx in range(1, pairs_size):
            dp[idx] = max([dp[jdx] + 1 for jdx in range(idx) if pairs[jdx][1] < pairs[idx][0]],
                          default=dp[idx])
        return dp[-1]

    # 贪心算法
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda item: item[1])
        res = 1
        left_bound = pairs[0][1]
        for pair in pairs[1:]:
            if pair[0] > left_bound:
                res += 1
                left_bound = pair[1]
        return res


pairs = [[3, 4], [1, 2], [2, 3]]
pairs = [[7, 9], [4, 5], [7, 9], [-7, -1], [0, 10], [3, 10], [3, 6], [2, 3]]
print(Solution().findLongestChain(pairs))
