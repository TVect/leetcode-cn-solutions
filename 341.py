"""
给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

示例 1:
    输入: [[1,1],2,[1,1]]
    输出: [1,1,2,1,1]
    解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。

示例 2:
    输入: [1,[4,[6]]]
    输出: [1,4,6]
    解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-nested-list-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator1:
    """ 借鉴 二叉树 遍历的做法来实现展平嵌套列表 """

    def __init__(self, nestedList: [NestedInteger]):
        self.all_integers = []
        for nestedItem in nestedList:
            self.traverse(nestedItem)

    def next(self) -> int:
        return self.all_integers.pop(0)

    def hasNext(self) -> bool:
        return len(self.all_integers) > 0

    def traverse(self, nestedItem: NestedInteger):
        if nestedItem.isInteger():
            self.all_integers.append(nestedItem.getInteger())
        else:
            for nestedItem in nestedItem.getList():
                self.traverse(nestedItem)


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList

    def next(self) -> int:
        return self.nestedList.pop(0).getInteger()

    def hasNext(self) -> bool:
        while len(self.nestedList) > 0 and not self.nestedList[0].isInteger():
            self.nestedList = self.nestedList.pop(0).getList() + self.nestedList
        return len(self.nestedList) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
