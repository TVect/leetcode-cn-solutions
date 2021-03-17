"""
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
每次转换只能改变一个字母。
转换后得到的单词必须是字典中的单词。

说明:
    如果不存在这样的转换序列，返回一个空列表。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:
    输入:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]
    输出:
        [["hit","hot","dot","dog","cog"],
         ["hit","hot","lot","log","cog"]]
示例 2:
    输入:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
    输出: []
    解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        all_words = list(set([beginWord] + wordList))
        words_cnt = len(all_words)

        if endWord not in all_words:
            return []

        # 为了加速，引入了中间单词（替换单词中每一个位置为 *）
        # 这样可以避免去直接比较两两单词间是否可以转换
        neighbors = {}
        for idx in range(words_cnt):
            for jdx in range(len(all_words[idx])):
                candidate = all_words[idx][:jdx] + "*" + all_words[idx][jdx+1:]
                if all_words[idx] not in neighbors:
                    neighbors[all_words[idx]] = []
                neighbors[all_words[idx]].append(candidate)
                if candidate not in neighbors:
                    neighbors[candidate] = []
                neighbors[candidate].append(all_words[idx])

        all_paths = []
        partial_paths = [[beginWord]]
        step_info = {beginWord: 0}
        while partial_paths:
            tmp_size = len(partial_paths)
            for idx in range(tmp_size):
                path = partial_paths.pop(0)
                if path[-1] == endWord:
                    all_paths.append(path)
                else:
                    for word in neighbors.get(path[-1], []):
                        if word not in step_info or step_info[word] == step_info[path[-1]] + 1:
                            step_info[word] = step_info[path[-1]] + 1
                            partial_paths.append(path + [word])
            if all_paths:
                break
        return [[word for word in path if "*" not in word] for path in all_paths]


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().findLadders(beginWord, endWord, wordList))
