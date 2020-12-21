"""
找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:
    输入:
        s = "aaabb", k = 3
    输出:
        3

    最长子串为 "aaa" ，其中 'a' 重复了 3 次。

示例 2:
    输入:
        s = "ababbc", k = 2
    输出:
        5

    最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 暴力法
    def longestSubstring_1(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            cnt = [0] * 26
            for j in range(i, len(s)):
                cnt[ord(s[j]) - ord("a")] += 1
                for t in cnt:
                    if 0 < t < k:
                        break
                else:
                    res = max(res, j - i + 1)
        return res

    # 分治法
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        for character in set(s):
            if s.count(character) < k:
                return max(self.longestSubstring(substring, k) for substring in s.split(character))
        return len(s)


s, k = "aaabb", 3
s, k = "a", 1
print(Solution().longestSubstring(s, k))
