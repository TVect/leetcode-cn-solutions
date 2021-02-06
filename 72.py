"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：
    插入一个字符
    删除一个字符
    替换一个字符
 

示例 1：
    输入：word1 = "horse", word2 = "ros"
    输出：3
    解释：
        horse -> rorse (将 'h' 替换为 'r')
        rorse -> rose (删除 'r')
        rose -> ros (删除 'e')

示例 2：
    输入：word1 = "intention", word2 = "execution"
    输出：5
    解释：
        intention -> inention (删除 't')
        inention -> enention (将 'i' 替换为 'e')
        enention -> exention (将 'n' 替换为 'x')
        exention -> exection (将 'n' 替换为 'c')
        exection -> execution (插入 'u') 

提示：
    0 <= word1.length, word2.length <= 500
    word1 和 word2 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 递归版本：超出时间限制
    def minDistance_1(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:-1], word2[:-1])
        else:
            return 1 + min(self.minDistance(word1[:-1], word2),
                           self.minDistance(word1, word2[:-1]),
                           self.minDistance(word1[:-1], word2[:-1]))

    # 动态规划版本
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        # dp[i][j] 表示 minDistance(word1[:i], word2[:j])
        word1_size, word2_size = len(word1), len(word2)
        dp = [[0] * (word2_size + 1) for _ in range(word1_size + 1)]
        # 初始化第一行
        for word2_idx in range(1, word2_size + 1):
            dp[0][word2_idx] = word2_idx
        # 初始化第一列
        for word1_idx in range(1, word1_size + 1):
            dp[word1_idx][0] = word1_idx

        for word1_idx in range(1, word1_size + 1):
            for word2_idx in range(1, word2_size + 1):
                if word1[word1_idx-1] == word2[word2_idx-1]:
                    dp[word1_idx][word2_idx] = dp[word1_idx-1][word2_idx-1]
                else:
                    dp[word1_idx][word2_idx] = 1 + min(dp[word1_idx - 1][word2_idx - 1],
                                                       dp[word1_idx - 1][word2_idx],
                                                       dp[word1_idx][word2_idx-1])
        return dp[-1][-1]


word1, word2 = "horse", "ros"
word1, word2 = "intention", "execution"
print(Solution().minDistance(word1, word2))
