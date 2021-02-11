"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

示例 1:
    输入：text1 = "abcde", text2 = "ace"
    输出：3
    解释：最长公共子序列是 "ace"，它的长度为 3。

示例 2:
    输入：text1 = "abc", text2 = "abc"
    输出：3
    解释：最长公共子序列是 "abc"，它的长度为 3。

示例 3:
    输入：text1 = "abc", text2 = "def"
    输出：0
    解释：两个字符串没有公共子序列，返回 0。

提示:
    1 <= text1.length <= 1000
    1 <= text2.length <= 1000
    输入的字符串只含有小写英文字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_size, text2_size = len(text1), len(text2)
        # dp[i][j] 表示 text1[:i] 和 text2[:j] 的最大公共子序列
        dp = [[0] * (text2_size + 1) for _ in range(text1_size+1)]
        for text1_idx in range(1, text1_size+1):
            for text2_idx in range(1, text2_size+1):
                if text1[text1_idx-1] == text2[text2_idx-1]:
                    dp[text1_idx][text2_idx] = 1 + dp[text1_idx-1][text2_idx-1]
                else:
                    dp[text1_idx][text2_idx] = max(dp[text1_idx-1][text2_idx], dp[text1_idx][text2_idx-1])
        return dp[-1][-1]


text1, text2 = "abcde", "ace"
text1, text2 = "abcba", "abcbcba"
text1, text2 = "yzebsbuxmtcfmtodclszgh", "ejevmhcvshclydqrulwbyha"
print(Solution().longestCommonSubsequence(text1, text2))
