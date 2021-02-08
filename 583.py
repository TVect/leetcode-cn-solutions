"""
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例：
    输入: "sea", "eat"
    输出: 2
    解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

提示：
    给定单词的长度不超过500。
    给定单词中的字符只含有小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        word1_size, word2_size = len(word1), len(word2)
        # dp[i][j] 表示 word1[:i] 和 word2[:j] 的最小移动步数
        dp = [[0] * (word2_size + 1) for _ in range(word1_size+1)]

        for idx in range(1, word2_size+1):
            dp[0][idx] = idx
        for jdx in range(1, word1_size+1):
            dp[jdx][0] = jdx

        for idx in range(1, word1_size+1):
            for jdx in range(1, word2_size+1):
                if word1[idx-1] == word2[jdx-1]:
                    dp[idx][jdx] = dp[idx-1][jdx-1]
                else:
                    dp[idx][jdx] = min(dp[idx][jdx-1], dp[idx-1][jdx]) + 1
        return dp[-1][-1]

    # 也可以利用 最长公共子序列 来求解：min_distance = len(word1) + len(word2) - 2 * longestCommonSubstring(word1, word2)


word1, word2 = "sea", "eat"
print(Solution().minDistance(word1, word2))
