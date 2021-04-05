"""
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。
你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:
    输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
    输出: 16
    解释: 这两个单词为 "abcw", "xtfn"。

示例 2:
    输入: ["a","ab","abc","d","cd","bcd","abcd"]
    输出: 4
    解释: 这两个单词为 "ab", "cd"。

示例 3:
    输入: ["a","aa","aaa","aaaa"]
    输出: 0
    解释: 不存在这样的两个单词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-word-lengths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    # 优化字符串重复的判断: 使用 位数组，记录下每个字符串中出现出现的字符；出现某个字符，就将位数组的某一位设置位 1
    # 优化比较次数: 只需要考虑出现相同字符集的最长的字符串即可，所以可以记录下 出现的每种字符串 对应的最长字符串长度
    # 以上两种优化可以同时在对 字符串 预处理中 做掉
    def maxProduct(self, words: List[str]) -> int:
        # tmp_dict:
        # key: 字符串中字符转化为的二进制数字表示
        # value: 相同二进制数字表示对应的最长的单词长度
        tmp_dict = {}
        for word in words:
            tmp = 0
            for character in word:
                tmp |= (1 << (ord(character) - ord('a')))
            tmp_dict[tmp] = max(len(word), tmp_dict.get(tmp, 0))

        return max([tmp_dict[key1] * tmp_dict[key2]
                    for key1 in tmp_dict.keys() for key2 in tmp_dict.keys() if key1 & key2 == 0],
                   default=0)


words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
words = ["a", "aa", "aaa", "aaaa"]
print(Solution().maxProduct(words))
