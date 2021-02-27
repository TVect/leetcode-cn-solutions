"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：
    如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

致谢：
    特别感谢 @pbrother 添加此问题并且创建所有测试用例。

示例 1：
    输入：s = "abc", t = "ahbgdc"
    输出：true

示例 2：
    输入：s = "axc", t = "ahbgdc"
    输出：false

提示：
    0 <= s.length <= 100
    0 <= t.length <= 10^4
    两个字符串都只由小写字符组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def isSubsequence_1(self, s: str, t: str) -> bool:
        s_size, t_size = len(s), len(t)
        s_idx, t_idx = 0, 0
        while s_idx < s_size and t_idx < t_size:
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1
        return s_idx == s_size

    # 在 有大量输入的 S，需要依次检查它们是否为 T 的子序列 时的优化
    # 使用 动态规划 记录下 中间匹配过程需要的一些数据
    def isSubsequence(self, s: str, t: str) -> bool:
        s_size, t_size = len(s), len(t)
        if s_size == 0:
            return True
        if t_size == 0:
            return False

        # dp[i][j] 表示 t[idx:] 中 字符j 出现的第一个位置
        # 有递推公式 dp[i][j] = j if t[i+1] == j else t[i+1][j]
        dp = [[-1] * 26 for _ in range(t_size + 1)]
        dp[-2][ord(t[-1]) - ord('a')] = t_size - 1

        for idx in range(t_size-2, -1, -1):
            for jdx in range(26):
                dp[idx][jdx] = idx if ord(t[idx]) - ord('a') == jdx else dp[idx+1][jdx]

        s_idx, t_idx = 0, 0
        for s_idx in range(s_size):
            t_idx = dp[t_idx][ord(s[s_idx]) - ord('a')]
            if t_idx == -1:
                return False
            t_idx += 1
        return True


s, t = "", "ahbgdc"
s, t = "b", "c"
s, t = "aaaaaa", "bbaaaa"
print(Solution().isSubsequence(s, t))
