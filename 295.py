"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，
    [2,3,4] 的中位数是 3

    [2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
    void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    double findMedian() - 返回目前所有元素的中位数。

示例：
    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3)
    findMedian() -> 2

进阶:
    如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
    如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-median-from-data-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_part = []
        self.right_part = []

    def addNum(self, num: int) -> None:
        if len(self.left_part) == len(self.right_part):
            # 找出 当前元素 和 右边 最小的元素，放入到左边
            heapq.heappush(self.right_part, num)
            ele = heapq.heappop(self.right_part)
            heapq.heappush(self.left_part, -ele)
        elif len(self.left_part) > len(self.right_part):
            # 找出 当前元素 和 左边 最大的元素，放入到右边
            heapq.heappush(self.left_part, -num)
            ele = heapq.heappop(self.left_part)
            heapq.heappush(self.right_part, -ele)

    def findMedian(self) -> float:
        if len(self.left_part) == len(self.right_part):
            return (- self.left_part[0] + self.right_part[0]) / 2
        elif len(self.left_part) > len(self.right_part):
            return - self.left_part[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

obj = MedianFinder()
for num in [1, 2, 3]:
    obj.addNum(num)
    print(obj.findMedian())
