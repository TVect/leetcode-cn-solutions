"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    # 递归/回溯
    def wordBreak_1(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def backtrace(input_str):
            if len(input_str) == 0:
                return True
            for i in range(0, len(input_str)):
                if backtrace(input_str[:i]) and input_str[i:] in wordDict:
                    return True
            return False

        return backtrace(s)

    # 动态规划
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        str_length = len(s)
        # dp[i] 表示 s[:i] 是否能拆成字典中的单词组合
        dp = [False] * (str_length+1)
        dp[0] = True

        for i in range(1, str_length+1):
            for k in range(0, i+1):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


s = "leetcode"
wordDict = ["leet", "code"]

s = "applepenapple"
wordDict = ["apple", "pen"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
'''
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
'''
print(Solution().wordBreak(s, wordDict))
