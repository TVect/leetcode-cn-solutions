"""
给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。

示例 1:
    输入: s1 = "sea", s2 = "eat"
    输出: 231
    解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
        在 "eat" 中删除 "t" 并将 116 加入总和。
        结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。

示例 2:
    输入: s1 = "delete", s2 = "leet"
    输出: 403
    解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
        将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
        结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
        如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。

注意:
    0 < s1.length, s2.length <= 1000。
    所有字符串中的字符ASCII值在[97, 122]之间。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1_size, s2_size = len(s1), len(s2)
        # dp[i][j] 表示 s1[:i] 和 s2[:j] 的 最小 ASCII 删除和
        dp = [[0] * (s2_size+1) for _ in range(s1_size+1)]
        for idx in range(1, s2_size+1):
            dp[0][idx] = dp[0][idx-1] + ord(s2[idx-1])
        for jdx in range(1, s1_size+1):
            dp[jdx][0] = dp[jdx-1][0] + ord(s1[jdx-1])
        for idx in range(1, s1_size+1):
            for jdx in range(1, s2_size+1):
                if s1[idx-1] == s2[jdx-1]:
                    dp[idx][jdx] = dp[idx-1][jdx-1]
                else:
                    dp[idx][jdx] = min(dp[idx-1][jdx] + ord(s1[idx-1]),
                                       dp[idx][jdx-1] + ord(s2[jdx-1]))
        return dp[-1][-1]

    # 可以转换为 The longest common subsequence问题
    # 假设dp[i][j] 为S1, S2最大公共子串的所有字母的和，那么该问题的解为 Sum(S1,S2) - 2 * dp[s1.size()][s2.size()]


s1, s2 = "delete", "leet"
print(Solution().minimumDeleteSum(s1, s2))
