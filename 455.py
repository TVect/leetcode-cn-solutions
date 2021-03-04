"""
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。
如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

示例 1:
    输入: g = [1,2,3], s = [1,1]
    输出: 1
    解释:
        你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
        虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
        所以你应该输出1。

示例 2:
    输入: g = [1,2], s = [1,2,3]
    输出: 2
    解释:
        你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
        你拥有的饼干数量和尺寸都足以让所有孩子满足。
        所以你应该输出2.


提示：
    1 <= g.length <= 3 * 104
    0 <= s.length <= 3 * 104
    1 <= g[i], s[j] <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/assign-cookies
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 贪心法
    # 给剩余孩子里最小饥饿度的孩子分配最小的能饱腹的饼干
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_sorted, s_sorted = sorted(g), sorted(s)
        g_size, s_size = len(g_sorted), len(s_sorted)
        g_idx, s_idx = 0, 0
        while s_idx < s_size and g_idx < g_size:
            if g_sorted[g_idx] <= s_sorted[s_idx]:
                g_idx += 1
            s_idx += 1
        return g_idx


g, s = [1, 2], [1, 2, 3]
g, s = [1, 2, 3], [1, 1]
print(Solution().findContentChildren(g, s))
