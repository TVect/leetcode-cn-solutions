"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

示例 1:
输入:
s: "cbaebabacd" p: "abc"
输出:
[0, 6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

示例 2:
输入:
s: "abab" p: "ab"
输出:
[0, 1, 2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 滑动窗口
    def findAnagrams_1(self, s: str, p: str) -> List[int]:
        char_cnt = {}
        for character in p:
            char_cnt[character] = char_cnt.get(character, 0) + 1
        if len(s) < len(p):
            return []

        rets = []
        tmp_char_cnt = {}
        for character in s[:len(p)]:
            tmp_char_cnt[character] = tmp_char_cnt.get(character, 0) + 1
        if tmp_char_cnt == char_cnt:
            rets.append(0)

        for idx in range(1, len(s)-len(p)+1):
            # s[idx-1] -> s[idx+len(s)-len(p)]
            tmp_char_cnt[s[idx - 1 + len(p)]] = tmp_char_cnt.get(s[idx - 1 + len(p)], 0) + 1
            tmp_char_cnt[s[idx-1]] -= 1
            if tmp_char_cnt[s[idx-1]] == 0:
                del tmp_char_cnt[s[idx-1]]
            if tmp_char_cnt == char_cnt:
                rets.append(idx)
        return rets

    # 滑动窗口 + 一些过滤
    def findAnagrams(self, s: str, p: str) -> List[int]:
        rets = []
        window, needs = {}, {}
        for c in p:
            needs[c] = needs.get(c, 0) + 1

        length_p, length_s = len(p), len(s)
        left, right = 0, 0
        while right < length_s:
            if s[right] not in needs:
                window.clear()
                left = right = right + 1
            else:
                window[s[right]] = window.get(s[right], 0) + 1
                if right - left + 1 == length_p:
                    if window == needs:
                        rets.append(left)
                    window[s[left]] -= 1
                    left += 1
                right += 1
        return rets


s = "cbaebabacd"
p = "abc"

s = "abab"
p = "ab"

print(Solution().findAnagrams(s, p))
