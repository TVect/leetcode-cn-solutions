"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。

示例:
    输入: "aab"
    输出:
        [
          ["aa","b"],
          ["a","a","b"]
        ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 递归
    def partition_1(self, s: str) -> List[List[str]]:
        def is_palindromic(start_idx, end_idx):
            while start_idx < end_idx:
                if s[start_idx] != s[end_idx]:
                    return False
                start_idx +=1
                end_idx -= 1
            return True

        if len(s) == 0:
            return []
        rets = []
        if is_palindromic(0, len(s)-1):
            rets.append([s])
        for i in range(len(s)-1, 0, -1):
            if is_palindromic(i, len(s)-1):
                rets.extend([part + [s[i:]] for part in self.partition(s[:i])])
        return rets

    # 动态规划
    def partition_2(self, s: str) -> List[List[str]]:
        def is_palindromic(start_idx, end_idx):
            while start_idx < end_idx:
                if s[start_idx] != s[end_idx]:
                    return False
                start_idx +=1
                end_idx -= 1
            return True

        if len(s) == 0:
            return []

        rets = []
        for i in range(len(s)):
            # 计算 s[0, ..., i] 的所有有效分割结果
            rets.append([])
            if is_palindromic(0, i):
                rets[-1].append([s[0:i+1]])
            for j in range(i, 0, -1):
                if is_palindromic(j, i):
                    rets[-1].extend([part + [s[j:i+1]] for part in rets[j-1]])
        return rets[-1]

    # 回溯算法
    def partition_3(self, s: str) -> List[List[str]]:
        res = []

        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])

        helper(s, [])
        return res

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # dp[i][j] 表示字符串从位置 i 到位置 j (闭区间) 是否为回文子串
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
        res = []

        def helper(i, tmp):
            if i == n:
                res.append(tmp)
            for j in range(i, n):
                if dp[i][j]:
                    helper(j + 1, tmp + [s[i: j + 1]])

        helper(0, [])
        return res


s = "aab"
print(Solution().partition(s))
