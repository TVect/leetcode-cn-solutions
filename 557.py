"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：
    输入："Let's take LeetCode contest"
    输出："s'teL ekat edoCteeL tsetnoc"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def reverseWords(self, s: str) -> str:
        return " ".join(item[::-1] for item in s.split())


s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))
