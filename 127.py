"""
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。

说明:
    如果不存在这样的转换序列，返回 0。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:
    输入:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]
    输出: 5
    解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
         返回它的长度 5。
示例 2:
    输入:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
    输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 构造一张图。
    # 依据朴素的思路，我们可以枚举每一对单词的组合，判断它们是否恰好相差一个字符，以判断这两个单词对应的节点是否能够相连。
    # 但是这样效率太低，我们可以优化建图。
    # 具体地，我们可以创建虚拟节点。
    # 对于单词 hit，我们创建三个虚拟节点 *it、h*t、hi*，并让 hit 向这三个虚拟节点分别连一条边即可。
    # 如果一个单词能够转化为 hit，那么该单词必然会连接到这三个虚拟节点之一。
    # 对于每一个单词，我们枚举它连接到的虚拟节点，把该单词对应的 id 与这些虚拟节点对应的 id 相连即可。
    #
    # 进一步优化：双向广度优先搜索
    # 同时从 beginWord 和 endWord 开始搜索
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        connect_nodes = {}
        extended_wordList = wordList + [beginWord, endWord]
        for word in extended_wordList:
            if word not in connect_nodes:
                all_nodes = [word[:i] + "*" + word[i+1:] for i in range(len(word))]
                connect_nodes[word] = all_nodes
                for node in all_nodes:
                    if node not in connect_nodes:
                        connect_nodes[node] = []
                    connect_nodes[node].append(word)

        dist_to_begin = {word: -1 for word in connect_nodes}
        dist_to_end = {word: -1 for word in connect_nodes}
        begin_queue, end_queue = [beginWord], [endWord]
        hops = 0
        while len(begin_queue) > 0 or len(end_queue) > 0:
            hops += 1
            begin_queue_size, end_queue_size = len(begin_queue), len(end_queue)
            for _ in range(begin_queue_size):
                ele = begin_queue.pop(0)
                if dist_to_begin[ele] == -1:
                    dist_to_begin[ele] = hops
                    if dist_to_end[ele] != -1:
                        return (dist_to_begin[ele] + dist_to_end[ele]) // 2
                    begin_queue.extend(connect_nodes.get(ele, []))
            for _ in range(end_queue_size):
                ele = end_queue.pop(0)
                if dist_to_end[ele] == -1:
                    dist_to_end[ele] = hops
                    if dist_to_begin[ele] != -1:
                        return (dist_to_begin[ele] + dist_to_end[ele]) // 2
                    end_queue.extend(connect_nodes.get(ele, []))
        return 0


beginWord = "ymain"
endWord = "oecij"
wordList = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]

print(Solution().ladderLength(beginWord, endWord, wordList))

