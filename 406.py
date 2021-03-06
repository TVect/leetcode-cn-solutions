"""
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 暴力解法. 每次寻找 k=0 的[h, k]
    def reconstructQueue_1(self, people: List[List[int]]) -> List[List[int]]:
        rets = []
        # [item, 0] 表示在 已排序好的 rets 中有 0 个更高的排在 item 前面
        in_people = [[item, 0] for item in people]
        while len(in_people) > 0:
            leader = min([item for item in in_people if item[0][1] == item[1]], key=lambda x: x[0][0])
            rets.append(leader[0])
            in_people = [[item[0], item[1] + 1 if leader[0][0] >= item[0][0] else item[1]]
                         for item in in_people if item != leader]
        return rets

    # 将身高从小到大排列，在插入 [h, k] 时在前面预留k个空位
    def reconstructQueue_2(self, people: List[List[int]]) -> List[List[int]]:
        people_cnt = len(people)
        rets = [0] * people_cnt
        people.sort(key=lambda item: (item[0], -item[1]))
        for item in people:
            blank_cnt = 0
            for idx in range(people_cnt):
                if rets[idx] == 0:
                    if blank_cnt == item[1]:
                        rets[idx] = item
                        break
                    blank_cnt += 1
        return rets

    # 贪心算法
    # 取身高从高到低从今操作，身高高的排好相对顺序之后，插入身高低的，不会影响其前面的高个子人数
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        rets = []
        people.sort(key=lambda item: (-item[0], item[1]))
        for item in people:
            rets.insert(item[1], item)
        return rets


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue(people))
