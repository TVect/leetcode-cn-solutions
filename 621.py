"""
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 ：
输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。
 

提示：
任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/task-scheduler
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from collections import Counter


class Solution:

    # 合理的安排任务：出现频率越多的任务越早安排
    # 将 n + 1 个任务为一轮，每一轮中选择 n + 1 个出现次数最多的任务执行
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        interval = 0
        while True:
            most_common_n = counter.most_common()[:n+1]
            for item in most_common_n:
                counter[item[0]] -= 1
                if counter[item[0]] == 0:
                    del counter[item[0]]
            if len(counter) > 0:
                interval += n+1
            else:
                interval += len(most_common_n)
                break
        return interval

    # 规划设计 得到 公式表示
    # 完成所有任务的最短时间取决于出现次数最多的任务数量
    def leastInterval_1(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        ele, cnt = counter.most_common(1)[0]
        return max((n+1) * (cnt - 1) + list(counter.values()).count(cnt), len(tasks))


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(Solution().leastInterval(tasks, n))
