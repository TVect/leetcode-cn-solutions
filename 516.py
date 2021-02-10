"""
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

示例 1:
    输入: "bbbab"
    输出: 4
        一个可能的最长回文子序列为 "bbbb"。

示例 2:
    输入: "cbbd"
    输出: 2
        一个可能的最长回文子序列为 "bb"。

提示：
    1 <= s.length <= 1000
    s 只包含小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 动态规划
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] : 在子串 s[i..j] 中，最长回文子序列的长度为 dp[i][j]
        s_size = len(s)
        dp = [[0] * s_size for _ in range(s_size)]
        for i in range(s_size):
            dp[i][i] = 1

        for i in range(s_size-2, -1, -1):
            for j in range(i+1, s_size):
                if s[i] == s[j]:
                    dp[i][j] = max(2 + dp[i+1][j-1], dp[i+1][j], dp[i][j-1])
                    # dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    # 如果 s[i] != s[j] 那么 s[i] 或者 s[j] 一定不包含在 s[i, ..., j] 的最大回文字串中
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]

    # 或者当作 求ｓ和ｓ的逆序的最长公共子序列的，转化成最长公共子序列问题。


s = "bbbab"
print(Solution().longestPalindromeSubseq(s))
