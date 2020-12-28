"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
    输入: s1 = "ab" s2 = "eidbaooo"
    输出: True
    解释: s2 包含 s1 的排列之一 ("ba").

示例2:
    输入: s1= "ab" s2 = "eidboaoo"
    输出: False

注意：
    输入的字符串只包含小写字母
    两个字符串的长度都在 [1, 10,000] 之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import collections


class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_size = len(s2)
        need = collections.Counter(s1)
        window = {character: 0 for character in need}
        valid = 0
        left, right = 0, 0
        while right < s2_size:
            character = s2[right]
            right += 1
            if character in need:
                window[character] += 1
                if window[character] == need[character]:
                    valid += 1
            while valid == len(need):
                if right - left == len(s1):
                    return True
                character = s2[left]
                left += 1
                if character in need:
                    if window[character] == need[character]:
                        valid -= 1
                    window[character] -= 1
        return False


s1, s2 = "ab", "eidboaoo"
s1, s2 = "ab", "eidbaooo"
print(Solution().checkInclusion(s1, s2))
