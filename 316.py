"""
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

示例 1：
    输入：s = "bcabc"
    输出："abc"

示例 2：
    输入：s = "cbacdcbc"
    输出："acdb"

提示：
    1 <= s.length <= 10^4
    s 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 为了得到字典序最小的字符串，需要删除 第一个满足条件 s[i] > s[i+1] 的 s[i]
    def removeDuplicateLetters(self, s: str) -> str:
        character_cnt = {}
        for character in s:
            character_cnt[character] = character_cnt.get(character, 0) + 1
        stack = []
        for character in s:
            if character not in stack:
                while stack and character < stack[-1] and character_cnt.get(stack[-1]) > 0:
                    stack.pop()
                stack.append(character)
            # character_cnt 表示了后续尚未处理的字符串中不同字符的统计量
            character_cnt[character] -= 1
        return "".join(stack)


s = "bcabc"
s = "cbacdcbc"
s = "bbcaac"
s = "edebbed"
print(Solution().removeDuplicateLetters(s))
