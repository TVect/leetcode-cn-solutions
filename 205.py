"""
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。
不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

示例 1:
    输入：s = "egg", t = "add"
    输出：true

示例 2：
    输入：s = "foo", t = "bar"
    输出：false

示例 3：
    输入：s = "paper", t = "title"
    输出：true

提示：
    可以假设 s 和 t 长度相同。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/isomorphic-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_size, t_size = len(s), len(t)
        if s_size != t_size:
            return False
        # 记录 s, t 中对应字符前一次出现的位置
        s_mapping, t_mapping = {}, {}
        for idx in range(s_size):
            if s_mapping.get(s[idx]) != t_mapping.get(t[idx]):
                return False
            s_mapping[s[idx]] = idx
            t_mapping[t[idx]] = idx
        return True


s, t = "egg",  "add"
s, t = "foo",  "bar"
print(Solution().isIsomorphic(s, t))
