"""
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。
当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
    不允许旋转信封。

示例:
    输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    输出: 3
    解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/russian-doll-envelopes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from functools import cmp_to_key


class Solution:

    # 最长上升子序列
    # 动态规划: 有超过时间限制的风险
    def maxEnvelopes_1(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort()
        envelopes_size = len(envelopes)
        # dp[i] 表示以 envelopes[i] 为结尾的最长嵌套信封的个数
        dp = [1] * envelopes_size
        for idx in range(1, envelopes_size):
            dp[idx] = max(dp[jdx] + 1
                          if (envelopes[idx][0] > envelopes[jdx][0]) and (envelopes[idx][1] > envelopes[jdx][1])
                          else 1
                          for jdx in range(idx))
        return max(dp)

    # 最长上升子序列 优化
    # 对[w, h] 的第一个维度进行升序排序，第一个维度相等的时候按第二个维度的降序排列
    # 最后在第二个维度上找最长上升子序列即可
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        if not envelopes:
            return 0

        def compare(element1, element2):
            # 按第一个元素的从小到大排序，按第二个元素的从大到小排序
            if element1[0] > element2[0]:
                return 1
            elif element1[0] < element2[0]:
                return -1
            elif element1[0] == element2[0]:
                if element1[1] == element2[1]:
                    return 0
                elif element1[1] < element2[1]:
                    return 1
                else:
                    return -1

        envelopes.sort(key=cmp_to_key(compare))
        envelopes_size = len(envelopes)
        # dp[i] 表示以 envelopes[i] 为结尾的最长嵌套信封的个数
        dp = [1] * envelopes_size
        for idx in range(1, envelopes_size):
            dp[idx] = max(dp[jdx] + 1 if envelopes[idx][1] > envelopes[jdx][1] else 1 for jdx in range(idx))
        return max(dp)

    # TODO 使用 O(N log N) 的方式找最大上升子序列（patient game \ patient sorting）


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
# envelopes = [[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]]
print(Solution().maxEnvelopes(envelopes))
