"""
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lexicon = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp = self.lexicon
        for character in word:
            if character not in tmp:
                tmp[character] = {}
            tmp = tmp[character]
        tmp["END"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.lexicon
        for character in word:
            if character not in tmp:
                return False
            tmp = tmp[character]
        return tmp.get("END", False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.lexicon
        for character in prefix:
            if character not in tmp:
                return False
            tmp = tmp[character]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

import pprint

trie = Trie()
trie.insert("apple")
pprint.pprint(trie.lexicon)
assert trie.search("apple") is True
assert trie.search("app") is False
assert trie.startsWith("app") is True
trie.insert("app")
pprint.pprint(trie.lexicon)
assert trie.search("app") is True
